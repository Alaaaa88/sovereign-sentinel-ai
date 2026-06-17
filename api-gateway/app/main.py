import subprocess
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# استيراد عقل الذكاء الاصطناعي من الملف الذي رأيته في الصورة
from api_gateway.app.ai_brain import SovereignAIBrain 

app = FastAPI(title="Sovereign Sentinel AI - Production Control Plane")

ai_brain = SovereignAIBrain()

class CodePayload(BaseModel):
    file_name: str
    source_code: str

@app.post("/api/v1/analyze")
async def analyze_code(payload: CodePayload):
    # المسار الفعلي للمحرك بناءً على شجرة المجلدات لديك
    binary_path = "/workspaces/sovereign-sentinel-ai/core-engine/build/sentinel_core"
    
    try:
        # تشغيل المحرك الأمني
        process = subprocess.run(
            [binary_path], 
            input=payload.source_code, 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # تحليل النتائج
        findings = json.loads(process.stdout)
        
        # دمج ذكاء الـ AI في التقرير
        return {
            "file": payload.file_name,
            "status": "analyzed",
            "findings": findings,
            "ai_summary": ai_brain.summarize(findings) # افتراض وجود دالة التلخيص
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Engine Failure: {str(e)}")