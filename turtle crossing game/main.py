import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.onkey(player.go_up,'w')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.mov_cars()
    for car in car_manager.all_car:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()