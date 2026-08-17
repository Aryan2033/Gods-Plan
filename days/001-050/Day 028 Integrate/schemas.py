from datetime import datetime

from pydantic import BaseModel


class MachineCreate(BaseModel):
    name: str
    location: str
    owner_email: str | None = None


class MachineUpdate(BaseModel):
    name: str | None = None
    location: str | None = None
    owner_email: str | None = None
    is_active: bool | None = None


class MachineRead(MachineCreate):
    id: int
    is_active: bool
    created_at: datetime


class SensorReadingCreate(BaseModel):
    machine_id: int
    temperature: float
    humidity: float | None = None
    note: str | None = None


class SensorReadingRead(SensorReadingCreate):
    id: int
    created_at: datetime


class PredictionCreate(BaseModel):
    machine_id: int
    prediction: str
    confidence_score: float | None = None
    model_version: str | None = None
    latency_ms: int | None = None


class PredictionRead(PredictionCreate):
    id: int
    created_at: datetime
