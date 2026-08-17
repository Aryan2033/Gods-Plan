from fastapi import FastAPI, Depends

app = FastAPI()

async def get_model():

    return "model"


app.get("/predict")

async def predict(
    model=Depends(get_model)
):
    
    return {"message": f"Using {model} for prediction"}

