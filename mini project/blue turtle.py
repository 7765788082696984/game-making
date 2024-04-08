import turtle

turtle.bgcolor('white')

turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('blue')
turtle.hideturtle()
def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def drawsign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

drawsign()
turtle.done()