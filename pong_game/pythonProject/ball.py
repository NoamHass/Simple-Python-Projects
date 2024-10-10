from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.009

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def detect_collision(self):
        y = self.ycor()
        if y == 280 or y == -280:
            return True
        return False

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.009
        self.bounce_x()



