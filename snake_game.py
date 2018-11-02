import turtle
import time
import random

delay = 0.1
#creating a screen

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("LightGreen")
screen.setup(width=800, height=600)
screen.tracer(0) # turns of animations

#Creating the head of the snake

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color('DarkGreen')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("red")
food.penup()
food.goto(0,100)

segment = [] # list representing body

#functions

def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_right():
    head.direction = 'right'

def go_left():
    head.direction = 'left'

#keyboard bindings

screen.listen()
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 'x')
screen.onkeypress(go_right, 'd')
screen.onkeypress(go_left, 'a')

def moving():

    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


# main game loop

while True:
    screen.update()

    if head.distance(food) < 20: # collided
        #move the food to a random place
        x = random.randint(-290, 290) # so it doesn't go off the screen
        y = random.randint(-290, 290)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.shape('circle')
        new_segment.color('green')
        new_segment.penup()
        segment.append(new_segment)

    # moving the segments
    length = len(segment)
    for index in range((length) -1, 0, -1):
        x = segment[index - 1 ].xcor()
        y = segment[index -1 ].ycor()
        segment[index].goto(x, y)
    # move segment 0 to the head

    if length > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
    moving()

    time.sleep(delay)

screen.mainloop()