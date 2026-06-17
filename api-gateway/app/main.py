import subprocess
import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Sovereign Sentinel AI - API Gateway",
    version="1.0.0",
    description="Control Plane Interface for High-Performance C++20 Core Analyzer Engine"
)

class CodePayload(BaseModel):
    file_name: str
    source_code: str

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "engine_signature": "Alaa_Sovereign_Gateway_v1.0"
    }

@app.post("/api/v1/analyze")
async def analyze_code(payload: CodePayload):
    binary_path = "/workspaces/sovereign-sentinel-ai/core-engine/build/sentinel_core"
    
    if not os.path.exists(binary_path):
        raise HTTPException(
            status_code=500, 
            detail="Core analyzer engine binary not found."
        )
        
    try:
        process = subprocess.run(
            [binary_path],
            input=payload.source_code,
            capture_output=True,
            text=True,
            check=True
        )
        
        raw_output = process.stdout.strip()
        parsed_json = json.loads(raw_output)
        
        return {
            "success": True,
            "filename_processed": payload.file_name,
            "metrics": parsed_json
        }
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Core engine crash: {e.stderr}")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse clean JSON from C++ binary.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
