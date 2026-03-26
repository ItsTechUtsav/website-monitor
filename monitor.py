import requests
import time
from datetime import datetime

# List of services to monitor
services = [
    "https://google.com",
    "https://github.com",
    "https://youtube.com"
]

# Function to check service status
def check_service(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=3)
        end = time.time()

        response_time = round((end - start) * 1000)

        if response.status_code == 200:
            return f"✅ UP ({response_time} ms)"
        else:
            return f"⚠️ ISSUE (Status: {response.status_code})"

    except:
        return "❌ DOWN"


# Main monitoring function
def run_monitor():
    print("\n🔍 Checking services...\n")

    report = ""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report += f"--- Report at {timestamp} ---\n"

    for service in services:
        result = check_service(service)
        output = f"{service} → {result}"

        print(output)
        report += output + "\n"

    report += "\n"

    # Save report to file
    with open("report.txt", "a", encoding="utf-8") as file:
        file.write(report)

    print("\n📁 Report saved to report.txt")


# Run once
run_monitor()