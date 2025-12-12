import turtle
from PIL import Image
from random import randint
import os

window = turtle.Screen()
window.setup(800,600)
window.bgcolor("cyan")
window.addshape("images/ship1.gif")
window.addshape("images/ship2.gif")
window.addshape("images/cannon.gif")
window.tracer(0)

ship1 = turtle.Turtle()
ship1.shape("images/ship1.gif")
ship1.up()

x = randint(-350,350)
y = randint(-250,250)

ship2 = turtle.Turtle()
ship2.shape("images/ship2.gif")
ship2.up()
ship2.goto(x,y)

cannon = turtle.Turtle()
cannon.shape("circle")
cannon.color("red")
cannon.up()
cannon.speed(0)
cannon.ht()

def fire():
    new = cannon.clone()
    new.goto(ship2.pos())
    new.seth(ship2.heading())
    new.st()

    for i in range(30):
        new.fd(10)
        window.update()

def fire2():
    new = cannon.clone()
    new.goto(ship1.pos())
    new.seth(ship1.heading())
    new.color("blue")
    new.st()

    for i in range(30):
        new.fd(10)
        if new.distance(ship2) < 50:
            ship2.ht()
            ship2.home()
            ship2.st()

        window.update()




image = "images/ship1.png"

def gemiyi_dondur(x,y):
    global image,ship1
    # 1. Pillow ile bir resmi açın
    image = Image.open("images/ship1.png")   
    
    angle = ship1.towards((x,y))
    ship1.setheading(angle)


    # 2. Resmi döndürün (örneğin, 45 derece döndürme)
    image = image.rotate(angle + 90, expand=True)
    
    # 3. Resmi .png formatında kaydedin
    image.save("images/ship1.gif")

def ds_gemiyi_dondur(x,y):
    image = Image.open("images/ship2.png")   
    
    angle = ship2.towards((x,y))
    ship2.setheading(angle)

    image = image.rotate(angle + 90, expand=True)
    
    image.save("images/ship2.gif")


def check_border():
    if ship2.xcor() < -400 or ship2.xcor() > 400 or ship2.ycor() > 300 or ship2.ycor() < -300:
        return True

window.listen()
window.onkey(fire2,"space")
window.onscreenclick(gemiyi_dondur)
window.onscreenclick(ds_gemiyi_dondur,3)

while True:
    window.addshape("images/ship1.gif")
    ship1.shape("images/ship1.gif")
    ship1.fd(1)

    window.addshape("images/ship2.gif")
    ship2.shape("images/ship2.gif")
    ship2.fd(1)
    
    if check_border():
        x,y = ship1.pos()
        ds_gemiyi_dondur(x,y)
        fire()

    window.update()




turtle.done()