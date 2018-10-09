import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()




def what_shape():
    shape = str(input("What shape should I draw?"))
    repetition = int(input("How many should I draw?"))
    increase = 10
    length = 10
    if shape == "Square" and repetition <= 100:
        for n in range(repetition):
            draw_square(-length / 2, length / 2, length)
            length = length + increase
    elif shape == "Circle" and repetition <= 100:
        for n in range(repetition):
            draw_circle(-length / 2, length / 2, length)
    elif shape == "Triangle" and repetition <= 100:
        for n in range(repetition):
            draw_equilatertriangle(-length / 2, length / 2, length)
    elif shape == "Pentagon" and repetition <= 100:
        for n in range(repetition):
            draw_pentagon(-length / 2, length / 2, length)
    else:
        print("I can't draw that yet, sorry")


def draw_square(start_x, start_y, size):
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

    for i in range(4):
        my_turtle.forward(size)
        my_turtle.right(90)

    my_turtle.penup()


def draw_circle(start_x, start_y, size):
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

    for i in range(100):
        my_turtle.circle(10 + i, 45)

def draw_equilatertriangle(start_x, start_y, size):
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

    for i in range(3):
        my_turtle.forward(size)
        my_turtle.right(60)

    my_turtle.penup()

def draw_pentagon(start_x, start_y, size):
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

    for i in range(5):
        my_turtle.forward(size)
        my_turtle.right(108)

    my_turtle.penup()

what_shape()

## Must be the last line of code
my_turtle.screen.exitonclick()

