from flask import Flask, jsonify
import logging
import time
import os

app = Flask(__name__)

os.makedirs('/tmp/flask-logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('/tmp/flask-logs/app.log')
    ]
)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info("Home endpoint hit")
    return jsonify({"status": "ok", "message": "AI RCA System - Demo App"})

@app.route('/metrics')
def metrics():
    return """# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",endpoint="/"} 100
# HELP app_errors_total Total errors
# TYPE app_errors_total counter
app_errors_total 0
""", 200, {'Content-Type': 'text/plain'}

@app.route('/cause-error')
def cause_error():
    logger.error("Simulated error: NullPointerException in payment_handler.py line 47")
    logger.error("Stack trace: payment_service -> process_payment -> validate_card -> None")
    return jsonify({"status": "error", "message": "Simulated error triggered"}), 500

@app.route('/stress')
def stress():
    logger.warning("High memory usage detected: 87% of limit")
    logger.warning("Request queue building up - latency increasing")
    time.sleep(0.5)
    return jsonify({"status": "stressed", "latency_ms": 500})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)