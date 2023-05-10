from turtle import Turtle

FRONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(-280, 250)
        self.create_level()

    def create_level(self):
        self.write(f"level : {self.level}", align="left", font=FRONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.create_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font= FRONT)