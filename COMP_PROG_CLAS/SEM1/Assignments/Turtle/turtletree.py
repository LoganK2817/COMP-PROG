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
mark.speed(50)
mark.pensize(5)


def prep_for_next_tri(): # puts turtle in place for overlaping triangles
    mark.penup()
    mark.setheading(0)
    mark.goto(mark.xcor(),mark.ycor() - 25 )


def prep_for_next_tree(): # puts turtle in place for next tree in row
    mark.penup()
    mark.setheading(0)


class tree: #all the shapes that make up tree

    def triangles():
        mark.penup()

        triangle_color = random.randint(1,3)
        if triangle_color == 1:
            mark.pencolor("#034a0f")
            mark.fillcolor("#034a0f")
        elif triangle_color == 2:
            mark.pencolor("#17572f")
            mark.fillcolor("#17572f")
        elif triangle_color == 3:
            mark.pencolor("#057d33")
            mark.fillcolor("#057d33")

        tri_size = 0
        for h in range(4): # number of triangles in tree
            mark.pendown()
            mark.begin_fill()
            mark.right(120)
            for i in range(3): # makes triangles themselves
                mark.forward(50 + tri_size)
                mark.left(120)
            mark.end_fill()
            prep_for_next_tri()
            tri_size += 20
        mark.penup()


    def trunk(x_off,y_off):
        mark.penup()
        mark.goto(-610 + x_off,210 + y_off) # move to correct position for trunk
        mark.pencolor("#70380c")
        mark.fillcolor("#70380c")
        mark.pendown()
        mark.begin_fill()
        for i in range(2): # makes the trunk itself
            mark.forward(20)
            mark.left(90)
            mark.forward(60)
            mark.left(90)
        mark.end_fill()
        mark.penup()
        mark.goto(-600 +x_off,400+y_off)

    def star(x_off,y_off):
        mark.penup()
        mark.pensize(2)
        mark.goto(-618 +x_off,410+y_off)
        mark.pendown()
        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.begin_fill()
        for i in range(5):
            mark.forward(35)  # Move forward by 100 units
            mark.right(144) 
        mark.end_fill()

    def fillstar():
        mark.penup()
        mark.goto(mark.xcor()+11, mark.ycor()-2)
        mark.pencolor("yellow")
        mark.fillcolor("yellow")
        mark.pendown()
        mark.begin_fill()
        for i in range(4):
            mark.forward(11)
            mark.right(90)
        mark.end_fill()
        



def make_tree(x_offset,y_offset):
    tree.trunk(x_offset,y_offset)
    tree.triangles()
    tree.star(x_offset,y_offset)
    tree.fillstar()

row_num = int(simpledialog.askstring("Input", "how many rows?"))
column_num = int(simpledialog.askstring("Input", "how many columns??"))

turtle.listen()

turtle.onkey(turtle.bye, "x")

def make_tree_grid():
    y_offset = 0
    for h in range(column_num):
        x_offset = 0
        for i in range(row_num):
            make_tree(x_offset,y_offset)
            x_offset += 120
        y_offset -= 250



make_tree_grid()

turtle.done()