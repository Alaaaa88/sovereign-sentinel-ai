import os
import json
import argparse

def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)["rules"]

def scan(target_dir):
    rules = load_rules()
    results = []
    summary = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    total_risk_score = 0
    files_scanned = 0
    severity_points = {"CRITICAL": 40, "HIGH": 25, "MEDIUM": 10, "LOW": 5}
    
    extensions = ('.cpp', '.c', '.py', '.js', '.ts', '.java', '.go')

    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(extensions):
                files_scanned += 1
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding='utf-8') as f:
                        content = f.read()
                    
                    for rule in rules:
                        if rule["pattern"] in content:
                            results.append({
                                "file": path,
                                "severity": rule["severity"],
                                "description": rule["description"],
                                "cwe": rule.get("cwe", "N/A"),
                                "recommendation": rule.get("recommendation", "No specific recommendation.")
                            })
                            summary[rule["severity"]] += 1
                            total_risk_score += severity_points.get(rule["severity"], 0)
                except Exception as e:
                    print(f"Error scanning {path}: {e}")
    
    report = {
        "metadata": {"files_scanned": files_scanned, "engine": "Sovereign Sentinel v1.0"},
        "summary": summary,
        "risk_score": total_risk_score,
        "findings": results
    }
    
    with open("security_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print(f"Scan complete. Found {len(results)} issues. Risk Score: {total_risk_score}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sovereign Sentinel Security Scanner")
    parser.add_argument("path", help="Project directory to scan")
    args = parser.parse_args()
    scan(args.path)

