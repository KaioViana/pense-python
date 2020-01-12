import turtle
from random import randint


loadWindow = turtle.Screen()
turtle.colormode(255)
turtle.speed(0)

turtle.begin_fill()
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    turtle.color(randint(100, 255), randint(100, 255), randint(100, 255))
turtle.end_fill()
turtle.done()
