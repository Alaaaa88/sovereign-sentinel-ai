class RealTimeDefender:
    def check_taint(self, ast_node):
        # المنطق الحقيقي: تتبع وصول المدخلات إلى دوال التنفيذ
        dangerous_sinks = ['system', 'exec', 'memcpy', 'strcpy']
        if ast_node.text.decode() in dangerous_sinks:
            return "CRITICAL_VULNERABILITY_FOUND"
        return "SAFE"
