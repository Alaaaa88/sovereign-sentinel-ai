from fastapi import FastAPI
from pydantic import BaseModel
from .security_scanner import SecurityScanner

app = FastAPI()
scanner = SecurityScanner()

# نحدد هيكل البيانات (Data Schema) ليعرف النظام ماذا يستقبل
class CodeRequest(BaseModel):
    source_code: str

@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    # المنصة الآن ستقرأ الكود من "source_code" مباشرة
    result = scanner.analyze(request.source_code)
    return {"status": "success", "analysis": result}