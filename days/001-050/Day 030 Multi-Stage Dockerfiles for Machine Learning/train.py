from pathlib import Path
from sklearn.datasets import load_iris

from app.models.industrial_vision import IndustrialVisionClassifier

def main():
    data = load_iris()

    X = data.data
    y = data.target

    #what data and target are is that they are the features and labels of the iris dataset, respectively. The features are the measurements of the iris flowers, and the labels are the species of the iris flowers.

    model = IndustrialVisionClassifier()

    print("Training the model...")

    model.train(X,y)

    artifact_path = Path("artifacts/model.joblib")
    model.save_model(artifact_path)
    print(f"Model saved to {artifact_path}")

if __name__ == "__main__":
    main()