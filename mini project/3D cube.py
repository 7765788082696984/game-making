import turtle
import time
t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800,500,bg="black")
t.pencolor("white")
t.pensize(3)

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)



square()
t.left(30)
t.forward(100)
#time.sleep(2)
t.right(30)
#time.sleep(2)
square()
t.left(90)
t.forward(100)
t.left(90+30)
t.forward(100)
t.right(30+180)
t.forward(100)
t.left(30)
t.forward(100)
t.right(30+90)
t.forward(100)
t.right(60)
t.forward(100)
turtle.done()