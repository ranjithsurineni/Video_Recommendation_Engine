# Video Recommendation Engine

## 📌 Project Overview

The **Video Recommendation Engine** is a deep-learning-based system designed to provide personalized video recommendations based on user interactions. This project uses **FastAPI**, **TensorFlow**, and **PostgreSQL** to build an end-to-end recommendation system that processes user data, trains a model, and serves recommendations through an API.

---

## 🏗️ Project Structure

```
video-recommendation-engine/
│── app/
│   │── models/                 # Database models
│   │   ├── user.py
│   │   ├── video.py
│   │── routers/                # API route handlers
│   │   ├── recommendation.py   # Main recommendation API
│   │── services/               # Core recommendation logic
│   │   ├── model.py            # Deep learning model
│   │   ├── preprocess.py       # Data preprocessing functions
│   │── database.py             # Database connection
│   │── main.py                 # FastAPI entry point
│── scripts/                    # Jupyter notebooks / scripts
│   ├── data_extraction.ipynb   # Fetching data from API
│   ├── train_model.ipynb       # Training the ML model
│   ├── test_model.ipynb        # Testing & evaluation
│── migrations/                 # Database migrations (Alembic)
│── .env                        # Environment variables
│── requirements.txt            # Dependencies
│── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Setup Database

- Ensure **PostgreSQL** is running on `localhost:5432`.
- Configure your `.env` file:
  ```env
  DATABASE_URL=postgresql://username:password@localhost:5432/video_recommendation
  ```
- Apply migrations:
  ```bash
  alembic upgrade head
  ```

### 3️⃣ Train the Model

Run the **Jupyter notebook** for training:

```bash
jupyter notebook scripts/train_model.ipynb
```

This will:
✅ Load user interaction data\
✅ Train a deep learning model using TensorFlow\
✅ Save the trained model to `recommendation_model.h5`

### 4️⃣ Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 Features Implemented

### 🔹 Data Preprocessing (`app/services/preprocess.py`)

- Extracts user data from `user_data.csv`
- Converts JSON columns into structured data
- Normalizes and prepares data for training

### 🔹 Model Training (`scripts/train_model.ipynb`)

- Builds a **deep learning model** using **TensorFlow**
- Uses **Embedding Layers** to capture video-user relationships
- Trains on user engagement data
- Saves the trained model to `recommendation_model.h5`

### 🔹 API Development (`app/routers/recommendation.py`)

- `/recommend` - Returns personalized video recommendations

### 🔹 Model Inference (`app/services/model.py`)

- Loads `recommendation_model.h5`
- Accepts user input and predicts recommended videos

---

## 📡 API Endpoints

### 1️⃣ **Root Endpoint**

```bash
GET /
```

📌 Returns:

```json
{"message": "Welcome to the Video Recommendation API"}
```

### 2️⃣ **Video Recommendation API**

```bash
POST /recommend
```

📌 Request Body:

```json
{
  "username": "user123"
}
```

📌 Response:

```json
{
  "message": "Recommended videos for user123"
}
```

---

## ⚠️ Troubleshooting

### 🔴 PostgreSQL Connection Error

**Error:** `OperationalError: Connection refused (0x0000274D/10061)`

✅ Fix:

- Ensure **PostgreSQL** is running on `localhost:5432`.
- Run: `sudo service postgresql start`

### 🔴 JSONDecodeError in `user_data.csv`

**Error:** `Expecting property name enclosed in double quotes`

✅ Fix:

- Ensure all JSON data in `user_data.csv` is **properly formatted**.
- Use `json.dumps(data)` before saving JSON fields.

---

## 🎯 Next Steps

🔹 Improve the recommendation model using **Collaborative Filtering**\
🔹 Deploy the API using **Docker & AWS**\
🔹 Implement a **React.js frontend** for video recommendations

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to submit **issues** or **pull requests** to improve the recommendation engine. 🚀

