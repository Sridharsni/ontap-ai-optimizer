# AI-Powered Cloud Storage Optimization System

This project demonstrates how to build an **AI-driven cloud storage optimization platform** that integrates **ONTAP** (mocked via FastAPI), Kubernetes, and a D3.js dashboard for real-time monitoring.

---

## Overview

- **AI-Driven Predictive Algorithms**: Uses Python (and optionally C++) to forecast storage demands and expand volumes accordingly.  
- **Kubernetes Orchestration**: Ensures automated workload balancing, high availability, and fault tolerance.  
- **Real-Time Dashboards**: D3.js for visualizing volume usage; can be extended with Grafana.  
- **ONTAP & AWS Lambda**: Simulated ONTAP with FastAPI, plus a Lambda-style trigger script for automated expansion logic.

---

## Key Features

1. **AI Predictive Model**  
   - `ai_model/train_model.py` trains a model to predict future usage.
   - The system can automatically expand volumes when usage crosses thresholds.

2. **Mock ONTAP API**  
   - Located in `ontap_api/mock_ontap_api.py`.
   - Provides routes like `/api/storage/volumes` for volume details.
   - Supports volume expansion via a `PATCH` route.

3. **Kubernetes Deployment**  
   - `kubernetes/api-deployment.yaml` & `kubernetes/dashboard-deployment.yaml` define how containers are deployed in K8s.
   - Exposes services via **NodePort** for local testing.

4. **D3.js Dashboard**  
   - `dashboard/index.html` fetches volume data from the mock ONTAP API.
   - Displays bar charts of usage (in GB), color-coded by threshold.

5. **Docker Containers**  
   - `docker/Dockerfile.api`: Builds the FastAPI-based mock ONTAP service.  
   - `docker/Dockerfile.dashboard`: Builds a simple static server for `index.html`.

6. **Lambda-style Trigger**  
   - `lambda_functions/trigger_expand.py` simulates usage events and calls the ONTAP API to expand volumes automatically.

---

## Architecture Diagram (Optional)
        ┌────────────────┐
        │ D3.js Dashboard│
        │ (dashboard/)   │
        └───────▲────────┘
                │
      NodePort   │   NodePort
                │
        ┌───────┴─────────┐
        │ Docker + K8s     │
        │ (ontap-dashboard)│
        └────────┬─────────┘
                 │
                 │
        ┌────────┴─────────┐
        │ Mock ONTAP API    │
        │ (FastAPI)         │
        └────────┬──────────┘
                 │
                 ▼
   [ AI Model + Lambda Trigger ]
            (Python/C++)

---

## Getting Started

### 1. Clone the Repository & Install Requirements
```bash
git clone https://github.com/your-username/ontap-ai-optimizer.git
cd ontap-ai-optimizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Run the Mock ONTAP API & Dashboard Locally (Optional)
API:
uvicorn ontap_api.mock_ontap_api:app --reload --port 8000
Dashboard:
python3 -m http.server 8080
Open:

http://localhost:8000/api/storage/volumes for the API
http://localhost:8080/index.html for the D3.js dashboard
Docker & Kubernetes

A. Build Docker Images
docker build -t youruser/ontap-api:latest -f docker/Dockerfile.api .
docker build -t youruser/ontap-dashboard:latest -f docker/Dockerfile.dashboard .
B. Push to Docker Hub (optional)
docker push youruser/ontap-api:latest
docker push youruser/ontap-dashboard:latest
C. Deploy to Kubernetes
kubectl apply -f kubernetes/api-deployment.yaml
kubectl apply -f kubernetes/dashboard-deployment.yaml
Check:

kubectl get pods
kubectl get services
Access the NodePort for each service to view your API and dashboard.

Usage

AI Model: Under ai_model/train_model.py, a sample approach to train or simulate usage predictions.
Trigger Script: lambda_functions/trigger_expand.py can simulate spikes and trigger expansions on the mock ONTAP API.
Dashboard: Real-time bar charts for volume usage in dashboard/index.html.
Kubernetes: Orchestrates containers for reliability, optionally scaled out with more replicas.
Future Enhancements

Integrate a real ONTAP simulator or NetApp Trident driver for actual storage volumes.
Grafana integration for advanced metrics and alerting.
Autoscaling your pods with a Horizontal Pod Autoscaler (HPA).
Complete the AI logic in Python or C++ for truly predictive volume expansions.
License

This project is licensed under the MIT License.
