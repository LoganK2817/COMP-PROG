import turtle

 

# Shared side length for all shapes
shape_length = 50

def display_keybinds():
    # Position the turtle at the top and hide it to display keybindings
    mark.penup()
    mark.goto(-200, 250)  # Position text at the top of the screen
    mark.hideturtle()
    mark.write("Keybinds:\n"
               "W: Up, S: Down, A: Left, D: Right\n"
               "C: Circle, V: Square, B: Triangle, N: Hexagon\n"
               "[ : Decrease size, ] : Increase size\n"
               "X: Exit", align="left", font=("Arial", 24, "normal"))
    mark.goto(0, 0)  # Return the turtle to the center position
    mark.showturtle()
    mark.pendown()

def get_turtle_position():
    x, y = turtle.position()
    return x, y


class shapes:
    def circle():
        # Save position and heading
        mark.pencolor("yellow")
        x, y = mark.position()
        heading = mark.heading()
        
        mark.circle(shape_length)  # Use shape_length as the radius

        # Return to saved position and heading
        mark.penup()
        mark.goto(x, y)
        mark.setheading(heading)
        mark.pendown()

    def square():
        x, y = mark.position()
        heading = mark.heading()
        
        for i in range(2):
            mark.pencolor("blue")
            mark.forward(shape_length)
            mark.left(90)
            mark.pencolor("red")
            mark.forward(shape_length)
            mark.left(90)
        
        mark.penup()
        mark.goto(x, y)
        mark.setheading(heading)
        mark.pendown()

    def triangle():
        x, y = mark.position()
        heading = mark.heading()
        
        for i in range(2):
            mark.pencolor("blue")
            mark.forward(shape_length)
            mark.left(120)
            mark.pencolor("red")
            mark.forward(shape_length)
            mark.left(120)
        
        mark.penup()
        mark.goto(x, y)
        mark.setheading(heading)
        mark.pendown()

    def hexagon():
        x, y = mark.position()
        heading = mark.heading()
        
        for i in range(3):
            mark.pencolor("blue")
            mark.forward(shape_length)
            mark.left(60)
            mark.pencolor("red")
            mark.forward(shape_length)
            mark.left(60)
        
        mark.penup()
        mark.goto(x, y)
        mark.setheading(heading)
        mark.pendown()


class movement:
    def up(dist):
        x, y = mark.position()
        mark.penup()
        mark.setposition(x, y + dist)
        mark.pendown()
        
    def down(dist):
        x, y = mark.position()
        mark.penup()
        mark.setposition(x, y - dist)
        mark.pendown()

    def left(dist):
        x, y = mark.position()
        mark.penup()
        mark.setposition(x - dist, y)
        mark.pendown()

    def right(dist):
        x, y = mark.position()
        mark.penup()
        mark.setposition(x + dist, y)
        mark.pendown()


def increase_shape_size():
    global shape_length
    shape_length += 10
    print(f"Shape length increased to {shape_length}")


def decrease_shape_size():
    global shape_length
    shape_length = max(10, shape_length - 10)
    print(f"Shape length decreased to {shape_length}")


mark = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")

mark.shape("turtle")
mark.color("black")
mark.speed(6)
mark.pensize(10)

# Display keybindings at the top of the screen
display_keybinds()

turtle.listen()

# Bind movement keys
turtle.onkey(lambda: movement.up(20), "w")
turtle.onkey(lambda: movement.down(20), "s")
turtle.onkey(lambda: movement.left(20), "a")
turtle.onkey(lambda: movement.right(20), "d")

# Bind shape drawing keys
turtle.onkey(shapes.circle, "c")
turtle.onkey(shapes.square, "v")
turtle.onkey(shapes.triangle, "b")
turtle.onkey(shapes.hexagon, "n")

# Bind keys to adjust shared shape size
turtle.onkey(increase_shape_size, "]")  # Increase shape length with "]"
turtle.onkey(decrease_shape_size, "[")  # Decrease shape length with "["

# Bind the "x" key to close the program
turtle.onkey(turtle.bye, "x")

turtle.done()
