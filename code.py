#!/usr/bin/env python3
"""
Discord 3-Character Username Checker
"""

import requests
import string
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

TOKEN = "YOUR_TOKEN_HERE"
CHARSET = string.ascii_lowercase + string.digits
MAX_WORKERS = 15
OUTPUT_DOLU = "dolu.txt"
OUTPUT_BOS = "bos.txt"

HEADERS = {
    "Authorization": TOKEN,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def generate_all():
    for c1 in CHARSET:
        for c2 in CHARSET:
            for c3 in CHARSET:
                yield f"{c1}{c2}{c3}"

def check(username):
    try:
        r = requests.get(
            f"https://discord.com/api/v9/users/{username}",
            headers=HEADERS,
            timeout=5
        )
        return username, r.status_code == 404  # True = boş, False = dolu
    except:
        return username, False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[*] Discord 3-Char Username Checker")
    print("[*] D = Dolu | B = Boş\n")

    bos = []
    dolu = []
    checked = 0
    start = time.time()

    all_usernames = list(generate_all())
    total = len(all_usernames)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(check, u): u for u in all_usernames}
        
        for f in as_completed(futures):
            checked += 1
            username, is_bos = f.result()
            
            if is_bos:
                bos.append(username)
                print(f"[B] {username}", flush=True)
            else:
                dolu.append(username)
            
            if checked % 100 == 0:
                pct = (checked / total) * 100
                print(f"\r[ ] {checked}/{total} | D: {len(dolu)} | B: {len(bos)} ({pct:.1f}%)", end="", flush=True)

    sure = time.time() - start
    print("\n\n" + "="*50)
    print(f"[✓] Toplam: {checked}")
    print(f"[✓] Dolu (D): {len(dolu)}")
    print(f"[✓] Boş  (B): {len(bos)}")
    print(f"[✓] Süre: {sure:.1f}s")

    with open(OUTPUT_DOLU, "w") as f:
        f.write("\n".join(dolu))
    print(f"[✓] Dolu olanlar -> {OUTPUT_DOLU}")

    with open(OUTPUT_BOS, "w") as f:
        f.write("\n".join(bos))
    print(f"[✓] Boş olanlar -> {OUTPUT_BOS}")

if __name__ == "__main__":
    if TOKEN == "YOUR_TOKEN_HERE":
        TOKEN = input("[>] Token: ").strip()
        HEADERS["Authorization"] = TOKEN
    main()
