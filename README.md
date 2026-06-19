🛡️ GuardianIQ – NIDS Project

📌 Overview
GuardianIQ is a Network Intrusion Detection System (NIDS) built using Suricata and a Streamlit dashboard. It detects and visualizes suspicious network activity in real time.

⚙️ Features
ICMP ping detection
SSH access monitoring
Port scan detection
Live Suricata log analysis
SOC-style dashboard (Streamlit)
🏗️ Architecture

Network Traffic → Suricata IDS → fast.log → Streamlit Dashboard

📁 Structure
GuardianIQ/
├── app.py
├── rules/guardianiq.rules
├── README.md
└── docs/
🚀 Run
sudo suricata -i ens33
sudo streamlit run app.py
🛠️ Tech Stack
Suricata IDS
Python
Streamlit
Linux
