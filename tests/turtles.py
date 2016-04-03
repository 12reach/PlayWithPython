#!/usr/bin/python3

import turtle

pen = turtle.Pen()
pen.speed(0)
turtle.bgcolor("black")
colors =['red', 'orange', 'yellow', 'blue', 'pink', 'white', 'purple', 'green', 'light blue']
sides = 8

for x in range(360):
    pen.pencolor(colors[x % sides])
    pen.forward(x * sides / 3 + x)
    pen.left(360 / sides + 1)
    pen.width(x * sides / 100)
