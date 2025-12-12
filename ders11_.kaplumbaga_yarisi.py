import turtle
import time
import random




wn = turtle.Screen()
wn.setup(600,600)
wn.tracer(0)
wn.bgcolor("light gray")

kaplumbagalar = []
kazananlar = []
colors = ["blue","red","yellow","green","orange"]

cizgi = turtle.Turtle()
cizgi.up()
cizgi.goto(250,150)
cizgi.seth(270)
cizgi.shape("square")
cizgi.shapesize(1.3,1.5)


for i in range(5):
    cizgi.color("black")
    cizgi.stamp()
    cizgi.fd(30)
    cizgi.color("white")
    cizgi.stamp()
    cizgi.fd(30)
    cizgi.ht()
cizgi.color("black")
cizgi.stamp()


for i in range(5):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.up()
    racer.color(colors[i])
    racer.goto(-200,100 - i*50)
    racer.down()
    kaplumbagalar.append(racer)



while True:
    for racer in kaplumbagalar:
        racer.fd(random.randint(1,5))
        if racer.xcor() > 240:
            racer.ht()
            racer.clear()
            kaplumbagalar.remove(racer)
            kazananlar.append(racer.pencolor())
    if len(kaplumbagalar) == 0:
        break
    
    time.sleep(0.01)
    wn.update()
cizgi.seth(90)
cizgi.shape("square")
cizgi.clearstamps()
cizgi.goto(-110,0)
cizgi.up()
cizgi.color("silver")
cizgi.st()
cizgi.shapesize(6,8)
cizgi.stamp()
cizgi.goto(-10,20)
cizgi.color("gold")
cizgi.shapesize(7,10)
cizgi.stamp()
cizgi.goto(100,-20)
cizgi.color("brown")
cizgi.shapesize(4,6)
cizgi.stamp()
cizgi.ht()


def konum(x,y):
    print(x,y)

wn.onscreenclick(konum)

print(kazananlar)

wn.update()
wn.mainloop()