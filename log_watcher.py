import time

log_file = "server.log"

print("🔎 Real-time log monitoring gestart...")

seen_lines = 0

while True:
    with open(log_file, "r") as file:
        lines = file.readlines()

    new_lines = lines[seen_lines:]

    for line in new_lines:
        if "ERROR" in line:
            print("🚨 ERROR gedetecteerd:", line.strip())
        elif "WARNING" in line:
            print("⚠️ WARNING:", line.strip())

    seen_lines = len(lines)

    time.sleep(5)

    ERROR Disk failure detected
WARNING Memory usage high