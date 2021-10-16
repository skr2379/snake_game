from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")
FONT1 = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(0,270)
        self.penup()
        self.write(f"score : {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over",align = ALIGNMENT, font = FONT)
    def wall_hit(self):
        self.goto(0, -20)
        self.write(f"avoid walls",align = ALIGNMENT, font = FONT1)
    def tail_hit(self):
        self.goto(0, -20)
        self.write(f"avoid eating tail",align = ALIGNMENT, font = FONT1)


            
