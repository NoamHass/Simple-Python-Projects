from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle("r")
l_paddle = Paddle("l")
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    #Detect collision with walls
    if ball.detect_collision():
        ball.bounce_y()
    ball.move()

    #Detect collision with right panel
    if ball.distance(r_paddle) < 50 and ball.xcor() == 340 or ball.distance(l_paddle) < 50 and ball.xcor() == -340:
        ball.bounce_x()

    #Detect if R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()