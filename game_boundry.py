from turtle import Turtle, Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Game_Boundry:
    def __init__(self):
        self.tim = Turtle()
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=600, height=600)
        
        self.screen.tracer(0)
        self.draw_screen()
        
    def draw_screen(self):
        self.tim.penup()
        self.tim.goto(270,270)
        self.tim.pendown()
        self.tim.pensize(5)
        self.tim.pencolor('white')
        for i in range(4):
            self.tim.right(90)
            self.tim.forward(540)
            self.tim.hideturtle()
        self.screen.update()
        


