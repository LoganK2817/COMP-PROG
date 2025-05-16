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
mark.speed(100)
mark.pensize(10)




class stringlights:

    def string():
        mark.penup()
        mark.pencolor("black")
        mark.pendown()
        for i in range(90):
            mark.right(1)
            mark.forward(.5)
        for i in range(90):
            mark.left(1)
            mark.forward(.5)

turtle.done()