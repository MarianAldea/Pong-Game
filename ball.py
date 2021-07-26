from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
        self.semn_y = 1
        self.semn_x = 1


    def ball_movement(self):
        x_coor = self.xcor() + self.semn_x*13
        y_coor = self.ycor() + self.semn_y*10
        self.speed("slowest")
        self.setx(x_coor)
        self.sety(y_coor)



    def bounce_y(self):
        self.semn_y = self.semn_y* -1
        print(self.semn_y)

    def bounce_x(self):
        self.semn_x = self.semn_x * -1

    def reset_x(self):
        self.setx(0)
        self.sety(0)
        self.semn_x = self.semn_x * -1