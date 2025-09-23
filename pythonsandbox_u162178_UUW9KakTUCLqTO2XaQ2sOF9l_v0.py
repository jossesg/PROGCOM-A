import turtle
import math


t = turtle.Turtle()
t.speed(0)
t.hideturtle()

for i in range(8):
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.left(120)
    t.end_fill()
    t.left(45)


t.penup()
t.goto(0, -20)
t.pendown()
t.begin_fill()
t.fillcolor("orange")
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, -20) 
t.pendown()
t.color("green")
t.width(5) 
t.right(90)
t.forward(80)

turtle.done()