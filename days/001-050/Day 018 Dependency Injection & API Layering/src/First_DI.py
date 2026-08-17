from fastapi import FastAPI, Depends

app = FastAPI()


async def get_user():

    return "aryan"


@app.get("/home")

async def home(user=Depends(get_user)):# this is the dependency injection part, it allows us to inject the get_user function into the home function, so that we can use the user variable in the home function

    return {"message": f"Hello {user}"}

