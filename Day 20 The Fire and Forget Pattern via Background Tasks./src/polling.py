from fastapi import FastAPI , BackgroundTasks
import time
import uuid

app = FastAPI()

jobs = {}

# ml function

def heavy_ml_task(job_id):

    jobs[job_id] = "Processing" # Update the job status to "Processing" and store it in the jobs dictionary 
    time.sleep(10)  # Simulate a time-consuming task

    jobs[job_id] = {
        "status": "Completed",
        "prediction": "ok" # Update the job status to "Completed" and store the prediction result in the jobs dictionary
    }

@app.post("/predict")

async def predict(background_tasks: BackgroundTasks):

    job_id = str(uuid.uuid4()) # Generate a unique job ID using the uuid library what uuid4() generates a random UUID (Universally Unique Identifier) which is a 128-bit value that is typically represented as a string of hexadecimal digits. This ensures that each job ID is unique and can be used to track the status of individual jobs.

    jobs[job_id] = "Queued" # Update the job status to "Queued" and store it in the jobs dictionary

    background_tasks.add_task(
        heavy_ml_task, 
        job_id) # Add the heavy_ml_task function to the background tasks, passing the generated job ID as an argument. This allows the task to be executed asynchronously without blocking the main thread.
    
    return {
        "job_id": job_id,
        "status": "accepted"
    }