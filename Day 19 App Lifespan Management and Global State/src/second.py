from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import time


class VisionModel:
    def predict(self, value):
        result = value * 2
        return result


@asynccontextmanager
async def lifespan(app):
    print("loading model..")
    time.sleep(3)

    app.state.model = VisionModel()

    print("model loaded")

    yield

    print("unloading model..")
    app.state.model = None

app = FastAPI(lifespan=lifespan) # what lifespan does is it allows us to run some code before the application starts and after the application stops. In this case, we are loading a model before the application starts and unloading it after the application stops.


@app.get("/predict")
async def predict(request: Request):
    model = request.app.state.model
    result = model.predict(5)

    return {
        "prediction": result
    }





    
