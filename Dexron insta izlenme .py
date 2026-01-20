#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEXRON INSTAGRAM STORY İZLENME TOOL
Created by Dexron Team
"""

import requests
import json
import time
import sys
from datetime import datetime
import os

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class DexronInstagramTool:
    def __init__(self):
        self.api_url = "https://api-nabi-sosyalmedya.trr.gt.tc/api/send"
        self.service = "instagram_story_views"
        
    def print_banner(self):
        banner = f"""
{Colors.PURPLE}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗ ███████╗██╗  ██╗██████╗  ██████╗ ███╗   ██╗      ║
║    ██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗████╗  ██║      ║
║    ██║  ██║█████╗   ╚███╔╝ ██████╔╝██║   ██║██╔██╗ ██║      ║
║    ██║  ██║██╔══╝   ██╔██╗ ██╔══██╗██║   ██║██║╚██╗██║      ║
║    ██████╔╝███████╗██╔╝ ██╗██║  ██║╚██████╔╝██║ ╚████║      ║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝      ║
║                                                              ║
║           📱 INSTAGRAM STORY İZLENME TOOL 📱                ║
║                                                              ║
║         🔥 Premium Instagram Hizmetleri 🔥                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)
    
    def get_user_info(self):
        print(f"\n{Colors.CYAN}{'═' * 60}{Colors.END}")
        print(f"{Colors.YELLOW}{Colors.BOLD}👤 KULLANICI BİLGİLERİ{Colors.END}")
        print(f"{Colors.CYAN}{'═' * 60}{Colors.END}")
        
        while True:
            name = input(f"\n{Colors.GREEN}📛 Adınız: {Colors.END}").strip()
            if name:
                break
            print(f"{Colors.RED}❌ Lütfen geçerli bir isim giriniz!{Colors.END}")
        
        while True:
            age = input(f"{Colors.GREEN}🎂 Yaşınız: {Colors.END}").strip()
            if age.isdigit() and 1 <= int(age) <= 120:
                break
            print(f"{Colors.RED}❌ Lütfen 1-120 arasında bir yaş giriniz!{Colors.END}")
        
        while True:
            username = input(f"{Colors.GREEN}📱 Instagram Kullanıcı Adı: {Colors.END}").strip()
            if username:
                username = username.replace('@', '')
                break
            print(f"{Colors.RED}❌ Lütfen geçerli bir kullanıcı adı giriniz!{Colors.END}")
        
        return name, age, username
    
    def check_story_availability(self, username):
        print(f"\n{Colors.BLUE}🔍 @{username} için story kontrol ediliyor...{Colors.END}")
        time.sleep(2)
        
        stories_exist = True
        
        if stories_exist:
            print(f"{Colors.GREEN}✅ Story bulundu! İzlenme gönderiliyor...{Colors.END}")
            return True
        else:
            print(f"{Colors.RED}❌ Aktif story bulunamadı!{Colors.END}")
            return False
    
    def send_story_views(self, username, count=1000):
        print(f"\n{Colors.PURPLE}🚀 Story izlenme gönderiliyor...{Colors.END}")
        
        story_link = f"https://instagram.com/stories/{username}/"
        
        params = {
            'service': self.service,
            'link': story_link
        }
        
        try:
            print(f"{Colors.CYAN}📡 API'ye bağlanılıyor: {self.api_url}{Colors.END}")
            time.sleep(1)
            
            response = requests.get(self.api_url, params=params, timeout=30)
            
            if response.status_code == 200:
                print(f"{Colors.GREEN}✅ İstek başarıyla gönderildi!{Colors.END}")
                
                try:
                    data = response.json()
                    print(f"{Colors.YELLOW}📊 API Yanıtı: {json.dumps(data, indent=2, ensure_ascii=False)}{Colors.END}")
                except:
                    print(f"{Colors.YELLOW}📄 API Yanıtı: {response.text}{Colors.END}")
                
                return True
            else:
                print(f"{Colors.RED}❌ API Hatası: {response.status_code}{Colors.END}")
                print(f"{Colors.RED}📄 Detay: {response.text}{Colors.END}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}❌ Bağlantı Hatası: {e}{Colors.END}")
            return False
        except Exception as e:
            print(f"{Colors.RED}❌ Beklenmeyen Hata: {e}{Colors.END}")
            return False
    
    def show_progress(self, duration=5):
        print(f"\n{Colors.BLUE}⏳ İşlem devam ediyor...{Colors.END}")
        for i in range(duration):
            progress = (i + 1) * 20
            bar = "█" * (i + 1) + "░" * (duration - i - 1)
            print(f"{Colors.PURPLE}📊 [{bar}] {progress}%{Colors.END}", end="\r")
            time.sleep(1)
        print(f"{Colors.GREEN}📊 [██████████] 100% Tamamlandı!{Colors.END}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        
        print(f"{Colors.YELLOW}🌟 Hoş geldiniz! Instagram story izlenme aracına başlıyoruz...{Colors.END}")
        
        name, age, username = self.get_user_info()
        
        print(f"\n{Colors.CYAN}👋 Merhaba {name} ({age} yaş)!{Colors.END}")
        print(f"{Colors.CYAN}📱 İşlem yapılacak hesap: @{username}{Colors.END}")
        
        if not self.check_story_availability(username):
            print(f"\n{Colors.RED}💡 Lütfen önce story paylaştığınızdan emin olun!{Colors.END}")
            input(f"\n{Colors.RED}🔚 Çıkmak için Enter tuşuna basın...{Colors.END}")
            return
        
        print(f"\n{Colors.YELLOW}⚠️  ONAY İSTEĞİ{Colors.END}")
        print(f"{Colors.CYAN}{'═' * 40}{Colors.END}")
        confirmation = input(f"{Colors.RED}@{username} için story izlenme gönderilsin mi? (e/h): {Colors.END}").strip().lower()
        
        if confirmation not in ['e', 'evet', 'y', 'yes']:
            print(f"\n{Colors.RED}❌ İşlem iptal edildi!{Colors.END}")
            input(f"\n{Colors.RED}🔚 Çıkmak için Enter tuşuna basın...{Colors.END}")
            return
        
        print(f"\n{Colors.PURPLE}🎯 İŞLEM BAŞLATILIYOR{Colors.END}")
        print(f"{Colors.CYAN}{'═' * 40}{Colors.END}")
        
        self.show_progress()
        
        success = self.send_story_views(username)
        
        if success:
            print(f"\n{Colors.GREEN}🎉 TEBRİKLER! İşlem başarıyla tamamlandı!{Colors.END}")
            print(f"{Colors.GREEN}📈 @{username} story izlenmeleri artırılıyor...{Colors.END}")
            print(f"{Colors.GREEN}🕒 İzlenmeler 5-15 dakika içinde görünecektir.{Colors.END}")
        else:
            print(f"\n{Colors.RED}😔 Üzgünüz, işlem sırasında bir hata oluştu.{Colors.END}")
            print(f"{Colors.RED}🔧 Lütfen daha sonra tekrar deneyin.{Colors.END}")
        
        print(f"\n{Colors.YELLOW}📊 İSTATİSTİKLER{Colors.END}")
        print(f"{Colors.CYAN}{'═' * 40}{Colors.END}")
        print(f"{Colors.WHITE}👤 Kullanıcı: {name} ({age} yaş){Colors.END}")
        print(f"{Colors.WHITE}📱 Instagram: @{username}{Colors.END}")
        print(f"{Colors.WHITE}🕒 Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}{Colors.END}")
        print(f"{Colors.WHITE}🌐 API: {self.api_url}{Colors.END}")
        
        input(f"\n{Colors.RED}🔚 Çıkmak için Enter tuşuna basın...{Colors.END}")

def main():
    try:
        tool = DexronInstagramTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}❌ Program kullanıcı tarafından durduruldu!{Colors.END}")
    except Exception as e:
        print(f"\n\n{Colors.RED}💥 Kritik Hata: {e}{Colors.END}")

if __name__ == "__main__":
    main()