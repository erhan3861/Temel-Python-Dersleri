# hazine adası resmi / rakip oyuncu
import turtle
from random import randint

window = turtle.Screen()
window.setup(800,600)
window.bgpic("images/hazineadasi.gif")

oyunmodu = input("oyun modu giriniz multiplayer/singleplayer")


if oyunmodu == "m":
    t2 = turtle.Turtle()
    t2.shape("turtle")
    t2.color("blue")


t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")

hak1 = 3
hak2 = 3


hedef = turtle.Turtle()
hedef.up()
hedef.shape("circle")
hedef.color("yellow")

def rastgele():
    hedef.setx(randint(-350,350))
    hedef.sety(randint(-250,250))

rastgele()

def check():
    distance = t1.distance(hedef)
    if distance < 5:
        print("kazandınız")
        return True
    else:
        return False

while True:
    a = int(input("Açı giriniz:"))
    m = int(input("Mesafe giriniz:"))

    t1.setheading(a)
    t1.forward(m)

    if oyunmodu == "multiplayer":
        a = int(input("Açı giriniz:"))
        m = int(input("Mesafe giriniz:"))
        
        t2.setheading(a)
        t2.forward(m)


    hak1 -= 1
    
    if hak1 == 0 or check():
        cevap = input("durmak istiyormusunuz? e/h")
        if cevap == "e":
            break
        else:
            hak1 = 3
            rastgele()


turtle.done()