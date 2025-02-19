from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.model import recommend_videos
import logging
from app.models.user import User

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)


@router.get("/recommendations/{username}")
def get_recommendations(username: str, db= Depends(get_db)):
    """
    API endpoint to get video recommendations for a user.

    Args:
        username (str): The username to fetch recommendations for.

    Returns:
        JSON: Recommended videos.
    """
    return recommend_videos(username, db)

@router.get("/feed")
def get_recommendations(username: str, category_id: int = None, db: Session = Depends(get_db)):
    logging.debug(f"Fetching user: {username}")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        logging.debug("User not found in database.")
        return {"error": "User not found"}

    # Call model recommendation function
    recommendations = recommend_videos(username, category_id, db)
    return {"recommendations": recommendations}