from fastapi import FastAPI
app = FastAPI()
@app.get("/")

async def root():
    return {
        "message": "Day 30 Docker API is running"
        }

