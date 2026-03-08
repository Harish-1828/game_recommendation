"""
Genre Preference Prediction using KNN
Predicts user's preferred game genre based on questionnaire responses
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import pickle
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("GENRE PREFERENCE PREDICTION - KNN MODEL")
print("=" * 70)

# Step 1: Create Training Dataset
print("\n[1/6] Creating training dataset from user preference patterns...")

# Training data: Simulated user responses that lead to specific genres
# Features: [playtime_preference, multiplayer_preference, pace_preference, budget, story_importance]
# - playtime_preference: 1=Casual(<10h/week), 2=Moderate(10-20h), 3=Hardcore(>20h)
# - multiplayer_preference: 1=Solo only, 2=Mixed, 3=Multiplayer focused
# - pace_preference: 1=Relaxed, 2=Balanced, 3=Fast-paced/Intense
# - budget: 1=Free/Cheap(<1000), 2=Mid(1000-3000), 3=Premium(>3000)
# - story_importance: 1=Don't care, 2=Nice to have, 3=Very important

training_data = []

# RPG patterns: High playtime, solo/mixed, balanced pace, premium, story-focused
for _ in range(30):
    training_data.append([
        np.random.choice([2, 3], p=[0.3, 0.7]),  # Moderate to Hardcore playtime
        np.random.choice([1, 2], p=[0.6, 0.4]),  # Solo or Mixed
        np.random.choice([1, 2], p=[0.5, 0.5]),  # Relaxed or Balanced
        np.random.choice([2, 3], p=[0.4, 0.6]),  # Mid to Premium
        np.random.choice([2, 3], p=[0.2, 0.8]),  # Story is important
        'RPG'
    ])

# Action patterns: Moderate playtime, mixed, fast-paced, premium, story moderate
for _ in range(25):
    training_data.append([
        np.random.choice([2, 3], p=[0.6, 0.4]),  # Moderate to Hardcore
        np.random.choice([1, 2], p=[0.7, 0.3]),  # Mostly solo
        np.random.choice([2, 3], p=[0.3, 0.7]),  # Balanced to Fast-paced
        np.random.choice([2, 3], p=[0.5, 0.5]),  # Mid to Premium
        np.random.choice([2, 3], p=[0.6, 0.4]),  # Story nice to have
        'Action'
    ])

# FPS patterns: Any playtime, multiplayer focused, fast-paced, free/cheap, story not important
for _ in range(25):
    training_data.append([
        np.random.choice([1, 2, 3], p=[0.3, 0.4, 0.3]),  # Any playtime
        np.random.choice([2, 3], p=[0.3, 0.7]),  # Mixed to Multiplayer
        np.random.choice([3], p=[1.0]),  # Fast-paced
        np.random.choice([1, 2], p=[0.7, 0.3]),  # Free to Mid
        np.random.choice([1, 2], p=[0.8, 0.2]),  # Story not important
        'FPS'
    ])

# Simulation patterns: Casual playtime, solo, relaxed, any budget, story moderate
for _ in range(20):
    training_data.append([
        np.random.choice([1, 2], p=[0.6, 0.4]),  # Casual to Moderate
        np.random.choice([1, 2], p=[0.8, 0.2]),  # Solo mostly
        np.random.choice([1], p=[1.0]),  # Relaxed
        np.random.choice([1, 2, 3], p=[0.4, 0.3, 0.3]),  # Any budget
        np.random.choice([1, 2], p=[0.5, 0.5]),  # Story mixed
        'Simulation'
    ])

# Strategy patterns: Moderate/hardcore, solo, balanced, mid budget, story moderate
for _ in range(15):
    training_data.append([
        np.random.choice([2, 3], p=[0.5, 0.5]),  # Moderate to Hardcore
        np.random.choice([1, 2], p=[0.7, 0.3]),  # Solo mostly
        np.random.choice([1, 2], p=[0.5, 0.5]),  # Relaxed to Balanced
        np.random.choice([2, 3], p=[0.6, 0.4]),  # Mid to Premium
        np.random.choice([1, 2], p=[0.6, 0.4]),  # Story not critical
        'Strategy'
    ])

# Adventure patterns: Moderate playtime, solo, balanced, mid budget, story important
for _ in range(15):
    training_data.append([
        np.random.choice([2], p=[1.0]),  # Moderate
        np.random.choice([1, 2], p=[0.8, 0.2]),  # Solo mostly
        np.random.choice([1, 2], p=[0.6, 0.4]),  # Relaxed to Balanced
        np.random.choice([2, 3], p=[0.5, 0.5]),  # Mid to Premium
        np.random.choice([2, 3], p=[0.4, 0.6]),  # Story important
        'Adventure'
    ])

# Horror patterns: Casual to moderate, solo, balanced, mid budget, story important
for _ in range(10):
    training_data.append([
        np.random.choice([1, 2], p=[0.5, 0.5]),  # Casual to Moderate
        np.random.choice([1], p=[1.0]),  # Solo
        np.random.choice([2], p=[1.0]),  # Balanced
        np.random.choice([2, 3], p=[0.6, 0.4]),  # Mid to Premium
        np.random.choice([2, 3], p=[0.5, 0.5]),  # Story important
        'Horror'
    ])

# Racing patterns: Casual, mixed, fast-paced, mid budget, story not important
for _ in range(10):
    training_data.append([
        np.random.choice([1, 2], p=[0.7, 0.3]),  # Casual to Moderate
        np.random.choice([2, 3], p=[0.5, 0.5]),  # Mixed to Multiplayer
        np.random.choice([3], p=[1.0]),  # Fast-paced
        np.random.choice([1, 2], p=[0.5, 0.5]),  # Cheap to Mid
        np.random.choice([1], p=[1.0]),  # Story not important
        'Racing'
    ])

df = pd.DataFrame(training_data, columns=[
    'playtime_preference', 'multiplayer_preference', 'pace_preference', 
    'budget', 'story_importance', 'genre'
])

print(f"✓ Created {len(df)} training samples")
print(f"\nGenre Distribution:")
print(df['genre'].value_counts().to_string())

# Step 2: Prepare Features and Labels
print("\n[2/6] Preparing features and labels...")
X = df[['playtime_preference', 'multiplayer_preference', 'pace_preference', 
        'budget', 'story_importance']].values
y = df['genre'].values

print(f"✓ Feature shape: {X.shape}")
print(f"✓ Unique genres: {len(np.unique(y))}")

# Step 3: Split Dataset
print("\n[3/6] Splitting dataset (80/20)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✓ Training set: {len(X_train)} samples")
print(f"✓ Testing set: {len(X_test)} samples")

# Step 4: Feature Scaling
print("\n[4/6] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ Feature scaling complete")

# Step 5: Train KNN Model
print("\n[5/6] Training KNN model...")

# Find optimal K using cross-validation
print("Finding optimal K value...")
k_values = range(3, 16, 2)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k, weights='distance', metric='euclidean')
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())
    print(f"  K={k}: CV Accuracy = {scores.mean():.4f}")

optimal_k = k_values[np.argmax(cv_scores)]
print(f"\n✓ Optimal K value: {optimal_k}")

# Train final model with optimal K
model = KNeighborsClassifier(n_neighbors=optimal_k, weights='distance', metric='euclidean')
model.fit(X_train_scaled, y_train)
print("✓ Model training complete!")

# Step 6: Evaluate Model
print("\n[6/6] Evaluating model performance...")
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

train_accuracy = accuracy_score(y_train, y_pred_train)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f"\n{'='*70}")
print("MODEL PERFORMANCE")
print(f"{'='*70}")
print(f"Training Accuracy: {train_accuracy*100:.2f}%")
print(f"Testing Accuracy:  {test_accuracy*100:.2f}%")
print(f"Optimal K:         {optimal_k}")
print(f"{'='*70}")

print("\nDetailed Classification Report (Test Set):")
print("-" * 70)
print(classification_report(y_test, y_pred_test, digits=4))

# Save Model and Scaler
print("\nSaving model and scaler...")
with open('genre_knn_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✓ Model saved as 'genre_knn_model.pkl'")

with open('genre_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("✓ Scaler saved as 'genre_scaler.pkl'")

print("\n" + "=" * 70)
print("✓ TRAINING COMPLETE - Model is ready for genre prediction!")
print("=" * 70)

# Test with sample predictions
print("\n" + "=" * 70)
print("SAMPLE PREDICTIONS")
print("=" * 70)

test_users = [
    {
        'name': 'Hardcore RPG Fan',
        'features': [3, 1, 2, 3, 3]  # Hardcore, Solo, Balanced, Premium, Story Important
    },
    {
        'name': 'Competitive FPS Player',
        'features': [2, 3, 3, 1, 1]  # Moderate, Multiplayer, Fast, Free, No Story
    },
    {
        'name': 'Casual Gamer',
        'features': [1, 1, 1, 1, 2]  # Casual, Solo, Relaxed, Cheap, Some Story
    },
    {
        'name': 'Action Lover',
        'features': [3, 2, 3, 3, 2]  # Hardcore, Mixed, Fast, Premium, Some Story
    }
]

for user in test_users:
    features = np.array([user['features']])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    confidence = max(probabilities) * 100
    
    print(f"\n{user['name']}:")
    print(f"  Answers: Playtime={user['features'][0]}, Multiplayer={user['features'][1]}, "
          f"Pace={user['features'][2]}, Budget={user['features'][3]}, Story={user['features'][4]}")
    print(f"  Predicted Genre: {prediction}")
    print(f"  Confidence: {confidence:.2f}%")

print("\n" + "=" * 70)
print("USAGE INSTRUCTIONS:")
print("=" * 70)
print("""
Feature Encoding Guide:
1. Playtime Preference:     1=Casual(<10h/week), 2=Moderate(10-20h), 3=Hardcore(>20h)
2. Multiplayer Preference:  1=Solo only, 2=Mixed, 3=Multiplayer focused
3. Pace Preference:         1=Relaxed, 2=Balanced, 3=Fast-paced/Intense
4. Budget:                  1=Free/Cheap(<₹1000), 2=Mid(₹1000-3000), 3=Premium(>₹3000)
5. Story Importance:        1=Don't care, 2=Nice to have, 3=Very important

Example:
    features = [3, 1, 2, 3, 3]  # Hardcore solo RPG player
    features_scaled = scaler.transform([features])
    genre = model.predict(features_scaled)[0]
""")
print("=" * 70)
