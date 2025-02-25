import turtle

import tkinter as tk
from tkinter import simpledialog

import random

mark = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("pink")
mark.shape("turtle")
mark.color("black")
mark.speed(5)
mark.pensize(10)

class shapes:

    def star():

        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.begin_fill()
        for i in range(5):
            mark.forward(100)  # Move forward by 100 units
            mark.right(144) 
        mark.end_fill()


    def fillstar():
        mark.penup()
        mark.goto(mark.xcor()+42, mark.ycor()-2)
        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.pendown()
        mark.begin_fill()
        for i in range(4):
            mark.forward(25)
            mark.right(90)
        mark.end_fill()


shapes.star()
shapes.fill()

turtle.done()