import re
# # Regular expression pattern to match "WARNING" or "ERROR"
# pattern = r"(WARNING|ERROR)"
# # Path to the log file
# log_file_path = "/var/log/messages"
# # Open the log file and read its contents
# with open(log_file_path, "r") as log_file:
#     for line in log_file:
#         # Search for lines containing "WARNING" or "ERROR"
#         if re.search(pattern, line):
#             print(line.strip())  # Print the matching line without leading/trailing whitespace  
            
            
            
# Challang mode: 

log_lines = """
192.168.1.10 - - [10/Oct/2026:13:55:02 +0000] "GET /api/v1/health HTTP/1.1" 200 1234
10.0.0.5 - - [10/Oct/2026:13:55:04 +0000] "POST /api/v1/deploy HTTP/1.1" 500 452
192.168.1.22 - - [10/Oct/2026:13:55:08 +0000] "GET /favicon.ico HTTP/1.1" 404 509
"""

status_codes = re.findall(r'HTTP/\d\.\d"\s(\d{3})', log_lines)
print(status_codes)  # Output: ['200', '500', '404']