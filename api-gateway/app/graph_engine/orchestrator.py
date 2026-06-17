from parser import CodeParser
from db_connector import GraphConnector

# ربط العقل الأمني بذاكرة Neo4j
class OracleEngine:
    def __init__(self):
        self.parser = CodeParser()
        self.db = GraphConnector("bolt://localhost:7687", "neo4j", "your_password")

    def ingest_code(self, source_code):
        tree = self.parser.parse_code(source_code.encode())
        # هنا سيتم استخراج الدوال وتحويلها لعقد في الرسم البياني
        self.db.create_node("Function", {"name": "main", "risk": "low"})
        print("تمت عملية التحليل والتخزين بنجاح في Graph Database")

if __name__ == "__main__":
    engine = OracleEngine()
    engine.ingest_code("int main() { return 0; }")
