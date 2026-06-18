import subprocess
import os
import json

def test_vulnerability_detection_and_report():
    # تشغيل الماسح
    result = subprocess.run(['python3', 'scanner_engine.py', 'samples/vulnerable.cpp'], capture_output=True, text=True)
    
    # التأكد من اكتشاف الثغرة
    assert result.returncode == 1
    assert os.path.exists("security_report.json")
    
    # التأكد من صحة محتوى التقرير
    with open("security_report.json", 'r') as f:
        data = json.load(f)
        assert data[0]["ruleId"] == "CWE-120"
