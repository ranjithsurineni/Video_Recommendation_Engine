from fastapi import FastAPI
from app.routers import recommendation
from app.database import engine, Base
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(recommendation.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Video Recommendation API"}

@app.get("/favicon.ico")
async def favicon():
    return StaticFiles(directory="app/static").get_response("favicon.ico")

# Run the server using:
# uvicorn app.main:app --reload
