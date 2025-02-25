import turtle
import random
import tkinter as tk
from tkinter import simpledialog


def draw_scene():

    turtle.listen()


    turtle.onkey(print('f'), "n")


    Present_color = "blue"

    mark = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=1920, height=1080)
    screen.bgcolor("pink")
    mark.shape("turtle")
    mark.color("black")
    mark.speed(100)
    mark.pensize(10)


    def prep_for_next_tri(): # puts turtle in place for overlaping triangles
        mark.penup()
        mark.setheading(0)
        mark.goto(mark.xcor(),mark.ycor() - 25 )


    def prep_for_next_tree(): # puts turtle in place for next tree in row
        mark.penup()
        mark.setheading(0)

    def move_turtle_for_next_shape():
        mark.penup()
        mark.goto(mark.xcor() - 30, mark.ycor() - 80)
        mark.setheading(0)
        mark.pendown()


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

            tri_size = 10
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


        def trunk():
            mark.penup()
            mark.goto(0,-10) # move to correct position for trunk
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
            mark.goto(10,190)

        def star():
            mark.penup()
            mark.pensize(2)
            mark.goto(-8,200)
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
            
    class Present:
        # Variables to control the position of the present
        present_x = 15
        present_y = -20  # Adjusted 10 units lower

        def square():
            mark.penup()
            mark.goto(Present.present_x, Present.present_y)
            mark.setheading(0)
            mark.pendown()

            
            mark.pencolor(Present_color)
            mark.fillcolor(Present_color)
            mark.begin_fill()

            for i in range(4):
                mark.forward(40)  # Scaled down from 80 to 40
                mark.left(90)
            mark.end_fill()

        def ribbon1():
            mark.penup()
            mark.goto(Present.present_x, Present.present_y + 15)  # Adjusted with present_y
            mark.setheading(0)
            mark.pendown()
            mark.pencolor("white")
            mark.fillcolor("white")
            mark.begin_fill()
            for i in range(2):
                mark.forward(40)  # Scaled down from 80 to 40
                mark.left(90)
                mark.forward(7.5)  # Scaled down from 15 to 7.5
                mark.left(90)
            mark.end_fill()

        def ribbon2():
            mark.penup()
            mark.goto(Present.present_x + 15, Present.present_y + 40)  # Adjusted with present_y
            mark.setheading(-90)
            mark.pendown()
            mark.pencolor("white")
            mark.fillcolor("white")
            mark.begin_fill()
            for i in range(2):
                mark.forward(40)  # Scaled down from 80 to 40
                mark.left(90)
                mark.forward(7.5)  # Scaled down from 15 to 7.5
                mark.left(90)
            mark.end_fill()

        def bow1():
            mark.penup()
            mark.goto(Present.present_x + 20, Present.present_y + 42.5)  # Adjusted with present_y
            mark.setheading(0)
            mark.pensize(2.5)  # Scaled down from 5 to 2.5
            mark.pendown()
            mark.pencolor("yellow")
            mark.fillcolor("yellow")
            mark.begin_fill()
            mark.left(110)
            for i in range(3):
                mark.forward(17.5)  # Scaled down from 35 to 17.5
                mark.left(120)
            mark.end_fill()

        def bow2():
            mark.penup()
            mark.goto(Present.present_x + 20, Present.present_y + 42.5)  # Adjusted with present_y
            mark.setheading(0)
            mark.pensize(2.5)  # Scaled down from 5 to 2.5
            mark.pendown()
            mark.pencolor("yellow")
            mark.fillcolor("yellow")
            mark.begin_fill()
            mark.left(10)
            for i in range(3):
                mark.forward(17.5)  # Scaled down from 35 to 17.5
                mark.left(120)
            mark.end_fill()




    def make_present():
        Present.bow1()
        Present.bow2()
        Present.square()
        Present.ribbon1()
        Present.ribbon2()
        move_turtle_for_next_shape()



    def make_tree():
        tree.trunk()
        tree.triangles()
        tree.star()
        tree.fillstar()



    make_tree()
    make_present()


    turtle.done()


draw_scene() 