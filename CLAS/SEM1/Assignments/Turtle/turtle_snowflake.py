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


class Snowflake:
    # Variables to control the position of the snowflake
    flake_x = 0
    flake_y = 0

    @staticmethod
    def draw_arm():
        """Draw a single arm of the snowflake."""
        mark.forward(30)
        mark.backward(10)
        mark.left(45)
        mark.forward(10)
        mark.backward(10)
        mark.right(90)
        mark.forward(10)
        mark.backward(10)
        mark.left(45)
        mark.backward(20)

    @staticmethod
    def draw():
        """Draw the complete snowflake at the specified position."""
        mark.penup()
        mark.goto(Snowflake.flake_x, Snowflake.flake_y)
        mark.setheading(0)
        mark.pendown()

        # Randomize snowflake color
        colors = ["white", "light blue", "cyan", "silver"]
        mark.pencolor(random.choice(colors))
        mark.pensize(2)

        for _ in range(8):  # Snowflakes typically have 6 or 8 arms
            Snowflake.draw_arm()
            mark.right(45)  # Turn 45 degrees for 8 arms (360/8)


for i in range(5):
    Snowflake.flake_x = random.randint(-200, 200)
    Snowflake.flake_y = random.randint(-200, 200)
    Snowflake.draw()

turtle.done()