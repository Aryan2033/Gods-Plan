from fastapi import FastAPI, BackgroundTasks, HTTPException
import time
import uuid

app = FastAPI(title="Ostalb Asynchronous ML Gateway")

# A mock database to store job statuses (In production, use Redis or PostgreSQL)
job_database = {}

# 1. The Heavy ML Function (Runs in the background)

def run_heavy_industrial_scan(job_id: str, sensor_data: list):
   
    print(f"[BACKGROUND] Starting job {job_id}...")

    time.sleep(10) 
    
    # Calculate dummy result
    anomaly_score = sum(sensor_data) / len(sensor_data)
    
    # Update the database when finished
    job_database[job_id] = {
        "status": "COMPLETED",
        "result": {"anomaly_score": round(anomaly_score, 4)}
    }
    print(f"[BACKGROUND] Job {job_id} finished successfully.")

@app.post("/api/v1/scan/async")

async def submit_scan_job(sensor_data: list[float], background_tasks: BackgroundTasks):
   
    if not sensor_data:
        raise HTTPException(status_code=400, detail="No sensor data provided.")

    # Generate a unique tracking ID
    job_id = str(uuid.uuid4())
    
    # Register the job as "PENDING"
    job_database[job_id] = {"status": "PENDING", "result": None}
    
    # Hand the heavy function to FastAPI's background worker
    background_tasks.add_task(run_heavy_industrial_scan, job_id, sensor_data)
    
    # Return immediately (User does not wait 10 seconds)

    return {
        "message": "Job accepted and is processing in the background.",
        "job_id": job_id,
        "check_status_url": f"/api/v1/scan/status/{job_id}"
    }

# 3. The Polling Endpoint (User checks this to get their result)

@app.get("/api/v1/scan/status/{job_id}")

async def check_job_status(job_id: str):
   
    job = job_database.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job ID not found.")
    
    return {"job_id": job_id, "current_status": job["status"], "data": job["result"]}