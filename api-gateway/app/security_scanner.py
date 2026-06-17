class SecurityScanner:
    def __init__(self):
        # هذه قائمة الدوال التي تجعل الكود "ملغوماً"
        self.dangerous_functions = ["system", "strcpy", "memcpy", "gets", "scanf"]

    def analyze(self, source_code: str):
        findings = []
        for func in self.dangerous_functions:
            if func in source_code:
                findings.append(f"تنبيه: تم اكتشاف دالة خطيرة [{func}] التي قد تؤدي لثغرات Buffer Overflow أو Injection.")
        
        if not findings:
            return "الكود يبدو سليماً من الناحية السطحية."
        return findings
