from turtle import Turtle
positions = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.tim_segments = []
        self.create_snake()
        self.head = self.tim_segments[0]

    def create_snake(self):
        for i in range(3):
            self.tim = Turtle(shape='square')
            self.tim.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.tim.color('white')
            self.tim.penup()
            self.tim.goto(positions[i])
            self.tim_segments.append(self.tim)
            
    def move(self):
        for i in range(len(self.tim_segments)-1, 0, -1):
            new_x = self.tim_segments[i-1].xcor()
            new_y = self.tim_segments[i-1].ycor()
            self.tim_segments[i].goto(new_x, new_y)
        self.head.forward(10)
        
    def extend(self):
        self.tim = Turtle(shape='square')
        self.tim.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.tim.color('white')
        self.tim.penup()
        self.tim.goto(self.tim_segments[-1].position())
        self.tim_segments.append(self.tim)
        
        
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
