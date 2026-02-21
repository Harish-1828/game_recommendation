# 🎮 STEAM REVIEW PREDICTOR - COMMANDS CHEAT SHEET

## 🚀 Essential Commands

### First Time Setup
```bash
# Install all dependencies
pip install -r requirements.txt

# Train the model (takes 1-2 minutes)
python train_model.py

# Run the Flask application
python app.py
```

### Quick Run (After Setup)
```bash
# Just run the app
python app.py
```

### Automated Run (Windows)
```bash
# Run everything automatically
run_project.bat
```

---

## 🌐 Access URLs

| URL | Description |
|-----|-------------|
| http://127.0.0.1:5000/ | Main application |
| http://localhost:5000/ | Alternative URL |

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| CTRL+C | Stop Flask server |
| CTRL+R | Refresh browser |

---

## 📂 Important Files

| File | Purpose | Size |
|------|---------|------|
| `train_model.py` | ML training script | Training only |
| `app.py` | Flask web app | Always needed |
| `model.pkl` | Trained model | Generated (~5MB) |
| `vectorizer.pkl` | TF-IDF vectorizer | Generated (~2MB) |
| `steam.csv` | Dataset | 100K+ rows (~75MB) |
| `requirements.txt` | Dependencies | Reference |

---

## 🔍 Common Tasks

### Check if Model Exists
```bash
# Windows PowerShell
Test-Path model.pkl
Test-Path vectorizer.pkl

# Windows CMD
dir model.pkl
dir vectorizer.pkl
```

### Retrain Model
```bash
python train_model.py
```

### Check Python Version
```bash
python --version
```

### List Installed Packages
```bash
pip list
```

### Update Package
```bash
pip install --upgrade flask
```

---

## 🐛 Troubleshooting Commands

### Port Already in Use
```bash
# Kill Python processes (Windows PowerShell)
Get-Process python | Stop-Process -Force
```

### Module Not Found
```bash
pip install -r requirements.txt --force-reinstall
```

### Check Flask Status
```bash
# If running in background, check browser:
# http://127.0.0.1:5000/
```

---

## 📊 Model Performance Quick Check

After running `train_model.py`, look for:
- ✅ Training Accuracy: ~97%+
- ✅ Testing Accuracy: ~97%+
- ✅ Files created: model.pkl, vectorizer.pkl

---

## 🧪 Test Samples (Copy-Paste Ready)

### Positive Review
```
This game is absolutely amazing! The graphics are stunning, gameplay is smooth, and the story keeps you engaged for hours. Best game I've played this year. Highly recommended for RPG fans!
```

### Negative Review
```
Terrible game, complete waste of money. The game is full of bugs, crashes constantly, and the developers clearly abandoned it. Graphics are outdated and gameplay is boring. Do not buy this under any circumstances!
```

### Neutral Review
```
Decent game with some good moments. The graphics are okay and the story is somewhat interesting. It has potential but needs more polish. Worth it on sale maybe.
```

---

## 📁 Project Structure (Visual)

```
datascience/
│
├── 🐍 Python Scripts
│   ├── train_model.py
│   └── app.py
│
├── 📊 Data
│   ├── steam.csv (original)
│   ├── model.pkl (generated)
│   └── vectorizer.pkl (generated)
│
├── 🌐 Web
│   └── templates/
│       └── index.html
│
├── 📝 Documentation
│   ├── README.md (full guide)
│   ├── QUICKSTART.md (quick start)
│   ├── PROJECT_SUMMARY.md (overview)
│   └── COMMANDS.md (this file)
│
└── ⚙️ Configuration
    ├── requirements.txt
    ├── .gitignore
    └── run_project.bat
```

---

## 💡 Pro Tips

1. **Always train first**: Run `train_model.py` before `app.py`
2. **Check model files**: Ensure `.pkl` files exist before running app
3. **Port conflict**: If port 5000 busy, stop other Flask apps
4. **Browser cache**: Hard refresh (CTRL+F5) if UI doesn't update
5. **Debug mode**: Flask debug=True auto-reloads on code changes

---

## 🎓 For Demos/Interviews

### Quick Demo Script (5 minutes)
```bash
# 1. Show project structure
dir

# 2. Show accuracy
# (Already trained, show the output or retrain)
python train_model.py

# 3. Start app
python app.py

# 4. Open browser and demonstrate predictions
# - Show positive review → Recommended
# - Show negative review → Not Recommended
# - Highlight confidence scores
```

### Key Points to Mention
- 50K training samples
- 97%+ accuracy
- TF-IDF + Logistic Regression
- Real-time predictions
- Production-ready code

---

## 🔗 Quick Links

| Resource | File |
|----------|------|
| Full Documentation | README.md |
| Quick Start | QUICKSTART.md |
| Project Overview | PROJECT_SUMMARY.md |
| Code | train_model.py, app.py |
| UI | templates/index.html |

---

## ⚡ Most Used Commands (Priority Order)

1. `python app.py` → Run application
2. `python train_model.py` → Train model
3. `pip install -r requirements.txt` → Install dependencies
4. `CTRL+C` → Stop server

---

**Last Updated:** February 21, 2026  
**Status:** ✅ Production Ready

---

**🚀 Keep this file handy for quick reference!**
