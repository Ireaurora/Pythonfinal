import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
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
head.color("Dark Green")
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


pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = 'center', font=("Arial", 25, "normal"))
#functions

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
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

    #stops collisions with the screen

    if head.xcor()>290 or head.xcor() <-290 or head.ycor()>290  or  head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"


        # hide segments
        for segmenti in segment:
            segmenti.goto(2000,2000)

        segment.clear()

        score =  0

        delay = 0.1

        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align='center',
                  font=("Arial", 25, "normal"))

    if head.distance(food) < 20: # collided
        #move the food to a random place
        x = random.randint(-290, 290) # so it doesn't go off the screen
        y = random.randint(-290, 290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.shape('circle')
        new_segment.color("#"  + str(random.randint(100000, 999999)))
        new_segment.penup()
        segment.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align = 'center', font=("Arial", 25, "normal"))

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

    # body collisions

    for segmenti in segment:
        if segmenti.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segmenti in segment:
                segmenti.goto(2000, 2000)

            segment.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align='center',
                      font=("Arial", 25, "normal"))

    time.sleep(delay)

screen.mainloop()