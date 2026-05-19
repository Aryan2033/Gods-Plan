from fastapi import FastAPI

app = FastAPI() #create an instance of the FastAPI class, which will be our web application.

@app.get("/") # means when browser sends a GET request to the root URL ("/"), the following function will be executed.

async def root() -> dict[str, str]:
    return {"message": "running async server", "status": "ok"} #fastapi will automatically convert this dictionary to JSON and send it as a response to the client.

#now dynamic endpoint that takes a parameter and returns it in the response.

@app.get("/greet")

async def greet(name: str) -> dict[str, str]:
    return {
        "message" : f"hello {name}"
    }