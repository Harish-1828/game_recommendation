# 🚀 QUICK START GUIDE

## Run Everything with One Command (Windows)

Double-click `run_project.bat` or run in terminal:
```bash
run_project.bat
```

This will automatically:
1. Install all dependencies
2. Train the ML model
3. Start the Flask application

---

## Manual Step-by-Step Commands

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python train_model.py
```

### 3. Run the Flask App
```bash
python app.py
```

### 4. Open Browser
Navigate to: `http://127.0.0.1:5000/`

---

## Commands Summary

| Command | Purpose |
|---------|---------|
| `pip install -r requirements.txt` | Install all dependencies |
| `python train_model.py` | Train ML model and save files |
| `python app.py` | Start Flask web server |
| `CTRL+C` | Stop the Flask server |

---

## First Time Setup (5 minutes)

1. ✅ Ensure Python 3.8+ is installed
2. ✅ Run: `pip install -r requirements.txt`
3. ✅ Run: `python train_model.py` (takes ~1-2 minutes)
4. ✅ Run: `python app.py`
5. ✅ Open: `http://localhost:5000/`

---

## Testing the Application

**Sample Positive Review:**
```
This game is absolutely amazing! Best RPG I've ever played. 
The graphics are stunning and gameplay is incredibly smooth.
```

**Sample Negative Review:**
```
Terrible game. Complete waste of money. Buggy and boring.
I want my money back. Do not recommend.
```

---

## Expected Model Accuracy

- Training Accuracy: ~92-94%
- Testing Accuracy: ~90-92%

---

## Project Files Generated After Training

- `model.pkl` - Trained Logistic Regression model
- `vectorizer.pkl` - TF-IDF vectorizer

---

## Need Help?

Check the detailed **README.md** for:
- Complete documentation
- Troubleshooting guide
- Project structure
- Technical details
- Interview talking points

---

**🎮 Happy Coding!**
