from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from .security_scanner import SecurityScanner

app = FastAPI()
scanner = SecurityScanner()

# تعريف هيكل النتائج
class Finding(BaseModel):
    issue: str
    severity: str
    line: int
    explanation: str
    recommended_fix: str

class AnalysisResponse(BaseModel):
    status: str
    security_score: int
    findings: List[Finding]

class CodeRequest(BaseModel):
    source_code: str

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_code(request: CodeRequest):
    results = scanner.analyze(request.source_code)
    # حساب تقييم أمني بسيط (مثال)
    score = 100 - (len(results) * 10)
    return {
        "status": "success",
        "security_score": max(0, score),
        "findings": results
    }