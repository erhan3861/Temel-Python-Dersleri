import turtle
import random


for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.up()

turtle.goto(-100,100)
turtle.down()


for i in range(3):
    turtle.left(120)
    turtle.forward(100)

turtle.up()
turtle.goto(200,100)
turtle.down()

for i in range(5):
    turtle.left(360/5)
    turtle.forward(100)

turtle.color("red")
turtle.up()
turtle.goto(200,-100)
turtle.down()
turtle.dot(50)

colors = ["red","blue","green","yellow"]

for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    size = 20 + i*5
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.dot(size)
    c = random.choice(colors)
    turtle.color(c)
# kullanıcıden renkler al listeye ekle top sayısı al top sayısı kadar renkli top buyukluk 100den baslayıp 1 1 azalt









turtle.done()