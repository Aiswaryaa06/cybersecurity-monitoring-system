🕵️ Cybersecurity Monitoring System (SOC Dashboard)


## 🚨 Project Overview

The **Cybersecurity Monitoring System** is a SOC-style (Security Operations Center) simulation dashboard built using **Python and Streamlit**.

It simulates real-world login activity, detects suspicious behavior, identifies brute-force attacks, assigns risk scores, and visualizes cybersecurity threats in real time.

This project demonstrates how raw logs can be transformed into **actionable security intelligence**.

---

## 🎯 Key Features

### 🔐 Log Monitoring
- Simulated login logs (SUCCESS / FAILED)
- Username, IP address, timestamp tracking

### 🚨 Threat Detection
- Brute-force attack detection
- Suspicious user identification
- IP-based anomaly detection

### 🧠 Risk Scoring Engine
- Failed login → High risk score
- Successful login → Low risk score
- Severity classification (LOW / MEDIUM / HIGH)

### 📊 Visual Analytics
- Login success vs failure charts
- Attack timeline (burst detection)
- Top attacking IPs
- Geo heatmap of attack origins

### 🧾 Incident Management
- Automatic incident logging
- Downloadable reports (CSV export)

### 🔴 Live Simulation
- Real-time log feed simulation
- Time-based attack progression
- SOC-style monitoring behavior

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming |
| Streamlit | Web dashboard UI |
| Pandas | Data processing |
| Plotly | Data visualization |
| Faker | Fake log generation |

📊 Detection Logic
🚨 Brute Force Detection
A user is flagged if:
Failed login attempts ≥ 3

🌐 IP Anomaly Detection
Multiple failed logins from same IP
High frequency login attempts

⏱ Attack Burst Detection
Logs grouped into time windows
Rolling analysis detects spikes in failed logins

monitoring-system/
│
├── app/
│   ├── dashboard.py
│   ├── data_generator.py
│
├── detector.py
├── data/
│   ├── logs.csv
│   ├── incidents.csv
│
├── requirements.txt
├── README.md

📸 Dashboard Preview




🧠 Key Learnings
SOC (Security Operations Center) fundamentals
Log-based anomaly detection
Time-series analysis for cybersecurity
Real-time dashboard design using Streamlit
Risk scoring systems in security monitoring

🚀 Future Improvements
🔴 Machine Learning anomaly detection (Isolation Forest)
🌍 Real IP geolocation API integration
⚡ Kafka-based real-time streaming logs
🧾 Database integration (PostgreSQL)
🔐 User authentication system
📡 Live attack simulation engine
👨‍💻 Author

Aiswaryaa Ramesh
Cybersecurity & Data Analytics Project
Built for learning SOC systems and log monitoring pipelines.





