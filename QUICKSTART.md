# 🚀 Quick Start Guide

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Run the Application
```bash
python app.py
```

## Step 3: Open Browser
Go to: http://127.0.0.1:5000

## Step 4: Login
- Enter any email (e.g., test@example.com)
- Click Login

## Step 5: Explore Features
- Browse books on home page
- Click ❤️ to add favorites
- Use search bar to find books
- Filter by year using dropdown
- Visit "Favorites" to see saved books
- Check "Recommendations" for suggestions

## Troubleshooting

### If you get "Module not found" error:
```bash
pip install Flask pandas
```

### If port 5000 is busy:
Change the last line in app.py to:
```python
app.run(debug=True, port=5001)
```

### To stop the server:
Press `Ctrl + C` in terminal
