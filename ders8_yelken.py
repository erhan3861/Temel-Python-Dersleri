import turtle


wn = turtle.Screen()
wn.screensize(800,600)
wn.tracer(0)
wn.bgcolor("cyan")


k = turtle.Turtle()
k.ht()
k.up()
k.color("brown")
k.bk(150)

k.begin_fill()

k.rt(45)
k.fd(90)
k.lt(45)
k.fd(200)
k.lt(45)
k.fd(90)
k.lt(135)

k.end_fill()

k.goto(0,0)
k.seth(90)
k.fd(5)
k.color("black","light slate gray")
k.shapesize(1,11,5)
k.shape("square")
k.st()
k.fd(105)
k.stamp()

k.shape("circle")
k.color("white")
k.shapesize(1,1)
k.goto(14,220)
k.begin_fill()

k.goto(14,220)
k.goto(172,28)
k.goto(14,28)
k.end_fill()

k.goto(-14,220)
k.begin_fill()
k.goto(-14,220)
k.goto(-122,28)
k.goto(-14,28)
k.end_fill()

k.goto(0,0)
k.seth(270)
k.fd(50)



def kordinat(x,y):
    print(x,y)


wn.onscreenclick(kordinat)

k.color("blue")
k.pensize(3)
def dalga(startx,starty):
    k.goto(startx,starty)
    k.down()
    k.seth(45)
    k.fd(50)
    k.seth(-45)
    k.fd(50)
    wn.update()

for i in range(10):
    dalga(i*75-370,-70)
k.up()
for i in range(10):
    dalga(i*75-370,-110)
    





wn.update()
wn.mainloop()