import turtle
import time
import random



score = 0
highscore = 0
delay = 0.1

wn = turtle.Screen()
wn.setup(600,600)
wn.tracer(0)
wn.bgcolor("black")

head = turtle.Turtle()
head.shape("square")
head.up()
head.color("white")
head.direction = "stop"

segments = []

food = turtle.Turtle()
food.shape("circle")
food.up()
food.color("yellow")
food.goto(0,100)

pen = turtle.Turtle()
pen.shape("circle")
pen.up()
pen.color("white")
pen.ht()
pen.goto(0,260)
pen.write("Skor: 0  Yüksek Skor: 0", align="center", font=("Courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkey(go_up,"w")
wn.onkey(go_down,"s")
wn.onkey(go_left,"a")
wn.onkey(go_right,"d")

while True:
    wn.update()
    # çarpışma
    if head.xcor() > 275 or head.xcor() < -275 or head.ycor() > 275 or head.ycor() < -275:
        time.sleep(1)
        head.home()
        head.direction = "stop"
        for i in segments:
            i.goto(500,500)
        segments.clear()

        score = 0
        pen.clear()
        pen.write(f"Skor: {score}  Yüksek Skor: {highscore}", align="center", font=("Courier", 24, "normal"))
        delay = 0.1
    # yemek
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)
        body = turtle.Turtle()
        body.shape("square")
        body.up()
        body.color("gray")
        segments.append(body)
        
        score += 1
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write(f"Skor: {score}  Yüksek Skor: {highscore}", align="center", font=("Courier", 24, "normal"))
        delay -= 0.001

    for i in range(len(segments) - 1,0,-1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x,y)
    if segments:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()

    # kendine çarpma
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.home()
            head.direction = "stop"
            for i in segments:
                i.goto(500,500)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"Skor: {score}  Yüksek Skor: {highscore}", align="center", font=("Courier", 24, "normal"))
            delay = 0.1





    time.sleep(delay)




wn.mainloop()