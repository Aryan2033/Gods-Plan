from fastapi import FastAPI, Depends

app = FastAPI()


async def get_user():

    return "aryan"


@app.get("/home")

async def home(user=Depends(get_user)):

    return {"message": f"Hello {user}"}

