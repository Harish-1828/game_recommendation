"""
Steam Game Store - Complete Gaming Platform
Features: Game grid, search, detailed views, recommendations, and ML-powered reviews
"""

from flask import Flask, render_template, request, jsonify
import pickle
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
from games_data import get_all_games, get_game_by_id, search_games, get_all_genres

app = Flask(__name__)

# Load trained model and vectorizer
print("Loading ML model and vectorizer...")
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print("✓ Model and vectorizer loaded successfully!")
except FileNotFoundError:
    print("WARNING: Model files not found. Some features will be limited.")
    model = None
    vectorizer = None

# Load review data
try:
    reviews_df = pd.read_csv("steam_reviews.csv", nrows=10000)
    print(f"✓ Loaded {len(reviews_df)} reviews")
except:
    reviews_df = None
    print("WARNING: Could not load reviews data")

@app.route("/")
def home():
    """Main page with game grid"""
    games = get_all_games()
    genres = get_all_genres()
    return render_template("index.html", games=games, genres=genres)

@app.route("/search")
def search():
    """Search for games"""
    query = request.args.get("q", "").strip()
    if query:
        games = search_games(query)
    else:
        games = get_all_games()
    genres = get_all_genres()
    return render_template("index.html", games=games, genres=genres, search_query=query)

@app.route("/game/<int:game_id>")
def game_detail(game_id):
    """Game detail page with visualizations"""
    game = get_game_by_id(game_id)
    if not game:
        return render_template("error.html", message="Game not found"), 404
    
    # Generate rating trend data (simulated over 12 months)
    months = []
    ratings = []
    base_rating = game["rating"]
    
    for i in range(12, 0, -1):
        date = datetime.now() - timedelta(days=i*30)
        months.append(date.strftime("%b %Y"))
        # Simulate rating trend with some variance
        variance = np.random.randint(-3, 4)
        ratings.append(min(100, max(60, base_rating + variance)))
    
    # Generate review distribution data
    review_distribution = {
        "Positive": int(base_rating),
        "Negative": int(100 - base_rating)
    }
    
    # Generate playtime distribution (hours)
    playtime_ranges = ["0-5h", "5-10h", "10-20h", "20-50h", "50-100h", "100h+"]
    playtime_data = [15, 20, 25, 23, 12, 5]  # percentages
    
    chart_data = {
        "rating_trend": {
            "months": months,
            "ratings": ratings
        },
        "review_distribution": review_distribution,
        "playtime": {
            "ranges": playtime_ranges,
            "data": playtime_data
        }
    }
    
    return render_template("game_detail.html", game=game, chart_data=json.dumps(chart_data))

@app.route("/recommend")
def recommend_page():
    """Recommendation questionnaire page"""
    genres = get_all_genres()
    return render_template("recommend.html", genres=genres)

@app.route("/get_recommendations", methods=["POST"])
def get_recommendations():
    """Process user preferences and recommend games"""
    data = request.form
    
    preferred_genre = data.get("genre", "").strip()
    min_rating = int(data.get("min_rating", 0))
    max_price = float(data.get("max_price", 10000))  # Max price in INR
    preferred_tags = data.get("tags", "").split(",")
    preferred_tags = [tag.strip().lower() for tag in preferred_tags if tag.strip()]
    
    # Get all games
    all_games = get_all_games()
    
    # Filter games based on preferences
    recommended = []
    for game in all_games:
        # Check genre
        if preferred_genre and preferred_genre != "Any" and game["genre"] != preferred_genre:
            continue
        
        # Check rating
        if game["rating"] < min_rating:
            continue
        
        # Check price
        if game["price"] > max_price:
            continue
        
        # Calculate match score based on tags
        match_score = 0
        if preferred_tags:
            game_tags_lower = [tag.lower() for tag in game["tags"]]
            matching_tags = sum(1 for tag in preferred_tags if tag in game_tags_lower)
            match_score = matching_tags
        
        recommended.append({
            **game,
            "match_score": match_score
        })
    
    # Sort by rating and match score
    recommended.sort(key=lambda x: (x["match_score"], x["rating"]), reverse=True)
    
    # Get top 6 recommendations
    recommended = recommended[:6]
    
    return render_template("recommendations.html", 
                         games=recommended, 
                         preferences=data)

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    """Save user feedback to dataset"""
    try:
        data = request.json
        game_id = data.get("game_id")
        liked = data.get("liked")
        review_text = data.get("review", "")
        
        game = get_game_by_id(game_id)
        if not game:
            return jsonify({"success": False, "error": "Game not found"})
        
        # Append to CSV file
        feedback_data = {
            "timestamp": datetime.now().isoformat(),
            "game_id": game_id,
            "game_name": game["name"],
            "liked": liked,
            "review": review_text,
            "recommended": liked
        }
        
        # Append to feedback file
        feedback_file = "user_feedback.csv"
        df = pd.DataFrame([feedback_data])
        
        if os.path.exists(feedback_file):
            df.to_csv(feedback_file, mode='a', header=False, index=False)
        else:
            df.to_csv(feedback_file, mode='w', header=True, index=False)
        
        return jsonify({"success": True, "message": "Thank you for your feedback!"})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/analyze_review", methods=["POST"])
def analyze_review():
    """Analyze if a review is positive or negative using ML model"""
    try:
        if not model or not vectorizer:
            return jsonify({
                "success": False,
                "error": "ML model not available"
            })
        
        data = request.json
        review_text = data.get("review", "").strip()
        
        if not review_text or len(review_text) < 10:
            return jsonify({
                "success": False,
                "error": "Review too short"
            })
        
        # Transform and predict
        review_vector = vectorizer.transform([review_text])
        prediction = model.predict(review_vector)[0]
        probabilities = model.predict_proba(review_vector)[0]
        
        is_positive = bool(prediction == 1)
        confidence = float(probabilities[1] if is_positive else probabilities[0]) * 100
        
        return jsonify({
            "success": True,
            "is_positive": is_positive,
            "confidence": round(confidence, 2),
            "sentiment": "Positive" if is_positive else "Negative"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🎮 STARTING STEAM GAME STORE")
    print("="*70)
    print("Application running at: http://127.0.0.1:5000/")
    print("Press CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)