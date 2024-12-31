import subprocess
import os

# Path to Brave browser executable
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Update if different

# URL to open
url = "https://youtube.com"

# Command to open Brave in private mode with the URL
subprocess.run([brave_path, "--incognito", url])
