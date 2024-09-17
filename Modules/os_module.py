import os

# Get the current working directory

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# list the files and directories
files = os.listdir(".")
print(f"Files in the current directory: {files}")