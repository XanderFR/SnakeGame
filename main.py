from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# The Snake Game GUI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns off automatic screen updates

snake = Snake()
food = Food()
scoreBoard = Scoreboard()

screen.listen()  # Gets screen to listen for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)  # screen updates every 0.1 second
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Food appears in a new random location
        snake.extend()
        scoreBoard.increaseScore()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        gameOn = False
        scoreBoard.gameOver()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Ensures that snake head doesn't trigger tail collision condition
        if snake.head.distance(segment) < 10:  # Snake head collides with a tail segment
            gameOn = False
            scoreBoard.gameOver()

screen.exitonclick()

