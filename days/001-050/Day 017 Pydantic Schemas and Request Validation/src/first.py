from pydantic import BaseModel, Field
from fastapi import FastAPI

app=FastAPI()

class User(BaseModel):
    name:str
    age: int = Field(..., ge=18, description="Age must be greater than or equal to 18")
    email:str

@app.post("/register")
async def register_user(user: User):
    return {"message": "successfully registered", "user": user}