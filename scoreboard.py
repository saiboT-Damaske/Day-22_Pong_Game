from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, -290)
        self.pendown()
        self.seth(90)
        while self.ycor() < 300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        self.penup()
        self.goto(-100, 200)
        self.write(self.score_p1, align="center", font=("Courier", 20, "normal"))
        self.goto(100, 200)
        self.write(self.score_p2, align="center", font=("Courier", 20, "normal"))

    def p1_point(self):
        self.score_p1 += 1
        self.update_score()

    def p2_point(self):
        self.score_p2 += 1
        self.update_score()