from collections import defaultdict

# Step 1: Read the log file
with open("logfile.txt", "r") as file:
    logs = file.readlines()

#Create a dictionary to track failed login attempts
failed_attempts = defaultdict(int)

# Analyze the log lines
for line in logs:
    if "login failed" in line:
        # Extract the username (last word in the line)
        parts = line.strip().split(" ")
        username = parts[-1]
        failed_attempts[username] += 1

# Display suspicious users and write to report.txt
print("\n Suspicious Users Detected:\n")

with open("report.txt", "w", encoding="utf-8") as report:
    suspicious_found = False
    for user, count in failed_attempts.items():
        if count >= 3:
            suspicious_found = True
            result = f"  User '{user}' had {count} failed login attempts!\n"
            print(result.strip())
            report.write(result)
    if not suspicious_found:
        print(" No suspicious login activity detected.")
        report.write(" No suspicious login activity detected.\n")

