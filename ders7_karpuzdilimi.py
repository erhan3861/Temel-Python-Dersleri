import turtle
from random import randint,uniform


wn = turtle.Screen()
wn.screensize(800,600)
wn.tracer(0)
wn.bgcolor("light sky blue")


k = turtle.Turtle()
k.ht()
k.up()
k.shape("turtle")


# Kabuk
k.right(180)
k.fd(100)
k.seth(0)
k.right(90)
k.begin_fill()
k.color("dark green")
k.circle(100,180)
k.end_fill()

# iç Kabuk
k.goto(0,0)
k.seth(0)
k.right(180)
k.fd(100)
k.seth(0)
k.fd(13.5)
k.right(90)
k.color("lime green")
k.begin_fill()
k.circle(85,180)
k.end_fill()

# iç kısım
k.goto(0,0)
k.seth(0)
k.right(180)
k.fd(100)
k.seth(0)
k.fd(22)
k.right(90)
k.color("red")
k.begin_fill()
k.circle(75,180)
k.end_fill()

# çekirdek
k.color("black")
k.goto(0,0)
k.shape("circle")
k.shapesize(0.4)
k.ht()


cekirdeksayisi = randint(14,20)
    
for i in range(cekirdeksayisi):
    k.seth(randint(190,340))
    k.fd(randint(20,65))
    k.shapesize(uniform(0.2,0.5))
    k.stamp()
    k.home()


wn.update()

wn.mainloop()