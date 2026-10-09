import re
# Regular expression pattern to match "WARNING" or "ERROR"
pattern = r"(WARNING|ERROR)"
# Path to the log file
log_file_path = "/var/log/messages"
# Open the log file and read its contents
with open(log_file_path, "r") as log_file:
    for line in log_file:
        # Search for lines containing "WARNING" or "ERROR"
        if re.search(pattern, line):
            print(line.strip())  # Print the matching line without leading/trailing whitespace  
            