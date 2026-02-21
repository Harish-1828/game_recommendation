# 🎮 Steam Game Review Recommendation Prediction

A complete end-to-end **Machine Learning project** that predicts whether a Steam game review recommends a game or not using **Natural Language Processing (NLP)** and **Flask Web Application**.

## 📋 Project Overview

This project implements a **supervised text classification model** that analyzes Steam game reviews and predicts whether the review recommends the game. The model is deployed using a **Flask web application** with an interactive user interface.

### 🎯 Key Features

- ✅ Text Classification using **TF-IDF Vectorization**
- ✅ **Logistic Regression** model for predictions
- ✅ Trained on **50,000 Steam game reviews**
- ✅ **Flask-based web interface** for real-time predictions
- ✅ **Confidence score** for each prediction
- ✅ Clean and responsive UI design
- ✅ Production-ready code with error handling
- ✅ Beginner-friendly and well-documented

---

## 📁 Project Structure

```
datascience/
│
├── train_model.py          # ML training script
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation (this file)
├── steam.csv              # Original dataset (100K+ reviews)
│
├── model.pkl              # Trained ML model (generated after training)
├── vectorizer.pkl         # TF-IDF vectorizer (generated after training)
│
├── templates/
│   └── index.html         # Web interface template
│
└── dataset/               # Additional data (if any)
```

---

## 🛠️ Technologies Used

| Technology       | Purpose                          |
|------------------|----------------------------------|
| Python 3.x       | Core programming language        |
| Flask            | Web framework                    |
| Scikit-learn     | Machine learning library         |
| Pandas           | Data manipulation                |
| NumPy            | Numerical computations           |
| TF-IDF           | Text vectorization               |
| Logistic Regression | Classification algorithm      |
| HTML/CSS         | Frontend design                  |

---

## ⚙️ Installation & Setup

### Step 1: Prerequisites

Make sure you have **Python 3.8+** installed on your system.

Check Python version:
```bash
python --version
```

### Step 2: Clone or Download the Project

If you haven't already, navigate to your project directory:
```bash
cd e:\datascience
```

### Step 3: Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```

This will install:
- Flask (Web Framework)
- Pandas (Data Processing)
- NumPy (Numerical Operations)
- Scikit-learn (Machine Learning)

---

## 🚀 How to Run the Project

### Step 1: Train the Machine Learning Model

Before running the Flask app, you need to train the model:

```bash
python train_model.py
```

**What this does:**
1. Loads the first 50,000 rows from `steam.csv`
2. Preprocesses and cleans the review text
3. Splits data into training (80%) and testing (20%) sets
4. Vectorizes text using **TF-IDF** (max 3000 features)
5. Trains a **Logistic Regression** classifier
6. Evaluates model performance (accuracy, precision, recall, F1-score)
7. Saves `model.pkl` and `vectorizer.pkl` files
8. Shows sample predictions

**Expected Output:**
```
======================================================================
STEAM GAME REVIEW RECOMMENDATION PREDICTION
======================================================================

[1/7] Loading dataset...
✓ Loaded 50000 rows from steam.csv

[2/7] Preprocessing data...
✓ Dataset shape after cleaning: (49876, 2)

[3/7] Splitting dataset into train and test sets (80/20)...
✓ Training set: 39900 samples
✓ Testing set: 9976 samples

[4/7] Vectorizing text using TF-IDF (max_features=3000)...
✓ Vectorization complete. Shape: (39900, 3000)

[5/7] Training Logistic Regression model...
✓ Model training complete!

[6/7] Evaluating model performance...

======================================================================
MODEL PERFORMANCE
======================================================================
Training Accuracy: 92.54%
Testing Accuracy:  90.87%
======================================================================
```

### Step 2: Run the Flask Application

After training is complete, start the web server:

```bash
python app.py
```

**Expected Output:**
```
======================================================================
Starting Flask Application...
======================================================================
Application is running at: http://127.0.0.1:5000/
Press CTRL+C to stop the server
======================================================================

 * Serving Flask app 'app'
 * Debug mode: on
```

### Step 3: Access the Web Application

Open your web browser and go to:
```
http://127.0.0.1:5000/
```

or

```
http://localhost:5000/
```

---

## 💻 Using the Application

1. **Enter a Review**: Type or paste a Steam game review in the text area
2. **Click "Analyze Review"**: The model will process your input
3. **View Results**: See the prediction (Recommended/Not Recommended) with confidence percentage

### Example Reviews to Test:

**Positive Review:**
```
This game is absolutely amazing! The graphics are stunning, gameplay is smooth, 
and the story keeps you engaged for hours. Best game I've played this year. 
Highly recommended!
```

**Negative Review:**
```
Terrible game, waste of money. Bugs everywhere, poor graphics, and boring gameplay. 
The developers clearly didn't care. Do not buy this game under any circumstances.
```

**Neutral Review:**
```
Decent game with some good moments. The graphics are okay and the story is 
somewhat interesting. It's not bad but not great either. Worth it on sale.
```

---

## 📊 Model Details

### Dataset Information
- **Source**: Steam game reviews (steam.csv)
- **Total Rows**: 100,002 reviews
- **Training Data**: First 50,000 rows
- **Features Used**: Review text (`review` column)
- **Target Variable**: Recommendation status (`recommended` column)

### Model Configuration
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
  - Max Features: 3000
  - N-grams: Unigrams and Bigrams (1, 2)
  - Lowercase: Yes
  - Stop Words: English
  
- **Algorithm**: Logistic Regression
  - Solver: lbfgs
  - Max Iterations: 1000
  - Regularization (C): 1.0
  - Multi-threading: Enabled (n_jobs=-1)

- **Train-Test Split**: 80% - 20%
- **Random State**: 42 (for reproducibility)

### Model Performance
- **Training Accuracy**: ~92-94%
- **Testing Accuracy**: ~90-92%
- **Metrics**: Precision, Recall, F1-Score (provided in classification report)

---

## 📂 File Descriptions

### Core Files

#### `train_model.py`
Complete ML pipeline that:
- Loads and preprocesses data
- Creates TF-IDF features
- Trains Logistic Regression model
- Evaluates performance
- Saves trained model artifacts

#### `app.py`
Flask web application that:
- Loads trained model and vectorizer
- Handles HTTP requests
- Processes user input
- Returns predictions with confidence scores
- Includes error handling

#### `templates/index.html`
Web interface with:
- Modern, responsive design
- Steam-themed color scheme
- Input form for reviews
- Results display with visual feedback
- Information section

#### `requirements.txt`
Python package dependencies with specific versions

### Generated Files (After Training)

#### `model.pkl`
Serialized Logistic Regression model (pickled)

#### `vectorizer.pkl`
Serialized TF-IDF vectorizer (pickled)

---

## 🎯 Project Highlights for Placements/Interviews

### Technical Skills Demonstrated:
1. **Machine Learning**: Supervised learning, classification algorithms
2. **NLP**: Text preprocessing, TF-IDF vectorization
3. **Python Programming**: Clean, modular, well-documented code
4. **Web Development**: Flask framework, RESTful APIs
5. **Data Science**: Pandas, NumPy, data preprocessing
6. **Model Deployment**: Pickle, production-ready code
7. **Frontend**: HTML, CSS, responsive design
8. **Best Practices**: Error handling, validation, documentation

### Key Talking Points:
- ✅ Complete end-to-end ML pipeline
- ✅ Real-world dataset (100K+ Steam reviews)
- ✅ Model evaluation and performance metrics
- ✅ Web application deployment
- ✅ User-friendly interface
- ✅ Production-ready code with error handling
- ✅ Scalable architecture

---

## 🔧 Troubleshooting

### Issue: Module not found error
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Model files not found
**Solution**: Train the model first
```bash
python train_model.py
```

### Issue: Port 5000 already in use
**Solution**: Change port in app.py or kill the process
```python
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: CSV file not found
**Solution**: Ensure `steam.csv` is in the project root directory

---

## 📈 Future Enhancements

Potential improvements for this project:

1. **Model Improvements**:
   - Try other algorithms (Random Forest, XGBoost, Neural Networks)
   - Implement word embeddings (Word2Vec, GloVe)
   - Add sentiment intensity analysis
   - Handle multiple languages

2. **Features**:
   - Add review rating (1-5 stars)
   - Show word clouds of important features
   - Batch prediction support
   - Review sentiment visualization

3. **Deployment**:
   - Deploy on cloud platforms (Heroku, AWS, Azure)
   - Add database for storing predictions
   - Implement user authentication
   - Create REST API endpoints

4. **UI/UX**:
   - Add dark/light mode toggle
   - Real-time prediction as you type
   - Show similar reviews
   - Add prediction history

---

## 📝 License

This project is created for educational and portfolio purposes.

---

## 👨‍💻 Author

Created as a placement-ready machine learning project demonstrating:
- End-to-end ML pipeline development
- NLP and text classification
- Web application development
- Production-ready code practices

---

## 🎓 Learning Resources

To understand this project better, learn about:
- **Machine Learning**: Classification algorithms
- **NLP**: Text preprocessing, TF-IDF, tokenization
- **Flask**: Python web framework basics
- **Scikit-learn**: ML library documentation
- **Model Deployment**: Pickle, model serving

---

## ⭐ Conclusion

This project demonstrates a complete **Machine Learning workflow** from data processing to model deployment. It's suitable for:
- **College Projects**
- **Placement Interviews**
- **Portfolio Building**
- **Learning ML/NLP Concepts**

The code is clean, well-documented, and follows industry best practices, making it ideal for showcasing in interviews and resumes.

---

**Happy Learning! 🚀**
