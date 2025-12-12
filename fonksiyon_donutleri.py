# For döngülerinde break Fonksiyonlarda return
from random import randint

print("araba oyunu")

araba1 = None
araba2 = None
mod = "menu"
puan1 = 0
puan2 = 0
arabarenk1 = None
arabarenk2 = None

def menugoster():
    menu = input("singleplayer :1 , multiplayer :2")
    if menu == "1":
        print("Singleplayer sectiniz")
        mod= "sp"
        singleplayer()
    else:
        print("Multiplayer sectiniz")
        mod = "mp"
        multiplayer()
    return menu

def arabasecim():
    araba = input("""
    1.Hızlı Araba
    2.Güçlü Araba
    3.Dayanıklı Araba
    """)
    if araba == "1":
        print("Hızlı Arabayı seçtiniz")
        return "hızlı"
    elif araba == "2":
        print("Güçlü Arabayı seçtiniz")
        return "güçlü"
    elif araba == "3":
        print("Dayanıklı Arabayı seçtiniz")
        return "dayanıklı"

def arabarengi():
    arabarenk = input("""
    1.Kırmızı Araba
    2.Mavi Araba
    3.Yesil Araba
    """)
    if arabarenk == "1":
        print("Kırmızı Rengi seçtiniz")
        return "Kırmızı"
    elif arabarenk == "2":
        print("Mavi Rengi seçtiniz")
        return "Mavi"
    elif arabarenk == "3":
        print("Yeşil Rengi seçtiniz")
        return "Yeşil"

def singleplayer():
    global araba1,araba2,mod
    araba1 = arabasecim()
    araba2 = None
    arabarenk1 = arabarengi()
    mod = "sp"

def  multiplayer():
    global araba1,araba2,mod
    araba1 = arabasecim()
    araba2 = arabasecim()
    arabarenk1 = arabarengi()
    arabarenk2 = arabarengi()
    print(f"1. Secildi:{araba1},{arabarenk1} 2.Secildi:{araba2},{arabarenk2}")

menugoster()

print("oyuna baslamak icin s tusuna basın")

tus = input()
if tus == "s":
    mod = "oyun"

while True:
    if araba1 and araba2:
        print("MultiPlayer Yarış Başladı")
        user1 = int(input("Sayınızı Giriniz:(1-100)"))
        user2 = int(input("Sayınızı Giriniz:(1-100)"))
        com = randint(1,100)

        if abs(com - user1) > abs(com - user2):
            print("1.Tur 2. Yarışcı kazandı Bilgisayarın secimi:",com) 
            puan2 += 1
            if puan2 == 3:
                print("oyunu ikinci yarışcı kazandı")
                break
        elif abs(com - user1) < abs(com - user2):
            print("1.Tur 1. Yarışcı kazandı Bilgisayarın secimi:",com)
            puan1 += 1
            if puan1 == 3:
                print("oyunu birinci yarışcı kazandı")
                break
        else:
            print("1.Tur Berabere bitti")