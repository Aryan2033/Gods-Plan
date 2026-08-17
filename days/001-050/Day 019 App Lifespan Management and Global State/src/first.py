from fastapi import FastAPI 
from contextlib import asynccontextmanager
import time

model = None

@asynccontextmanager
async def lifespan(app):

    global model

    print("loading model..")

    time.sleep(3)

    model = "vision_model_loaded"

    print("model loaded")

    yield

    print("unloading model..")
    model = None

app = FastAPI(lifespan=lifespan)
 
@app.get("/predict")
async def predict():
    return {
        "status": "success",
        "model": model
    }

# Why Not Use Global Variables?

# Bad:

# model=None

# Problems:

# difficult testing
# harder scaling
# poor structure
# hidden dependencies