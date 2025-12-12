import turtle
from random import randint
import time

# target adım hakı 100 eğer 10 hit olursa kazanılcak olmaz ise kaybedilicek hak ve hit sayısı sonda yazılıcak + win yada lose yazılcak

wn = turtle.Screen()
wn.setup(800,600)
wn.tracer(0)
wn.title("Target Game")

oncekizaman = time.time()

t = turtle.Turtle()
t.color("sky blue")
t.ht()
t.up()
t.goto(-400,300)
t.begin_fill()

for i in range(2):
    t.fd(800)
    t.right(90)
    t.fd(200)
    t.right(90)

t.end_fill()

t.goto(-400,100)
t.color("spring green")
t.seth(0)
t.begin_fill()

for i in range(2):
    t.fd(800)
    t.right(90)
    t.fd(400)
    t.right(90)


t.end_fill()

t.goto(0,0)
t.color("red")
t.dot(300)
t.color("white")
t.dot(230)
t.color("red")
t.dot(150)
t.color("white")
t.dot(60)

target = turtle.Turtle()
target.color("yellow")
target.shape("circle")
target.up()
target.goto(0,0)
target.shapesize(2)

def rastgele():
    rx = randint(-150,150)
    ry = randint(-150,150)
    target.goto(rx,ry)
    wn.update()

def vur(x,y):
    if target.distance((x,y)) < 60:
        print("hit")
    else:
        print("miss")
    print(target.distance((x,y)))


wn.onscreenclick(vur)

while True:
    if time.time() - oncekizaman > 1:
        rastgele()
        oncekizaman = time.time()
    


wn.mainloop()