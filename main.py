from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard
from game_boundry import Game_Boundry
tim_segments = []
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
game_boundry = Game_Boundry()
game_on = True
while game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    
    screen.listen()
    screen.onkey(fun=snake.move_up, key='Up')
    screen.onkey(fun=snake.move_down, key='Down')
    screen.onkey(fun=snake.move_left, key='Left')
    screen.onkey(fun=snake.move_right, key='Right')
    if snake.head.distance(food)<10:
        snake.extend()
        score.clear()
        food.refresh()
        score.score += 1
        score.update_score()
    if snake.head.xcor() > 260 or snake.head.ycor() > 260 or\
        snake.head.xcor() < -260 or snake.head.ycor() < -260:
        game_on = False
        score.game_over()
        score.wall_hit()
    for segment in snake.tim_segments[1:]:
        if snake.head.distance(segment)<5:
            game_on = False
            score.game_over()
            score.tail_hit()
        

screen.exitonclick()
