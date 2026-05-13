import pandas as pd

def load_logs():
    logs = pd.read_csv("data/logs.csv")
    return logs