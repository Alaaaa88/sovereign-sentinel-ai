import subprocess
import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from neo4j import GraphDatabase

app = FastAPI(
    title="Sovereign Sentinel AI - API Gateway",
    version="2.0.0",
    description="Real-time Production Interface with Live Neo4j Graph Database Integration"
)

# Real Production Credentials pointing to the local Docker container
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "AlaaSovereignPass2026"

class CodePayload(BaseModel):
    file_name: str
    source_code: str

def push_to_neo4j_live(file_name: str, findings: list):
    # Establish real driver connection
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        with driver.session() as session:
            # 1. Inject or update the target File node
            session.run(
                "MERGE (f:File {name: $file_name}) SET f.last_analyzed = datetime()", 
                file_name=file_name
            )
            
            # 2. Map vulnerabilities dynamically into the graph topology
            for finding in findings:
                session.run(
                    """
                    MERGE (v:Finding {entity_name: $entity})
                    SET v.category = $category,
                        v.line = $line,
                        v.type = $type,
                        v.vulnerable = $vulnerable
                    WITH v
                    MATCH (f:File {name: $file_name})
                    MERGE (f)-[:HAS_VULNERABILITY]->(v)
                    """,
                    file_name=file_name,
                    entity=finding.get("entity", "Unknown_Entity"),
                    category=finding.get("category", "Unknown"),
                    line=finding.get("line", 0),
                    type=finding.get("type", "Unknown"),
                    vulnerable=finding.get("vulnerable", False)
                )
    finally:
        driver.close()

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "engine_signature": "Alaa_Sovereign_Gateway_v2.0",
        "database_target": "Live_Docker_Neo4j"
    }

@app.post("/api/v1/analyze")
async def analyze_code(payload: CodePayload):
    binary_path = "/workspaces/sovereign-sentinel-ai/core-engine/build/sentinel_core"
    
    if not os.path.exists(binary_path):
        raise HTTPException(
            status_code=500, 
            detail="Core analyzer engine binary not found. Please compile the C++ source."
        )
        
    try:
        # Pipeline stream execution via stdin
        process = subprocess.run(
            [binary_path],
            input=payload.source_code,
            capture_output=True,
            text=True,
            check=True
        )
        
        raw_output = process.stdout.strip()
        parsed_json = json.loads(raw_output)
        findings = parsed_json.get("findings", [])
        
        # Live transaction commit to Neo4j
        push_to_neo4j_live(payload.file_name, findings)
        
        return {
            "success": True,
            "filename_processed": payload.file_name,
            "graph_sync": "committed_successfully",
            "metrics": parsed_json
        }
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Core engine runtime crash: {e.stderr}")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse clean JSON from C++ binary.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database or Pipeline Transaction Failed: {str(e)}")
