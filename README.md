# AI-Powered Root Cause Analysis System

An end-to-end DevOps observability platform that automatically analyzes application logs and generates AI-powered root cause analysis using a locally-hosted LLM.

## Architecture
```
Flask App → Promtail → Loki → RCA Service (Phi-4-mini) → REST API
         → Prometheus → Grafana Dashboard
```

## Stack
- **Flask** - Demo application with simulated errors
- **Loki + Promtail** - Log aggregation and collection
- **Prometheus** - Metrics scraping
- **Grafana** - Visualization dashboard
- **Phi-4-mini via Ollama** - Local LLM for RCA analysis
- **Docker Compose** - Container orchestration

## Quick Start
```bash
git clone https://github.com/vivek1251/ai-rca-system.git
cd ai-rca-system
docker-compose up -d
```

## Endpoints
| URL | Purpose |
|-----|---------|
| http://localhost:5000 | Flask demo app |
| http://localhost:8000/rca | AI root cause analysis API |
| http://localhost:9090 | Prometheus |
| http://localhost:3000 | Grafana (admin/admin) |