from turtle import Turtle, Screen
import random
screen = Screen()
screen.bgcolor("Orange")
screen.screensize(600, 600)

midline = Turtle("square")
midline.hideturtle()
midline.penup()
midline.goto(0, -300)
midline.shapesize(600, 0.01)
midline.showturtle()


ball = Turtle("circle")
ball.penup()
ball.color("Blue")


INITIAL_ANGLE = [45, 135, 225, 315]
UPLIMIT = 290
DOWNLIMIT = -290
LEFTLIMIT = -290
RIGHTLIMIT = 290
STEP = 5

# ESTIMATION BALL'S ANGLE:


def move_ball(steps):
    ball.goto(0, 0)
    ball.setheading(random.choice(INITIAL_ANGLE))
    if INITIAL_ANGLE == 45:
        rebound_angle = 315
    elif INITIAL_ANGLE == 135:
        rebound_angle = 225
    elif INITIAL_ANGLE == 225:
        rebound_angle = 135
    else:
        rebound_angle = 45
    for steps in range(1, steps):
        ball.forward(STEP)


move_ball(50)


screen.exitonclick()
