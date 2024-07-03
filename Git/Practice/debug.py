import os
from dotenv import load_dotenv, dotenv_values

# Print current working directory
print("Current working directory:", os.getcwd())

# Print contents of the current directory
print("Directory contents:", os.listdir(os.getcwd()))

# Attempt to load the .env file
load_dotenv()

# Check if .env file exists and can be read
env_file_path = ".env"
if os.path.exists(env_file_path) and os.access(env_file_path, os.R_OK):
    print(f"{env_file_path} exists and is readable.")
else:
    print(f"{env_file_path} does not exist or is not readable.")

# Load the .env file into a dictionary
config = dotenv_values(".env")
print("dotenv_values output:", config)

# Access the environment variable using os.getenv
secret_key = os.getenv("MY_SECRET_KEY")
print(f"MY_SECRET_KEY from os.getenv: {secret_key}")
