# 🔍 AI-Powered Root Cause Analysis System

> Automatically detects application errors and generates AI-driven root cause analysis — no manual log reading required.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![LLM](https://img.shields.io/badge/LLM-Phi--4--mini-purple)
![License](https://img.shields.io/badge/license-MIT-green)

## 📸 Demo

### 🎬 Live Dashboard
![Grafana Dashboard](screenshots/grafana-dashboard.gif)

### 🤖 AI Root Cause Analysis API
![RCA Output](screenshots/rca-output.png)

### ✅ Health Check
![Health Check](screenshots/health-check.png)
## 🏗️ Architecture
```
Flask App ──► Promtail ──► Loki ──► RCA Service ──► Phi-4-mini (Ollama)
          ──► Prometheus ──► Grafana Dashboard        └──► REST API (/rca)
```

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Application | Flask (Python) |
| Log Collection | Promtail → Loki |
| Metrics | Prometheus |
| Visualization | Grafana |
| AI/LLM | Microsoft Phi-4-mini via Ollama |
| Infrastructure | Docker Compose |

## ✨ Key Features

- **Automated RCA** — AI analyzes logs and returns root cause + fix in seconds
- **Local LLM** — Phi-4-mini runs on-device, no API keys, no data leakage
- **Real-time dashboards** — Live log streaming and error highlighting in Grafana
- **REST API** — Trigger analysis via `GET /rca`, integrate into any workflow

## 🚀 Quick Start

**Prerequisites:** Docker Desktop, [Ollama](https://ollama.ai) with Phi-4-mini
```bash
# Pull the model
ollama pull phi4-mini

# Clone and run
git clone https://github.com/vivek1251/ai-rca-system.git
cd ai-rca-system
docker-compose up -d
```

## 🧪 Testing
```bash
# Simulate errors
curl http://localhost:5000/cause-error
curl http://localhost:5000/stress

# Get AI root cause analysis
curl http://localhost:8000/rca
```

## 📡 Endpoints

| URL | Purpose |
|-----|---------|
| `localhost:5000` | Flask demo app |
| `localhost:8000/rca` | AI root cause analysis |
| `localhost:8000/health` | Service health check |
| `localhost:9090` | Prometheus metrics |
| `localhost:3000` | Grafana (admin/admin) |