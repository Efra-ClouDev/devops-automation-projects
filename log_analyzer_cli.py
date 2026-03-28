import sys
import glob
from datetime import datetime

pattern = sys.argv[1]
output_file = sys.argv[2]

error_count = 0
warning_count = 0
info_count = 0

files = glob.glob(f"{pattern}*.log")

for log_file in files:
    print(f"Processing {log_file}")
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

with open(output_file, "w") as output:
    output.write(report)

if error_count > 0:
    print("🚨 ALERT: Errors gevonden in logs!")