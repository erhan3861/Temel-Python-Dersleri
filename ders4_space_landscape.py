import turtle
import random
import time


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(600,600)
wn.tracer(0)
wn.addshape("images/rocket.gif")

stars = []

star = turtle.Turtle()
star.color("white")
star.shape("circle")
star.up()




for i in range(200):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    s = star.clone()
    s.shapesize(random.uniform(0.1,0.5))
    s.goto(x,y)
    stars.append(s)

moon = turtle.Turtle()
moon.color("gray")
moon.up()
moon.goto(100,150)
moon.dot(40)



planet = turtle.Turtle()
planet.color("light gray")
planet.shape("circle")
planet.up()
planet.goto(-40,-500)
planet.dot(700)

rocket = turtle.Turtle()
rocket.shape("images/rocket.gif")
rocket.up()

pen = turtle.Turtle()
pen.color("red")
pen.ht()
pen.up()
pen.goto(0,-300)
pen.write("space",align="center",font=("Arial", 40, "normal"))
wn.update()

def move(x,y):
    rocket.goto(x,y)
    wn.update()

wn.onclick(move)

while True:
    for s in stars:
        s.shapesize(random.uniform(0.1,0.5))
        if s.distance(planet) < 370:
            s.ht()
    
    time.sleep(0.1)
    wn.update()



wn.mainloop()

