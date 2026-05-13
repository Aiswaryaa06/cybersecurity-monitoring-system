from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

def generate_logs(n=200):
    logs = []

    for _ in range(n):
        logs.append({
            "timestamp": datetime.now() - timedelta(minutes=random.randint(0, 5000)),
            "user": fake.user_name(),
            "ip": fake.ipv4(),
            "action": random.choice(["login_success", "login_failed"]),
            "location": fake.city(),
        })

    return pd.DataFrame(logs)