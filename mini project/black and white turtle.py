import turtle
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.speed(0)
turtle.pensize(4)

for i in range(1, 300, 15):
    turtle.right(90)
    turtle.forward(i)
    turtle.right(270)
    turtle.pendown()
    turtle.circle(i)
    turtle.penup()
    turtle.home()

turtle.hideturtle()
turtle.mainloop()