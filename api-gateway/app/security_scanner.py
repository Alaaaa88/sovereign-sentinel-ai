class SecurityScanner:
    def __init__(self):
        self.rules = [
            {"name": "Buffer Overflow", "patterns": ["gets", "strcpy"], "severity": "Critical", "fix": "استخدم fgets"},
            {"name": "SQL Injection", "patterns": ["SELECT", "userInput"], "severity": "High", "fix": "استخدم Prepared Statements"},
            {"name": "Hardcoded Secrets", "patterns": ["password", "admin123"], "severity": "High", "fix": "استخدم .env"}
        ]

    def analyze(self, source_code: str):
        findings = []
        lines = source_code.splitlines()
        for i, line in enumerate(lines, 1):
            for rule in self.rules:
                for pattern in rule["patterns"]:
                    if pattern in line:
                        findings.append({
                            "issue": rule["name"],
                            "severity": rule["severity"],
                            "line": i,
                            "explanation": f"تم اكتشاف {rule['name']} في السطر {i}",
                            "fix": rule["fix"]
                        })
        return findings
