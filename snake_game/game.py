import sys
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorboard import Scoreboard, ALTONMENT, FONT

def stop_game():
    global game_is_on
    game_is_on = False
    snake.beyond_screen()
    food.color("black")
    stop = Turtle()
    stop.hideturtle()
    stop.color("white")
    stop.write("GAME OVER.",align="center", font=("Courier", 20, "normal"))
    screen.update()
    time.sleep(3)
    sys.exit()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "q")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)
    snake.move()

    # Detect callisium with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_is_on = False
        snake.reset()
        scoreboard.reset()

    # detect collision head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()