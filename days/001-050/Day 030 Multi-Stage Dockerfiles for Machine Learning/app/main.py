from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from app.models.industrial_vision import IndustrialVisionClassifier


MODEL_PATH = Path("artifacts/model.joblib")

model = IndustrialVisionClassifier()


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Loading ML model...")

    model.load_model(MODEL_PATH)

    print("ML model loaded successfully.")

    yield

    print("Application shutting down...")


app = FastAPI(
    title="Industrial Vision API",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "message": "Industrial Vision API is running"
    }


@app.get("/predict")
async def predict():

    sample = [[
        5.1,
        3.5,
        1.4,
        0.2
    ]]

    prediction = model.predict(sample)

    return {
        "prediction": int(prediction[0])
    }