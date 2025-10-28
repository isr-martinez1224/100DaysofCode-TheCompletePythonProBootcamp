import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()

game_is_on = True
car = CarManager()
#this car manager is showing another turtle which effects the logic
#solution: passed Turtle through class added another one, removed it
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.add_car()
    car.move_cars()

    #check for crash
    for x in car.all_cars:
        if player.distance(x) < 20:
            game_is_on = False
            scoreboard.game_over()

    #check for finish line and reset
    if player.cross_finish():
        scoreboard.increase_level()
        car.increase_speed()
        player.reset()


screen.exitonclick()