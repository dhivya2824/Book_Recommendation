from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import json
import os

app = Flask(__name__)
app.secret_key = "bookverse_secret_key"

FAVORITES_FILE = "user_favorites.json"

def load_favorites():
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_favorites(data):
    with open(FAVORITES_FILE, 'w') as f:
        json.dump(data, f)


# ---------------- LOGIN PAGE (FIRST PAGE) ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # (Demo login – no database)
        session["user"] = request.form["email"]
        return redirect(url_for("home"))

    return render_template("login.html")


# ---------------- REGISTER PAGE ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Normally save user details in DB
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- BOOKVERSE HOME PAGE ----------------
@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    df = pd.read_csv("Books.csv", dtype=str)
    df = df[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-M']]
    df['Image-URL-M'] = df['Image-URL-M'].fillna("")
    
    search = request.args.get('search', '').lower()
    if search:
        df = df[df['Book-Title'].str.lower().str.contains(search, na=False) | 
                df['Book-Author'].str.lower().str.contains(search, na=False)]
    
    df = df.head(1000)
    books = df.to_dict(orient="records")
    
    favorites = load_favorites()
    user_favs = favorites.get(session['user'], [])
    
    return render_template("index.html", books=books, favorites=user_favs)


# ---------------- FAVORITES ----------------
@app.route("/toggle_favorite", methods=["POST"])
def toggle_favorite():
    if "user" not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    book_title = request.json.get('title')
    favorites = load_favorites()
    user = session['user']
    
    if user not in favorites:
        favorites[user] = []
    
    if book_title in favorites[user]:
        favorites[user].remove(book_title)
    else:
        favorites[user].append(book_title)
    
    save_favorites(favorites)
    return jsonify({"success": True, "favorites": favorites[user]})

@app.route("/favorites")
def favorites_page():
    if "user" not in session:
        return redirect(url_for("login"))
    
    favorites = load_favorites()
    user_favs = favorites.get(session['user'], [])
    
    if not user_favs:
        return render_template("favorites.html", books=[])
    
    df = pd.read_csv("Books.csv", dtype=str)
    df = df[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-M']]
    df['Image-URL-M'] = df['Image-URL-M'].fillna("")
    df = df[df['Book-Title'].isin(user_favs)]
    
    books = df.to_dict(orient="records")
    return render_template("favorites.html", books=books)

@app.route("/recommend")
def recommend():
    if "user" not in session:
        return redirect(url_for("login"))
    
    favorites = load_favorites()
    user_favs = favorites.get(session['user'], [])
    
    df = pd.read_csv("Books.csv", dtype=str)
    df = df[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-M']]
    df['Image-URL-M'] = df['Image-URL-M'].fillna("")
    
    if user_favs:
        fav_authors = df[df['Book-Title'].isin(user_favs)]['Book-Author'].unique()
        recommendations = df[df['Book-Author'].isin(fav_authors) & ~df['Book-Title'].isin(user_favs)].head(20)
    else:
        recommendations = df.head(20)
    
    books = recommendations.to_dict(orient="records")
    return render_template("recommend.html", books=books)

# ---------------- ADD BOOK ----------------
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if "user" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        new_book = {
            'Book-Title': request.form['title'],
            'Book-Author': request.form['author'],
            'Year-Of-Publication': request.form['year'],
            'Publisher': request.form['publisher'],
            'Image-URL-M': request.form['image_url']
        }
        
        df = pd.read_csv("Books.csv", dtype=str)
        new_row = pd.DataFrame([new_book])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv("Books.csv", index=False)
        
        return redirect(url_for("home"))
    
    return render_template("add_book.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
