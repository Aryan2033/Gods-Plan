from fastapi import FastAPI, BackgroundTasks
import time


def process_image(image_id):
    print(f"Processing image {image_id}...")
    time.sleep(10)  # Simulate a time-consuming task
    print(f"Finished processing image {image_id}.")


app = FastAPI()


@app.post("/scan")
async def scan(
    image_id: int,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(process_image, image_id)

    return {
        "status": "accepted",
    }

#what happened here is that we have created a FastAPI application with a single endpoint "/scan". When a POST request is made to this endpoint with an image_id, the process_image function is added to the background tasks. This allows the server to immediately respond with a status of "accepted" while the image processing continues in the background without blocking the main thread.