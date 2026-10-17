import os

# current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# list all files and directories in the current working directory
files = os.listdir(".")
print(f"Files in the current working directory: {files}")