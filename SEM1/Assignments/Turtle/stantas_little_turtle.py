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
mark.speed(2000)
mark.pensize(10)

def get_x():
    return mark.xcor()

def get_y():
    return mark.ycor()

def move_turtle_for_next_shape():
    mark.penup()
    mark.goto(mark.xcor() - 30, mark.ycor() - 80)
    mark.setheading(0)
    mark.pendown()

def prep():
    x, y = mark.position()
    mark.penup()
    mark.goto(x + 120, y)

class shapes:

    def square(x_offset,y_offset):
        mark.penup()
        mark.goto(0 + x_offset, 0 - y_offset)
        mark.setheading(0)
        mark.pendown()

        present_color = random.randint(1,3)
        if present_color == 1:
            mark.pencolor("red")
            mark.fillcolor("red")
        elif present_color == 2:
            mark.pencolor("blue")
            mark.fillcolor("blue")
        elif present_color == 3:
            mark.pencolor("green")
            mark.fillcolor("green")
        mark.begin_fill()

        for i in range(4):
            mark.forward(80)
            mark.left(90)
        mark.end_fill()

    def ribbon1(x_offset,y_offset):
        mark.penup()
        mark.goto(0 + x_offset, 30 -y_offset)
        mark.setheading(0)
        mark.pendown()
        mark.pencolor("white")
        mark.fillcolor("white")
        mark.begin_fill()
        for i in range(2):
            mark.forward(80)
            mark.left(90)
            mark.forward(15)
            mark.left(90)
        mark.end_fill()

    def ribbon2(x_offset,y_offset):
        mark.penup()
        mark.goto(30 + x_offset, 80 -y_offset)
        mark.setheading(-90)
        mark.pendown()
        mark.pencolor("white")
        mark.fillcolor("white")
        mark.begin_fill()
        for i in range(2):
            mark.forward(80)
            mark.left(90)
            mark.forward(15)
            mark.left(90)
        mark.end_fill()

    def bow1(x_offset,y_offset):
        mark.penup()
        mark.goto(40 + x_offset, 85 -y_offset)
        mark.setheading(0)
        mark.pensize(5)
        mark.pendown()
        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.begin_fill()
        mark.left(110)
        for i in range(3):
            mark.forward(35)
            mark.left(120)
        mark.end_fill()

    def bow2(x_offset,y_offset):
        mark.penup()
        mark.goto(40 + x_offset, 85 -y_offset)
        mark.setheading(0)
        mark.pensize(5)
        mark.pendown()
        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.begin_fill()
        mark.left(10)
        for i in range(3):
            mark.forward(35)
            mark.left(120)
        mark.end_fill()

def make_present(x_offset,y_offset):
    shapes.bow1(x_offset,y_offset)
    shapes.bow2(x_offset,y_offset)
    shapes.square(x_offset,y_offset)
    shapes.ribbon1(x_offset,y_offset)
    shapes.ribbon2(x_offset,y_offset)
    move_turtle_for_next_shape()
    prep()

# Main loop to draw presents


row_num = int(simpledialog.askstring("Input", "how many rows?"))
column_num = int(simpledialog.askstring("Input", "how many columns??"))

def make_presents_grid():
    y_offset = 0
    for h in range(column_num):  # next column
        
        for i in range(row_num):  # make row
            x_offset = get_x()  # Store current x position
            make_present(x_offset,y_offset)
            mark.penup()
            # Move to the next position in the row

        y_offset += 150
        mark.goto(0,get_y())
        mark.pendown()  # Ready to draw the next row


make_presents_grid()
mark.penup()
mark.goto(0,0)



turtle.done()
