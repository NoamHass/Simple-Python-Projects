from turtle import Turtle
WIDTH = 20
HEIGHT = 100
STARTING_POSITION_R = (350,0)
STARTING_POSITION_L = (-350, 0)
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, paddle_side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        if(paddle_side == "r"):
            self.goto(STARTING_POSITION_R)
        else:
            self.goto(STARTING_POSITION_L)
    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)
    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() + -20)

