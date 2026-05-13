from app.log_reader import load_logs

logs = load_logs()

print(logs)

from app.log_reader import load_logs
from app.detector import detect_failed_logins

logs = load_logs()

alerts = detect_failed_logins(logs)

print("Suspicious IPs:")
print(alerts)

from app.alert_system import save_alerts

save_alerts(alerts)

from app.reporting import generate_report

generate_report(logs)