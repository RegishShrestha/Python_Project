from termios import PARODD
from turtle import Turtle, Screen, time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_segment()  
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
        
    for segment in snake.segment[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()


# with open("my_file.txt", mode="a") as file:
#     # conteents=file.read()
#     file.write("\nHeY HEY HEY")
#     # print(conteents)