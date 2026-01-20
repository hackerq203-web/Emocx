
import requests, json, random, string, uuid, re
import pyfiglet, threading, itertools, time, sys
from colorama import Fore, Style, init
init(autoreset=True)
B = Style.BRIGHT
logo = pyfiglet.figlet_format("BERKE", font="slant")
print(Fore.MAGENTA + B + logo)
print(Fore.YELLOW + B + "     ╔════════════════════════════╗")
print(Fore.YELLOW + B + f"     ║  @Bulsunlar | @BerkePython  ║")
print(Fore.YELLOW + B + "     ╚════════════════════════════╝\n")
use = input(Fore.CYAN + B + "🎯 Hedef TikTok Kullanıcı Adı → " + Style.RESET_ALL)
try:
    adet = int(input(Fore.GREEN + B + "🚀 Kaç takipçi yollayalım? → " + Style.RESET_ALL))
    if adet < 1:
        print(Fore.RED + B + "→ En az 1 takipçi girmelisin kanka...")
        sys.exit()
except:
    print(Fore.RED + B + "→ Sayı yazsana aq sayı!!")
    sys.exit()
def get_token():
    url = "https://www.ttboost.app/api/login"
    device_name = ''.join(random.choices(string.digits, k=8)) + ''.join(random.choices(string.ascii_uppercase, k=2))
    android_id = uuid.uuid4().hex[:16]
    username = ''.join(random.choices(string.ascii_lowercase, k=5)) + str(random.randint(11,99))
    
    payload = {
        "device_name": device_name,
        "id": android_id,
        "referral": None,
        "username": username
    }
    
    headers = {
        'User-Agent': "ktor-client",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'hash': "f3306e1b14321996320eaca84b2250fa7a8506f92e29274e67125b1f81b45726",
        'accept-charset': "UTF-8"
    }
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.json()['data']['token']

def get_profile_image(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip"
    }
    
    r = requests.get(url, headers=headers)
    m = re.search(r'https:\\u002F\\u002F[^\s"]+:100:100\.jpeg[^\s"]*', r.text)
    
    if m:
        return m.group(0).replace("\\u002F", "/")
    else:
        print(Fore.RED + B + "❌ Profil resmi çekilemedi! Kullanıcı adı doğru mu?")
        sys.exit()

def loading_animation(stop_event):
    animation = itertools.cycle(['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'])
    for c in animation:
        if stop_event.is_set():
            break
        sys.stdout.write(Fore.YELLOW + B + f'\r[BERKE] Takipçiler uçuyor... {c} ')
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write('\r' + ' ' * 60 + '\r')

def send_follower(username, image, index, total):
    try:
        token = get_token()
        url = "https://www.ttboost.app/api/orders"
        
        payload = {
            "image": image,
            "url": f"https://www.tiktok.com/@{username}/",
            "username": username,
            "product_id": 27,
            "purchase_token": None
        }
        
        headers = {
            'User-Agent': "ktor-client",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'authorization': f"Bearer {token}",
            'accept-charset': "UTF-8"
        }
        
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        res = r.json()
        
        if res.get("success"):
            print(Fore.CYAN + B + f"  [{index}/{total}] » Takipçi başarıyla yollandı! 🔥")
        else:
            print(Fore.RED + B + f"  [{index}/{total}] » Hata: {res.get('error_code', 'Bilinmeyen hata')}")         
    except Exception as e:
        print(Fore.RED + B + f"  [{index}/{total}] » İstek patladı: {str(e)}")

print(Fore.BLUE + B + "\n" + "═" * 55)
print(Fore.BLUE + B + f"   Hedef → @{use}  |  Gönderim → {adet} takipçi")
print(Fore.BLUE + B + "═" * 55 + "\n")
image = get_profile_image(use)
stop_event = threading.Event()
loader = threading.Thread(target=loading_animation, args=(stop_event,))
loader.start()
threads = []
for i in range(1, adet + 1):
    t = threading.Thread(target=send_follower, args=(use, image, i, adet))
    threads.append(t)
    t.start()
    time.sleep(0.18 + random.uniform(0, 0.12))
for t in threads:
    t.join()
stop_event.set()
loader.join()
print("\n" + Fore.GREEN + B + "╔════════════════════════════════════════════╗")
print(Fore.GREEN + B + "║   İşlem tamamlandı! Berke onayladı 🚀     ║")
print(Fore.GREEN + B + "╚════════════════════════════════════════════╝")
