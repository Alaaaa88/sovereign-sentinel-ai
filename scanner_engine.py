import sys
import json

def scan_file(file_path):
    vulnerabilities = []
    with open(file_path, 'r') as f:
        content = f.read()
        if "strcpy" in content:
            vulnerabilities.append({
                "ruleId": "CWE-120",
                "message": "Potential buffer overflow detected",
                "file": file_path
            })
    return vulnerabilities

if __name__ == "__main__":
    target = sys.argv[1]
    vulns = scan_file(target)
    
    # حفظ النتائج في ملف تقرير
    with open("security_report.json", "w") as f:
        json.dump(vulns, f, indent=4)
        
    if vulns:
        sys.exit(1)
    sys.exit(0)
