from sqlalchemy import create_engine

DATABASE_URL = "postgresql://myuser:mypassword@localhost:1234/video_recommendation"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
