from tensorflow.keras.models import load_model
import numpy as np
from app.models.user import User
import logging

# Load trained model
logging.basicConfig(level=logging.DEBUG)


# Function to encode gender as a number (Example: Male = 0, Female = 1, Other = 2)
def encode_gender(gender):
    gender_map = {"male": 0, "female": 1, "other": 2}
    return gender_map.get(gender.lower(), -1)  # Default to -1 if unknown

def recommend_videos(username, category_id, db):
    logging.debug(f"Fetching user: {username}")

    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        logging.debug("User not found in database.")
        return {"error": "User not found"}
    
    logging.debug(f"User found: {user.username}")

    # Convert user ID and category ID to input
    user_id = user.id  # User ID from database
    category_id = int(category_id)  # Convert category to integer


    model_input = np.array([[user_id, category_id]], dtype=np.int32)  # Shape: (1,2)

    # Load model and predict
    model = load_model("D:/VideoRecom/video-recommendation-assignment/scripts/recommendation_model.h5")
    prediction = model.predict(model_input)

    return {"recommendations": prediction.tolist()}

def select_top_videos(prediction_scores, db):
    """
    Selects the top recommended videos based on model predictions.

    Args:
        prediction_scores (numpy.ndarray): Model's output scores.
        db (object): Database connection.

    Returns:
        list: List of recommended video details.
    """
    # Fetch available videos from the database
    all_videos = db.get_all_videos()  # Modify based on your DB structure

    # Sort videos by predicted scores
    sorted_videos = sorted(all_videos, key=lambda x: prediction_scores[0][x["id"]], reverse=True)

    # Return the top 5 recommended videos
    return sorted_videos[:5]
