import pandas as pd
import random
import time
from datetime import datetime, timedelta
import os

users = ["alice","bob","charlie","david","emma","frank","grace"]
ips = ["185.220.101.1","45.33.32.156","104.244.72.115","192.168.1.10"]
countries = ["US","India","Germany","Russia","Singapore"]

file_path = os.path.join("data", "logs.csv")
os.makedirs("data", exist_ok=True)

if not os.path.exists(file_path):
    pd.DataFrame(columns=["timestamp","username","ip_address","status","country"]).to_csv(file_path, index=False)

print("🚀 REAL attack simulator started...")

# 🔥 ATTACK STATE (THIS IS THE KEY FIX)
attack_ip = random.choice(ips)
attack_window_start = datetime.now()

while True:

    now = datetime.now()

    # 🔥 Every ~20 seconds trigger a BURST attack window
    if (now - attack_window_start).seconds > 20:
        attack_ip = random.choice(ips)
        attack_window_start = now

    # 🔥 40% chance we are in attack mode
    in_attack = random.random() < 0.4

    if in_attack:
        ip = attack_ip
        status = random.choices(["FAILED", "FAILED", "FAILED", "SUCCESS"], weights=[80, 10, 5, 5])[0]

        # 🔥 cluster timestamps slightly backward to create spike effect
        timestamp = now - timedelta(seconds=random.randint(0, 30))

    else:
        ip = random.choice(ips)
        status = random.choices(["SUCCESS", "FAILED"], weights=[85, 15])[0]

        timestamp = now - timedelta(minutes=random.randint(0, 120))

    new_log = {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "username": random.choice(users),
        "ip_address": ip,
        "status": status,
        "country": random.choice(countries)
    }

    df = pd.read_csv(file_path)
    df = pd.concat([df, pd.DataFrame([new_log])], ignore_index=True)
    df.to_csv(file_path, index=False)

    print("Added:", new_log)

    time.sleep(2)