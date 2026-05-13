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

<img width="347" height="354" alt="image" src="https://github.com/user-attachments/assets/c01cd06f-af7b-4639-811d-0c40382ff30e" />



📸 Dashboard Preview
<img width="1915" height="924" alt="image" src="https://github.com/user-attachments/assets/bac4b326-e42c-489c-a198-70e6efc1f2cd" />
<img width="1090" height="831" alt="image" src="https://github.com/user-attachments/assets/682d0c19-3d0d-4071-92bb-b1f4d89a59d7" />
<img width="1218" height="673" alt="image" src="https://github.com/user-attachments/assets/9b8c37af-4152-4e00-b396-eb994c7f695a" />
<img width="1315" height="686" alt="image" src="https://github.com/user-attachments/assets/af7998df-3ff9-4308-8a48-6c7c610af46a" />
<img width="1157" height="744" alt="image" src="https://github.com/user-attachments/assets/670a3347-47f7-4efd-adf1-1a48c10287d3" />
<img width="1062" height="517" alt="image" src="https://github.com/user-attachments/assets/6e6a9e17-72c9-493f-b563-bcbc41d45293" />








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





