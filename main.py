import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

game_is_on = True

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")

screen.onkeypress(player2.up, "w")
screen.onkeypress(player2.down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball past paddle
    if ball.xcor() > 380:   # past p1 on right
        ball.reset_ball()
        score.p2_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.p1_point()

    if score.score_p1 >= 5 or score.score_p2 >= 5:
        score.goto(0, 0)
        score.write("GAME OVER", align="Center", font=("courier", 50, "normal"))
        game_is_on = False


screen.exitonclick()
