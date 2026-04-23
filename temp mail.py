import requests, json
from uuid import uuid4

h = {
    'User-Agent': "okhttp/4.11.0",
    'Content-Type': "application/json",
    'x-revenuecat-app-user-id': f"$RCAnonymousID:{uuid4().hex}"
}

email = requests.post("https://api.emailnator.com/api/email/generate", json={"ids": [3]}, headers=h).json()["email"]
print(f"📧 {email}")

input("⏎ Bas ve gelen kutunu gör...")

inbox = requests.post("https://api.emailnator.com/api/email/inbox", json={"email": email}, headers=h).json()
print(json.dumps(inbox, indent=2, ensure_ascii=False))