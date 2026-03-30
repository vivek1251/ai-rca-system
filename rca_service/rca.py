import requests
from datetime import datetime, timedelta
from flask import Flask, jsonify

app = Flask(__name__)

LOKI_URL = "http://loki:3100"
OLLAMA_URL = "http://host.docker.internal:11434"

def fetch_recent_logs(minutes=5):
    end = datetime.utcnow()
    start = end - timedelta(minutes=minutes)
    params = {
        "query": '{job="flask-app"}',
        "start": str(int(start.timestamp() * 1e9)),
        "end": str(int(end.timestamp() * 1e9)),
        "limit": 50
    }
    response = requests.get(f"{LOKI_URL}/loki/api/v1/query_range", params=params)
    data = response.json()
    logs = []
    for stream in data.get("data", {}).get("result", []):
        for entry in stream.get("values", []):
            logs.append(entry[1])
    return logs

def analyze_with_llm(logs):
    if not logs:
        return "No logs found in the last 5 minutes."
    filtered = [l for l in logs if "ERROR" in l or "WARNING" in l]
    if not filtered:
        return "No errors or warnings detected. System is healthy."
    log_text = "\n".join(filtered[:15])
    prompt = f"""Analyze these app logs briefly:
1. What errors occurred?
2. Root cause?
3. Fix?

LOGS:
{log_text}

Be concise."""
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "phi4-mini",
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": 200, "temperature": 0.1}
        },
        timeout=120
    )
    return response.json().get("response", "LLM analysis failed")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "AI RCA System"})

@app.route("/rca")
def rca():
    logs = fetch_recent_logs(minutes=5)
    errors = [l for l in logs if "ERROR" in l or "WARNING" in l]
    analysis = analyze_with_llm(logs)
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "logs_analyzed": len(logs),
        "errors_found": len(errors),
        "analysis": analysis
    })

@app.route("/rca/errors")
def rca_errors_only():
    logs = fetch_recent_logs(minutes=5)
    errors = [l for l in logs if "ERROR" in l or "WARNING" in l]
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "errors": errors
    })

if __name__ == "__main__":
    print("AI RCA Service running on http://0.0.0.0:8000")
    app.run(host="0.0.0.0", port=8000, debug=False)