import turtle
import random
import time

wn = turtle.Screen()
wn.screensize(800,600)
wn.tracer(0)
wn.bgcolor("tomato")


onceki_zaman = time.time()
oyun_zamani = 60


t = turtle.Turtle()
t.up()
t.ht()
t.goto(-200,250)
t.write("Time: " + str(oyun_zamani),align="center",font=("Arial", 30, "normal"))

maze = turtle.Turtle()
maze.up()
maze.color("red","blue")
maze.speed(0)
maze.shape("square")


p = turtle.Turtle()
p.up()
p.color("blue")
p.speed(0)
p.shape("turtle")
p.goto(50,50)

e = turtle.Turtle()
e.up()
e.color("red")
e.speed(0)
e.shape("turtle")

score = 0
can = 3


walls = []
colors = ["blue","red","yellow","green"]
points = []



def make_maze(yon, tekrar, x, y):
    maze.goto(x,y)
    maze.seth(yon)
    
    for i in range(tekrar):
        #renk = random.choice(colors)
        index = i % len(colors)
        renk = colors[index]
        maze.color(renk)
        maze.stamp()
        konum = maze.pos()
        walls.append(konum)
        maze.fd(10)
     

make_maze(0, 40, -200, 200)
make_maze(270, 40, 200, 200)
make_maze(180, 40, 200, -200)
make_maze(90, 40, -200, -200)

make_maze(270, 30, -100, 200)
make_maze(90, 30, -10, -200)
make_maze(180, 13, 200, -90)

def make_point(count):
    for i in range(count):
        c = turtle.Turtle()
        c.up()
        c.color("yellow")
        c.speed(0)
        c.shape("circle")
        c.goto(random.randint(-180,180),random.randint(-180,180))
        for konum in walls:
            if c.distance(konum) < 15:
                c.goto(random.randint(-180,180),random.randint(-180,180))

        points.append(c)

make_point(5)

def go_right():
    p.setx(p.xcor() + 20)
    p.seth(0)
def go_left():
    p.setx(p.xcor() - 20)
    p.seth(180)
def go_up():
    p.sety(p.ycor() + 20)
    p.seth(90)
def go_down():
    p.sety(p.ycor() - 20)
    p.seth(270)

pen = turtle.Turtle()
pen.up()
pen.ht()
pen.goto(250,250)
pen.write("score: " + str(score) + "\nlive: " + str(can),font=("Arial", 20, "normal"))

wn.listen()
wn.onkey(go_right,"d")
wn.onkey(go_left,"a")
wn.onkey(go_down,"s")
wn.onkey(go_up,"w")

while True:
    for wall in walls:
        if p.distance(wall) < 30:
            p.fd(-20)
        if e.distance(wall) < 30:
            angle = e.towards(p)
            e.seth(angle)
    e.fd(1)
    if p.distance(e) < 20:
        p.goto(50,50)
        can -= 1
        pen.clear()
        pen.write("score: " + str(score) + "\nlive: " + str(can),font=("Arial", 20, "normal"))
    for c in points:
        if p.distance(c) < 30:
            c.ht()
            points.remove(c)
            score += 1
            pen.clear()
            pen.write("score: " + str(score) + "\nlive: " + str(can),font=("Arial", 20, "normal"))
            break
    if can <= 0 or oyun_zamani <= 0:
        pen.clear()
        pen.goto(0,220)
        pen.color("red")
        pen.write("Kaybettiniz",align="center",font=("Arial", 60, "normal"))
        t.clear()
        wn.update()
        break
    elif score == 5:
        pen.clear()
        pen.goto(0,220)
        pen.color("green")
        pen.write("Kazandınız",align="center",font=("Arial", 60, "normal"))
        t.clear()
        wn.update()
        break
    
    time.sleep(0.01)
    if time.time() - onceki_zaman > 1:
        oyun_zamani -= 1
        onceki_zaman = time.time()
        t.clear()
        t.write("Time: " + str(oyun_zamani),align="center",font=("Arial", 30, "normal"))
    wn.update()


wn.mainloop()