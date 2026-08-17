from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

import joblib
from sklearn.ensemble import RandomForestClassifier

class BaseModel(ABC):
    @abstractmethod
    def train(self,X,y):
        pass
    @abstractmethod
    def predict(self,X):
        pass

class IndustrialVisionClassifier(BaseModel):

    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, path: Union[str, Path]):
        path = Path(path)

        path.parent.mkdir(
        parents=True, 
        exist_ok=True
        ) 
        #what it does is it creates the parent directory if it doesn't exist, and it won't raise an error if the directory already exists.

        joblib.dump(self.model, path)

        #what it does is it saves the model to the specified path using joblib. The model can be loaded later using joblib.load(). what is dump? dump is a function in the joblib library that serializes an object and saves it to a file. In this case, it is used to save the trained model to the specified path so that it can be loaded later for predictions or further training.

    def load_model(self, path: Union[str, Path]):
        path = Path(path)

        #what it does is it loads the model from the specified path using joblib. The model can be used for predictions or further training after being loaded.

        if not path.exists():
            raise FileNotFoundError(f"Model file not found at {path}")

        self.model = joblib.load(path)
        


