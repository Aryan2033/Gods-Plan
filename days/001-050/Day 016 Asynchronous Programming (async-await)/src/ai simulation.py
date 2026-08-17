import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")

async def predict(text:str) -> dict[str, str]:
    embedding = await create_embedding(text)
    result = await vector_search(embedding)
    answer = await llm_response(result)
    return {
        "answer" : answer
    }

