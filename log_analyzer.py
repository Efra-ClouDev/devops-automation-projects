from datetime import datetime

log_file = "server.log"

error_count = 0
warning_count = 0
info_count = 0

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

timestamp = datetime.now()

report = f"""
Log Rapport - {timestamp}

Errors: {error_count}
Warnings: {warning_count}
Info: {info_count}
"""

print(report)

with open("log_report.txt", "w") as output:
    output.write(report)

if error_count > 0:
    print("🚨 ALERT: Errors gevonden in logs!")