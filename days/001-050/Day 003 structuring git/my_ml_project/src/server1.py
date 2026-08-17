from fastapi import FastAPI , Depends  , HTTPException, Header
from pydantic import BaseModel, Field
import time

app=FastAPI(title= "Ostalb Decoupled ML Engine Gateway")

#input schema

class ProductionPayload(BaseModel):

    batch_id :int = Field(..., description="Batch ID for the production data")

    sensor_reading : float = Field(...,ge=0.0, description="Sensor reading for inference")

#dependency

async def verify_hardware_handshake(
        
        x_client: str = Header(..., description = "industrial authorization header for hardware handshake")
):
    
    if x_client != "Aalen_Secure_Factory_99":

        raise HTTPException(
            status_code=401,
            detail="Unauthorized industrial cluster client node"    
        )
    
    return{
        "cluster_node":
        "Cluster_01_Baden_Württemberg",

        "status":"VERIFIED"
    }

#main route

@app.post("/api/v1/compute")

async def execute_batch_prediction(
    payload: ProductionPayload,
    hardware_info = Depends(verify_hardware_handshake)
):
    
    #simulate processing time
    

    return {
        "execution_status":"success",
        "batch_processed": payload.batch_id,
        "authorized_by_node": hardware_info["cluster_node"],
        "inference_result": {
            "scaled_telemetry": round(payload.sensor_reading * 1.5, 2),
            "timestamp": time.time()
        }
    }

