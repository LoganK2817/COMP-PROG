"""
Student Name: Logan Kunz
Class: Computer Programming 1
Period: B6
Project 1: The Barbie Movie
"""
import turtle
import math


#customizable Vars
square_color = "black"
first_tri_color = ["red", "#530c99"]
second_tri_color = ["blue","#068f61"]
rows_num = 4
colum_num = 4


#turtle set up
mark = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("pink")
mark.shape("turtle")
mark.color("black")
mark.speed(100)
mark.pensize(5)

class Shapes:
    def make_square():
        mark.penup()


        #basic parameters 
        mark.pendown()
        mark.pencolor(square_color)
        mark.fillcolor(square_color)
        mark.begin_fill()
        
        # making the square it self
        for i in range(4):
            mark.forward(40)
            mark.left(90)
        mark.end_fill()
        mark.setheading(0)

    def make_triangle_one(fill_color):
        mark.penup()


        #basic parameters
        mark.pendown()
        mark.pencolor(fill_color)
        mark.fillcolor(fill_color)
        mark.begin_fill()

        saved_triangle_corner = 0,0




        #making the triangle it self
        mark.forward(40)
        saved_triangle_corner = mark.xcor(),mark.ycor()
        mark.backward(40)
        mark.right(90)
        mark.forward(40)
        mark.goto(saved_triangle_corner)
        mark.end_fill()
        mark.setheading(0)
        
    def make_triangle_two(fill_color):
        mark.penup()


        mark.setheading(-90)
        mark.pendown()
        mark.pencolor(fill_color)
        mark.fillcolor(fill_color)
        mark.begin_fill()

        saved_triangle_corner = 0,0


        #making triangle
        saved_triangle_corner = mark.xcor(),mark.ycor()
        mark.forward(40)
        mark.right(90)
        mark.forward(40)
        mark.goto(saved_triangle_corner)
        mark.end_fill()
        mark.setheading(0)

    def make_unit_box():
        mark.pencolor("#8f0686")
        mark.left(90)
        mark.forward(40)
        mark.left(90)
        for i in range(3):
            mark.forward(80)
            mark.left(90)
        mark.forward(40)

        mark.setheading(0)



def next_row():
    mark.penup()
    mark.goto(0,mark.ycor()-80)

def make_unit():
    for i in range(2):
        if i == 0:
            color1 = first_tri_color[0]
            color2 = second_tri_color[0]
        else:
            color1 = first_tri_color[1]
            color2 = second_tri_color[1]
        Shapes.make_square()
        Shapes.make_triangle_one(color1)
        Shapes.make_triangle_two(color2)
    
    Shapes.make_unit_box()



for i in range(colum_num):
    for h in range(rows_num):
        make_unit()
    next_row()

turtle.done()