"""
Simple webhook-capable FastAPI module.

POST /predict?image_id=...&callback_url=...  -> accepts job and triggers background work
GET  /status?job_id=...                     -> returns job state

This file is intentionally self-contained and uses the standard library for outgoing
HTTP callbacks so no extra dependencies are required.
"""
from fastapi import FastAPI, BackgroundTasks, HTTPException
import time
import uuid
import json
import urllib.request
import urllib.error
from typing import Optional

app = FastAPI()

# In-memory job store for demo purposes. Replace with Redis/DB in production.
JOBS = {}


def _post_callback(callback_url: str, payload: dict, timeout: int = 10):
    """Send a JSON POST to the callback URL (best-effort)."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(callback_url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.getcode(), resp.read()


def heavy_task(job_id: str, image_id: int, callback_url: Optional[str] = None):
    """Simulate heavy work, update job state, and call the callback URL if provided."""
    JOBS[job_id]["status"] = "running"

    # Simulate long-running processing
    time.sleep(5)

    # Write result
    JOBS[job_id]["status"] = "completed"
    JOBS[job_id]["result"] = {"prediction": "ok", "image_id": image_id}

    # Call webhook if requested (best-effort)
    if callback_url:
        try:
            code, body = _post_callback(callback_url, {"job_id": job_id, "status": JOBS[job_id]["status"], "result": JOBS[job_id]["result"]})
            JOBS[job_id]["callback_response"] = {"code": code}
        except Exception as e:
            JOBS[job_id]["callback_error"] = str(e)


@app.post("/predict")
async def predict(background_tasks: BackgroundTasks, image_id: int, callback_url: Optional[str] = None):
    """Accept a job and optionally a callback URL to POST the result to when ready.

    - `image_id`: identifier for the input to process
    - `callback_url`: optional URL the server will POST to after completion
    """
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {"status": "queued", "image_id": image_id, "callback_url": callback_url}

    # Schedule the heavy work and pass the callback URL
    background_tasks.add_task(heavy_task, job_id, image_id, callback_url)

    return {"job_id": job_id, "status": "accepted"}


@app.get("/status")
def status(job_id: str):
    """Return the job status and available metadata."""
    j = JOBS.get(job_id)
    if not j:
        raise HTTPException(status_code=404, detail="job not found")
    return {"job_id": job_id, "status": j.get("status"), "result": j.get("result"), "callback_response": j.get("callback_response"), "callback_error": j.get("callback_error")}
