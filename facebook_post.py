import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
PAGE_ID = os.getenv("FB_PAGE_ID")

GRAPH_API_URL = f"https://graph.facebook.com/{PAGE_ID}/feed"

def post_to_facebook(message: str):
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    resp = requests.post(GRAPH_API_URL, data=payload)
    if resp.status_code == 200:
        print("✅ Post successful:", resp.json())
    else:
        print("❌ Error:", resp.status_code, resp.text)

if __name__ == "__main__":
    post_to_facebook("Hello Facebook! 🚀 Posted using Python + Graph API.")

