from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 1200
HEIGHT = 1200

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_counter = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#   Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        snake.extend()
        food.refresh()
        score_counter.increase_score()


#   Detect collisions with wall
    QUADRANT_WIDTH = 580

    if (snake.head.xcor() > QUADRANT_WIDTH or
            snake.head.xcor() < -1*QUADRANT_WIDTH or
            snake.head.ycor() > QUADRANT_WIDTH or
            snake.head.ycor() < -1*QUADRANT_WIDTH):
        score_counter.reset_scoreboard()
        snake.reset_segments()

    #   Detect collisions with tail
#     if head collides with any segment of the tail
#     trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_counter.reset_scoreboard()
            snake.reset_segments()

screen.exitonclick()
