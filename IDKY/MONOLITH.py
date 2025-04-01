import turtle

mark = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
mark.shape("turtle")
mark.color("white")
mark.speed("fast")
mark.pensize(10)

class unit:
    
    height = 40
    width = 40
    color = ["white","orange","blue","purple"]
    x_offset = 40
    y_offset = 43
    
    
    @staticmethod
    def draw(width,height,x,y,color):
        mark.color(color)
        mark.setposition(x,y)
        mark.setheading(0)
        mark.pendown()
        mark.fillcolor(color)
        mark.begin_fill()
        
        for i in range(2):
            mark.forward(width)
            mark.left(90)
            mark.forward(height)
            mark.left(90)
        
        mark.end_fill()
        mark.setheading(90)
        mark.penup()

rows = 2
colums = 4

cubeSize = 4
cubed = 1

if cubed:
    rows = cubeSize
    colums = cubeSize
else:
    rows = rows
    colums = colums
    





y=0
for columNum in range(colums):
    x=0
    for rowNum in range(rows):
        
        unit.draw(unit.width,unit.height,x,y,unit.color[columNum])
        
        x += unit.x_offset
    
    y -= unit.y_offset
        
    

turtle.done()