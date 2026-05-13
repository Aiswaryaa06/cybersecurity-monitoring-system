import matplotlib.pyplot as plt

def failed_login_chart(logs):
    failed = logs[logs["status"] == "FAILED"]

    counts = failed["country"].value_counts()

    counts.plot(kind="bar")

    plt.title("Failed Logins by Country")

    plt.xlabel("Country")
    plt.ylabel("Attempts")

    plt.savefig("charts/failed_logins.png")

    plt.show()