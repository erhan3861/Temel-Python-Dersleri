"""
mikrofon
kamera
altyazı
emoji
ekran paylaşımı
el kaldır
diyer seçenekler
görüşmeden çık
herkesi göster
sohbet
etkinlikler
"""

def mikrofon():
    sor = input("mikrofon açıkmı? a/k")
    if sor == "a":
        print("mikrofon kapatıldı")
    elif sor == "k":
        print("mikrofon açıldı")

def kamera():
    sor = input("kamera açıkmı? a/k")
    if sor == "a":
        print("kamera kapatıldı")
    elif sor == "k":
        print("kamera açıldı")
def altyazi():
    dil = ["Türkçe","İngilizce","Almanca"]
    ac = input("altyazıyı açmakmı istiyorsunuz kapatmakmı a/k")
    if ac == "a":
        print(dil)
        secim = input("dil seçiniz t:i:a")
        if secim == "t": print("Türkçe altyazılar açıldı")
        elif secim == "i": print("İngilizce altyazılar açıldı")
        elif secim == "a": print("Almanca Altyazılar açıldı")

    else:
        print("altyazı kapatıldı")

def emoji():
    emoji = input("😊:1 😡:2 ❤️:3")
    if emoji == "1":
        print("😊")
    elif emoji == "2":
        print("😡")
    elif emoji == "3":
        print("❤️")
    else:
        print("lütfen 1/2/3 sayılarından birini giriniz")

def ekran():
    sor = input("ekran paylaşılıyormu? e/h")
    if sor == "e":
        print("ekran paylaşımı kapatıldı")
    elif sor == "h":
        print("ekran paylaşımı başlatıldı")

def el():
    sor = input("el havadamı? e/h")
    if sor == "e":
        print("el indirildi")
    elif sor == "h":
        print("el kaldırıldı")

def gorusmedencıkıs():
    sor = input("çıkmak istediğinize eminmisiniz? e/h")
    if sor == "e":
        print("görüşmeden ayrılındı")
    elif sor == "h":
        print("iptal edildi")

def diyer():
    secenek = input(":1 :2 :3")
    if secenek == "1":
        print("")
    elif secenek == "2":
        print("")
    elif secenek == "3":
        print("")
    else:
        print("lütfen 1/2/3 sayılarından birini giriniz")

while True:
    girdi = input("""
  1. Mikrofon
  2. Kamera
  3. Alt Yazı
  4. Emoji
  5. Ekran Paylaşımı
  6. El Kaldır
  7. Diyer Seçenekler
  8. Görüşmeden Cık
  9. Çıkış
  """)
    if girdi == "1":
        mikrofon()
    elif girdi == "2":
        kamera()
    elif girdi == "3":
        altyazi()
    elif girdi == "4":
        emoji()
    elif girdi == "5":
         ekran()
    elif girdi == "6":
        el()
    elif girdi == "7":
        diyer()
    elif girdi == "8":
        gorusmedencıkıs()
    elif girdi == "9":
        print("seçim durduruluyor")
        break