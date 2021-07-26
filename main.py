from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
game_is_on = True
screen = Screen()
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Game of Pong")
left_paddle = Paddle(-340,0)
right_paddle = Paddle(340,0)
ball_speed = 0.1
ball = Ball()
score_right = 0
score_left = 0
screen.listen()
scoreboard = Scoreboard()
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
while game_is_on:
    screen.update()
    ball.ball_movement()
    time.sleep(ball_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball_speed -= 0.002
    if ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        ball_speed -= 0.002
    if ball.xcor() > 360:
        ball.reset_x()
        scoreboard.l_point()
        time.sleep(1)
        ball_speed = 0.1
    if ball.xcor() < -360:
        ball.reset_x()
        scoreboard.r_point()
        time.sleep(1)
        ball_speed = 0.1
    print(ball_speed)







screen.exitonclick()