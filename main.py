# pongGame.py
#
# Python Bootcamp Day 22 - Pong Game
# Usage:
#      A demo of the game of Pong.
#
# Marceia Egler November 17, 2021


import operator
from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Draw Screen
X = 800
Y = 600
screen = Screen()
screen.screensize(X, Y, "black")
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()

# Player 1 Paddle
r_paddle = Paddle((350, 0))
r_paddle.move_paddle("Up", "Down")

# Player 2 Paddle
l_paddle = Paddle((-350, 0))
l_paddle.move_paddle("w", "s")

# Ball
ball = Ball()


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 50 and abs(a.ycor() - b.ycor()) < 50


game = True


while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Bounce off top or bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect if collision with paddle
    if is_collided_with(r_paddle, ball) or is_collided_with(l_paddle, ball):
        ball.bounce_x()

    # Detect if right ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # Detect if left ball goes out of bounds
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
