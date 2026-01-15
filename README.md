# 📚 BookVerse - Book Recommendation System

A personalized book recommendation web application built with Flask that helps users discover and manage their favorite books.

## ✨ Features

- 🔐 **User Authentication** - Login and registration system
- 🔍 **Smart Search** - Search books by title or author in real-time
- ❤️ **Favorites System** - Save and manage your favorite books
- ✨ **Personalized Recommendations** - Get book suggestions based on your favorite authors
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 📱 **Responsive Design** - Works seamlessly on all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
```bash
cd Book_Recommender_Flask
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Ensure Books.csv is in the project root**
   - The application requires a `Books.csv` file with columns: `Book-Title`, `Book-Author`, `Year-Of-Publication`, `Publisher`, `Image-URL-M`

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
   - Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
Book_Recommender_Flask/
│
├── app.py                  # Main Flask application
├── Books.csv              # Book dataset
├── requirements.txt       # Python dependencies
├── user_favorites.json    # User favorites storage (auto-generated)
│
├── templates/
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── index.html         # Home page with book catalog
│   ├── favorites.html     # User's favorite books
│   └── recommend.html     # Personalized recommendations
│
└── static/
    └── style.css          # Styling and animations
```

## 🎯 How It Works

### 1. Authentication
- Users can register and login (demo mode - no database required)
- Session management keeps users logged in

### 2. Browse Books
- View a catalog of 1000+ books with cover images
- Search functionality filters books instantly
- Click the heart icon to add books to favorites

### 3. Favorites
- Save books you're interested in
- Access your favorites anytime from the Favorites page
- Data persists across sessions using JSON storage

### 4. Recommendations
- Algorithm analyzes your favorite books
- Suggests books from authors you like
- Discovers new titles based on your preferences

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Data Processing**: Pandas
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: JSON file-based storage
- **Session Management**: Flask sessions

## 📊 Features Breakdown

| Feature | Description | Status |
|---------|-------------|--------|
| User Login | Session-based authentication | ✅ |
| Book Catalog | Display books with images | ✅ |
| Search | Real-time search by title/author | ✅ |
| Favorites | Save/remove favorite books | ✅ |
| Recommendations | Author-based suggestions | ✅ |
| Responsive UI | Mobile-friendly design | ✅ |

## 🎨 UI Highlights

- **Gradient Backgrounds** - Eye-catching purple-pink gradients
- **Glass Morphism** - Modern frosted glass effect on cards
- **Smooth Animations** - Hover effects and heartbeat animations
- **Clean Navigation** - Easy access to all features

## 🔮 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User ratings and reviews
- [ ] Advanced recommendation algorithms (collaborative filtering)
- [ ] Book details modal with descriptions
- [ ] Reading status tracker (Want to Read, Reading, Finished)
- [ ] Social features (share favorites with friends)
- [ ] Export favorites as PDF/CSV

## 📝 Notes

- This is a demo application using session-based authentication
- User data is stored in `user_favorites.json`
- For production use, implement proper database and password hashing

## 👨‍💻 Author

Mini Project - Book Recommendation System

## 📄 License

This project is open source and available for educational purposes.

---

**Enjoy discovering your next favorite book! 📖✨**
