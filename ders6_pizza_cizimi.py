import turtle
from random import randint


wn = turtle.Screen()
wn.screensize(800,600)
wn.tracer(0)
wn.bgcolor("spring green")

k = turtle.Turtle()
k.color("dark orange")
k.up()
k.ht()
k.dot(400)

k.color("gold")
k.dot(350)

k.color("orange")
k.down()
k.pensize(13)

for i in range(8):
    k.left(45)
    k.fd(169)
    k.goto(0,0)


k.up()

sucuksayisi = randint(12,20)

for i in range(sucuksayisi):
    k.seth(randint(0,360))
    k.goto(0,0)
    k.fd(randint(30,167))
    k.color("black")
    k.dot(randint(30,40))
    k.color("dark red")
    k.dot(randint(20,30))


zeytinsayisi = randint(24,30)

for i in range(zeytinsayisi):
    k.seth(randint(0,360))
    k.goto(0,0)
    k.fd(randint(30,167))
    k.color("olive drab")
    k.dot(randint(10,20))


misirsayisi = randint(24,34)

for i in range(misirsayisi):
    k.seth(randint(0,360))
    k.goto(0,0)
    k.fd(randint(50,167))
    k.down()
    k.color("khaki","yellow")
    k.shape("square")
    k.shapesize(0.5,0.7,3)
    k.stamp()
    k.up()

peynirsayisi = randint(24,34)

for i in range(peynirsayisi):
    k.seth(randint(0,360))
    k.goto(0,0)
    k.fd(randint(50,167))
    k.down()
    k.color("white")
    k.shape("triangle")
    k.shapesize(0.5,0.7,4)
    k.stamp()
    k.up()


wn.update()

wn.mainloop()