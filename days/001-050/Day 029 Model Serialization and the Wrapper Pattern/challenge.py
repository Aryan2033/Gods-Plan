import os
import joblib
from pathlib import Path
from abc import ABC, abstractmethod
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 1. The Abstract Contract (From Day 13)
class BaseMLModel(ABC):
    @abstractmethod
    def train(self, X, y) -> None:
        pass

    @abstractmethod
    def predict(self, X) -> np.ndarray:
        pass

# 2. The Concrete Production Wrapper
class IndustrialQualityModel(BaseMLModel):
    def __init__(self, model_name: str = "rf_quality_v1"):
        self.model_name = model_name
        self.model = RandomForestClassifier(n_estimators=10, random_state=42)
        
        # Professional Path Handling (From Day 9)
        self.artifact_dir = Path("data/artifacts")
        self.artifact_dir.mkdir(parents=True, exist_ok=True)
        self.model_path = self.artifact_dir / f"{self.model_name}.joblib"
        self.is_loaded = False

    def train(self, X, y) -> None:
        print(f"[{self.model_name}] Training started on {len(X)} samples...")
        self.model.fit(X, y)
        self.is_loaded = True
        print(f"[{self.model_name}] Training complete.")

    def predict(self, X) -> np.ndarray:
        if not self.is_loaded:
            raise RuntimeError(f"Model '{self.model_name}' is not loaded into memory.")
        return self.model.predict(X)

    def save_model(self) -> None:
        """Serializes the trained model object to the hard drive."""
        if not self.is_loaded:
            raise ValueError("Cannot save an untrained model.")
        joblib.dump(self.model, self.model_path)
        print(f"[{self.model_name}] Model serialized and saved to {self.model_path}")

    def load_model(self) -> None:
        """Deserializes the model artifact from the hard drive into RAM."""
        if not self.model_path.exists():
            raise FileNotFoundError(f"No serialized artifact found at {self.model_path}")
        self.model = joblib.load(self.model_path)
        self.is_loaded = True
        print(f"[{self.model_name}] Weights successfully loaded into RAM.")

# --- Execution Simulation ---
if __name__ == "__main__":
    # Simulate some factory sensor data (Features: Vibration, Temp, Pressure)
    mock_X = np.random.rand(100, 3)
    # Simulate binary labels (0 = Normal, 1 = Anomaly)
    mock_y = np.random.randint(0, 2, 100)

    print("--- PHASE 1: Training & Serialization ---")
    trainer = IndustrialQualityModel()
    trainer.train(mock_X, mock_y)
    trainer.save_model()  # This creates the .joblib file

    print("\n--- PHASE 2: Deserialization & Inference (Simulating Server Boot) ---")
    # We create a NEW instance, simulating starting a web server
    api_engine = IndustrialQualityModel()
    
    # Notice we do NOT call .train() here! We just load the artifact.
    api_engine.load_model()
    
    # Test inference on a new "sensor reading"
    new_sensor_reading = np.array([[0.5, 0.6, 0.1]])
    prediction = api_engine.predict(new_sensor_reading)
    print(f"Prediction for new reading: {'Anomaly' if prediction[0] == 1 else 'Normal'}")