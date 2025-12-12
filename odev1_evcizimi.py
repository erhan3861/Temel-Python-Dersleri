import turtle


wn = turtle.Screen()
wn.screensize(800,600)
wn.tracer(0)
wn.bgcolor("sky blue")




k = turtle.Turtle()
k.ht()
k.up()
k.goto(-400,350)

k.goto(-2000,100)
k.color("spring green")
k.seth(0)
k.begin_fill()

for i in range(2):
    k.fd(4000)
    k.right(90)
    k.fd(500)
    k.right(90)


k.end_fill()

k.goto(0,0)
k.right(90)
k.fd(100)
k.color("black","white")
k.shape("square")
k.shapesize(30,20,5)
k.stamp()

k.color("white")
k.goto(0,0)
k.seth(0)
k.left(90)
k.fd(100)
k.shapesize(12,12)
k.stamp()

k.goto(0,0)
k.seth(0)
k.left(90)
k.fd(100)
k.st()
k.shape("circle")
k.color("black","orange red")
k.shapesize(1,1)

def cati():
    k.up()
    k.goto(0,0)
    k.seth(0)
    k.left(90)
    k.fd(100)
    
    k.st()
    k.seth(0)
    k.fd(100)
    k.down()
    
    k.fd(250)

    k.left(135)
    k.fd(250)
    
    k.seth(0)
    k.left(180)
    k.fd(350)

    k.seth(0)
    k.right(135)
    k.fd(250)

    k.seth(0)
    k.fd(250)
    k.left(45)
    k.fd(150)

    k.seth(0)
    k.right(45)
    k.fd(150)


k.begin_fill()
cati()
k.end_fill()

k.color("black")
k.down()
k.pensize(5)
cati()

k.up()
k.goto(0,0)
k.seth(0)
k.left(90)
k.fd(100) 
k.st()
k.seth(0)
k.fd(100)
k.fd(250)
k.left(135)
k.fd(250)
k.seth(0)
k.left(180)
k.fd(350)
k.seth(0)
k.right(135)
k.fd(250)

k.color("yellow")
k.pencolor("yellow")
k.pensize(20)
k.down()

k.seth(0)
k.fd(250)
k.left(45)
k.fd(150)
k.seth(0)
k.right(45)
k.fd(150)
k.seth(0)
k.fd(240)
k.ht()


k.st()
k.color("black","cyan")
k.up()
k.goto(0,0)

k.seth(0)
k.fd(250)

def pencere():
    k.color("black","cyan")
    k.begin_fill()

    for i in range(4):
        k.right(90)
        k.fd(100)

    k.end_fill()
    k.color("black")
    k.down()
    k.pensize(5)

    for i in range(4):
        k.right(90)
        k.fd(100)

    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(50)
    k.right(90)
    k.fd(100)
    k.right(90)
    k.fd(50)



pencere()
k.seth(0)
k.color("medium blue")
k.pensize(20)
k.fd(100)
k.up()
k.st()
k.goto(0,0)
k.seth(180)
k.fd(150)
k.seth(0)
pencere()
k.seth(0)
k.color("medium blue")
k.pensize(20)
k.fd(100)
k.up()

k.goto(-47,0)
k.seth(0)
k.left(90)
k.fd(130)
pencere()
k.up()
k.goto(0,0)
k.seth(0)
k.right(90)
k.fd(300)
k.seth(180)
k.fd(75)
k.color("cyan")
k.begin_fill()
k.seth(90)
for i in range(2):
    k.fd(250)
    k.right(90)
    k.fd(150)
    k.right(90)

k.end_fill()
k.color("black")
k.down()
for i in range(2):
    k.fd(250)
    k.right(90)
    k.fd(150)
    k.right(90)

k.fd(250)
k.right(90)
k.fd(150)
k.right(90)
k.fd(125)
k.right(90)
k.up()
k.fd(20)
k.dot(10)

wn.update()

wn.mainloop()