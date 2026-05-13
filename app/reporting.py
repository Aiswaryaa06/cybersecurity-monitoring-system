def generate_report(logs):
    total_logins = len(logs)

    failed = len(logs[logs["status"] == "FAILED"])

    successful = len(logs[logs["status"] == "SUCCESS"])

    print("=== Security Report ===")
    print(f"Total Logins: {total_logins}")
    print(f"Failed Logins: {failed}")
    print(f"Successful Logins: {successful}")