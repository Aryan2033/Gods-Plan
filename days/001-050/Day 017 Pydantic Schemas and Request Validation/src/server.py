from pydantic import BaseModel, Field
from fastapi import FastAPI

app=FastAPI()

class InferenceRequest(BaseModel):
    sensor_id: str = Field(..., description="Sensor ID for inference")

    temperature:float = Field(...,gt=-273.15, description="Temperature must be greater than absolute zero")

    confidence:float = Field(..., ge=0, le=1, description="Confidence must be between 0 and 1")

    feature1:float
    feature2:float
    feature3:float


@app.post("/predict")

async def predict(data:InferenceRequest):

    return {
        "sensor": data.sensor_id,
        "received_features": [
            data.feature1,
            data.feature2,
            data.feature3
        ],
        "confidence": data.confidence,
        "status": "valid input",
        "message": "Inference received successfully"
    }