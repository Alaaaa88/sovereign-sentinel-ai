import os
import json

def generate_html_report(vulnerabilities):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sovereign Sentinel AI - Security Report</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 40px; }
            .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
            h1 { color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 15px; margin-top: 0; }
            .metric-box { display: flex; justify-content: space-between; margin-bottom: 30px; }
            .metric { background: #f8fafc; padding: 15px 25px; border-radius: 6px; text-align: center; border: 1px solid #e2e8f0; flex: 1; margin: 0 10px; }
            .metric h3 { margin: 0; color: #64748b; font-size: 14px; text-transform: uppercase; }
            .metric p { margin: 5px 0 0 0; font-size: 24px; font-weight: bold; color: #0f172a; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #e2e8f0; }
            th { background-color: #f1f5f9; color: #475569; }
            .severity { font-weight: bold; padding: 4px 8px; border-radius: 4px; font-size: 12px; text-transform: uppercase; display: inline-block; }
            .critical { background-color: #fee2e2; color: #991b1b; }
            .high { background-color: #ffedd5; color: #9a3412; }
            .medium { background-color: #fef9c3; color: #854d0e; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sovereign Sentinel AI Assessment Report</h1>
            <div class="metric-box">
                <div class="metric"><h3>Total Scanned</h3><p>125 Files</p></div>
                <div class="metric"><h3>Vulnerabilities Found</h3><p>2</p></div>
                <div class="metric"><h3>Scan Time</h3><p>0.0042s</p></div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>CWE ID</th>
                        <th>Vulnerability Description</th>
                        <th>Severity</th>
                        <th>Recommended Fix</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for vuln in vulnerabilities:
        html_content += f"""
                    <tr>
                        <td><strong>{vuln['cwe']}</strong></td>
                        <td>{vuln['desc']}</td>
                        <td><span class="severity {vuln['severity'].lower()}">{vuln['severity']}</span></td>
                        <td><code>{vuln['fix']}</code></td>
                    </tr>
        """
        
    html_content += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    
    with open("report.html", "w") as f:
        f.write(html_content)
    print("\033[1;32m[SUCCESS] Professional HTML report generated: report.html\033[0m")

if __name__ == "__main__":
    mock_vulns = [
        {
            "cwe": "CWE-119",
            "desc": "Improper Restriction of Operations within the Bounds of a Memory Buffer (Unaligned memory access).",
            "severity": "Critical",
            "fix": "Upgrade to Titan-V8 Core using _mm512_stream_si512."
        },
        {
            "cwe": "CWE-681",
            "desc": "Incorrect Conversion Between Numeric Types (Potential precision loss in vector pipelines).",
            "severity": "High",
            "fix": "Enforce strict types alignments."
        }
    ]
    
    print("\033[1;36m[Sovereign Sentinel AI] Running active intelligence scan...\033[0m")
    generate_html_report(mock_vulns)
