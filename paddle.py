from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x_coord = x
        self.y_coord = y
        self.segment_list = []
        self.build_paddle()

    def build_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=self.x_coord, y=self.y_coord)
        self.setheading(90)

    def paddle_up(self):
        if self.ycor() <= 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

