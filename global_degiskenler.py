#  değiskeni fonksiyonda DEĞİŞTİRİYORSAK global kullanırız
#  değişkeni fonksiyonda KULLANIYORSAK global yok

from random import randint
import time

print("uzay oyunu")
time.sleep(1)
score = 0
live = 3

def attack():
    global score 
    time.sleep(1)
    result = randint(0,1)
    if result:
        score += 1
        print("düşmanı vurdunuz skorunuz =",score)
    else:
        print("düşmanı vuramadınız")
    time.sleep(1)

def defense():
    global score, live
    result = randint(0,1)
    if result:
        score += 2
        print("düşmanın saldırısını başarıyla savurdunuz =",score)
    else:
        live -= 1
        print("savunma başarısız oldu canınız =",live)

def display_score():
    print("score = ", score, "live =", live)

def restart():
    global score, live
    score = 0
    live = 3
    print("oyun yeniden başlatıldı")
    display_score()

while True:
    option = input("1.Attack\t2.Defense\t3.Restart\t4.Exit")
    if option == "1":
        attack()
    elif option == "2":
        defense()
    elif option == "3":
        restart()
    elif option == "4":
        break
    else:
        print("doğru seçenek giriniz")
    
    if live <= 0:
        print("Game Over you lost")
        break
    elif score >= 5:
        print("You win")
        break