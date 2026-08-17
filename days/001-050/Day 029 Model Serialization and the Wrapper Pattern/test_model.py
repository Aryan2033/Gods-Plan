from pathlib import Path

from app.models.industrial_vision import IndustrialVisionClassifier


def main():
    model = IndustrialVisionClassifier()

    model.load_model(
        Path("artifacts/model.joblib")
    )

    sample = [[
        5.1,
        3.5,
        1.4,
        0.2
    ]]

    prediction = model.predict(sample)

    print("Prediction:", prediction)


if __name__ == "__main__":
    main()