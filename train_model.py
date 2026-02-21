"""
Steam Game Review Recommendation Prediction - ML Training Script
This script trains a Logistic Regression model using TF-IDF vectorization
to predict whether a Steam review recommends a game or not.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import warnings
warnings.filterwarnings('ignore')

# Configuration
DATA_FILE = 'steam_reviews.csv'
MAX_ROWS = 50000
RANDOM_STATE = 42
TEST_SIZE = 0.2
MAX_FEATURES = 3000

print("=" * 70)
print("STEAM GAME REVIEW RECOMMENDATION PREDICTION")
print("=" * 70)

# Step 1: Load Dataset
print("\n[1/7] Loading dataset...")
df = pd.read_csv(DATA_FILE, nrows=MAX_ROWS)
print(f"✓ Loaded {len(df)} rows from {DATA_FILE}")

# Step 2: Data Preprocessing
print("\n[2/7] Preprocessing data...")
# Select only required columns
df = df[['review', 'recommended']].copy()

# Remove missing values
df.dropna(inplace=True)
print(f"✓ Dataset shape after cleaning: {df.shape}")

# Check class distribution
print(f"\nClass Distribution:")
print(f"  Recommended: {df['recommended'].sum()} ({df['recommended'].mean()*100:.2f}%)")
print(f"  Not Recommended: {(~df['recommended']).sum()} ({(~df['recommended']).mean()*100:.2f}%)")

# Step 3: Split Dataset
print("\n[3/7] Splitting dataset into train and test sets (80/20)...")
X = df['review']
y = df['recommended']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=TEST_SIZE, 
    random_state=RANDOM_STATE,
    stratify=y
)
print(f"✓ Training set: {len(X_train)} samples")
print(f"✓ Testing set: {len(X_test)} samples")

# Step 4: Text Vectorization using TF-IDF
print(f"\n[4/7] Vectorizing text using TF-IDF (max_features={MAX_FEATURES})...")
vectorizer = TfidfVectorizer(
    max_features=MAX_FEATURES,
    stop_words='english',
    lowercase=True,
    ngram_range=(1, 2)  # Use unigrams and bigrams
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
print(f"✓ Vectorization complete. Shape: {X_train_tfidf.shape}")

# Step 5: Train Logistic Regression Model
print("\n[5/7] Training Logistic Regression model...")
model = LogisticRegression(
    max_iter=1000,
    random_state=RANDOM_STATE,
    C=1.0,
    solver='lbfgs',
    n_jobs=-1  # Use all CPU cores
)
model.fit(X_train_tfidf, y_train)
print("✓ Model training complete!")

# Step 6: Model Evaluation
print("\n[6/7] Evaluating model performance...")
y_pred_train = model.predict(X_train_tfidf)
y_pred_test = model.predict(X_test_tfidf)

train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f"\n{'='*70}")
print("MODEL PERFORMANCE")
print(f"{'='*70}")
print(f"Training Accuracy: {train_accuracy*100:.2f}%")
print(f"Testing Accuracy:  {test_accuracy*100:.2f}%")
print(f"{'='*70}")

print("\nDetailed Classification Report (Test Set):")
print("-" * 70)
print(classification_report(y_test, y_pred_test, 
                          target_names=['Not Recommended', 'Recommended'],
                          digits=4))

# Step 7: Save Model and Vectorizer
print("[7/7] Saving model and vectorizer...")
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✓ Model saved as 'model.pkl'")

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("✓ Vectorizer saved as 'vectorizer.pkl'")

print("\n" + "=" * 70)
print("✓ TRAINING COMPLETE - Model is ready for deployment!")
print("=" * 70)

# Test with sample predictions
print("\n" + "=" * 70)
print("SAMPLE PREDICTIONS")
print("=" * 70)

sample_reviews = [
    "This game is absolutely amazing! Best game I've ever played.",
    "Terrible game, waste of money. Do not buy this.",
    "Pretty good game, had fun playing it with friends."
]

for i, review in enumerate(sample_reviews, 1):
    review_tfidf = vectorizer.transform([review])
    prediction = model.predict(review_tfidf)[0]
    confidence = model.predict_proba(review_tfidf)[0]
    recommendation = "Recommended" if prediction else "Not Recommended"
    conf_percentage = max(confidence) * 100
    
    print(f"\nSample {i}:")
    print(f"  Review: {review}")
    print(f"  Prediction: {recommendation}")
    print(f"  Confidence: {conf_percentage:.2f}%")

print("\n" + "=" * 70)
