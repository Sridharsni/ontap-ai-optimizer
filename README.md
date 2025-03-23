# ONTAP AI Optimizer

A cloud-based intelligent storage optimization system that integrates a FastAPI backend, AI-powered volume expansion logic, and a D3.js dashboard to visualize ONTAP storage volumes in real time.

---

## 📌 Overview

This project demonstrates how predictive algorithms and visual insights can help manage and scale ONTAP volumes efficiently. It simulates real-world ONTAP behavior through mock APIs and offers a dashboard to monitor volume size trends.

### 🔧 Key Components
- **FastAPI server** exposing mock ONTAP APIs
- **Lambda-style function** to auto-expand volumes based on usage
- **D3.js dashboard** for real-time visualization

---

## 🗂 Project Structure

ontap-ai-optimizer/ ├── ai_model/ │ ├── model.pkl │ ├── storage_data.csv │ └── train_model.py ├── dashboard/ │ └── index.html ├── docker/ │ └── Dockerfile ├── kubernetes/ │ └── pod_balancer.py ├── lambda_functions/ │ └── trigger_expand.py ├── ontap_api/ │ ├── mock_ontap_api.py │ └── ontap_client.py ├── requirements.txt └── README.md


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sridharsni/ontap-ai-optimizer.git
cd ontap-ai-optimizer
2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Start the FastAPI Server
uvicorn ontap_api.mock_ontap_api:app --reload --port 8000
5. Serve the D3.js Dashboard
In a new terminal window:

python3 -m http.server 8080
Then open your browser and visit:

http://localhost:8080/dashboard/index.html
6. Run the Volume Expansion Trigger Script
python lambda_functions/trigger_expand.py
📊 Dashboard Preview

The dashboard displays ONTAP volume usage in a bar chart with the following color indicators:

Steelblue → Normal usage
Orange → Near threshold
Red → Critical (expansion triggered)
Each bar includes a label showing the volume size in GB.

🧰 Technologies Used

Python — Core language
FastAPI — API backend for ONTAP simulation
D3.js — Interactive frontend visualizations
Docker & Kubernetes — For containerization and orchestration (optional)
AWS Lambda-style Logic — For storage expansion simulation
🧠 AI-Powered Logic

The AI trigger script reads usage input and automatically expands volumes if usage exceeds a threshold (e.g., 80%). It interacts with the mock ONTAP API and simulates volume growth dynamically.

📝 Notes

.gitignore excludes virtual environments, cache files, and large binaries.
CORS is enabled to allow communication between the FastAPI server and the dashboard.
Avoid pushing large virtual environment files or ML binaries to GitHub.
📄 License

This project is open-source and available under the MIT License.

💡 Inspiration

This project was built to simulate intelligent cloud storage management, combining real-time insights and automation — perfect for infrastructure engineers, DevOps teams, or students exploring smart backend systems.
