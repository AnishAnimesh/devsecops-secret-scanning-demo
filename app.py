AWS_ACCESS_KEY_ID = "REMOVED"
AWS_SECRET_ACCESS_KEY = "REMOVED"

import os

def connect_to_cloud():
    api_key = os.getenv("CLOUD_API_KEY")
    if not api_key:
        print("No API key found")
        return
    print("Connecting securely...")

connect_to_cloud()