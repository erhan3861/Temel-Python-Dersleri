import turtle
from PIL import Image
from random import randint

window = turtle.Screen()
window.setup(800,600)
window.bgcolor("cyan")
window.addshape("images/ship.gif")
window.tracer(0)

ship1 = turtle.Turtle()
ship1.shape("images/ship.gif")
ship1.up()

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
    image.save("images/ship.gif")





window.onscreenclick(gemiyi_dondur)
    
while True:
    window.addshape("images/ship.gif")
    ship1.shape("images/ship.gif")
    ship1.fd(1)
    window.update()




turtle.done()