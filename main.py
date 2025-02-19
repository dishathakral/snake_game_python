from turtle import Screen
import snake
import time
import food
import scoreboard
my_screen=Screen()
my_screen.screensize(600,600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)
# turtle.shapesize(stretch_len=3,stretch_wid=1)
snake1=snake.Snake()
snake1.create_snake()
food=food.Food()
score=scoreboard.Score()
my_screen.listen()
my_screen.onkeypress(snake1.up, "Up")
my_screen.onkeypress(snake1.down, "Down")
my_screen.onkeypress(snake1.left, "Left")
my_screen.onkeypress(snake1.right, "Right")
game_on=True
speed=0.1  #initial speed
while game_on:
    my_screen.update()
    time.sleep(speed)
    snake1.move()
    if food.distance(snake1.t_list[0])<15:#collison with food
        food.food_location()
        score.increase_score()
        speed *= 0.95
        snake1.grow()
    #collison with wall
    if snake1.collision_with_wall():
        score.game_over()
        break
    #collision with tail
    # if snake1.no_turtles > 3:
    #     for segment in snake1.t_list[1:]:
    #         if snake1.t_list[0].distance(segment) < 10:
    #             score.game_over()
    #             game_on = False  # 🚀 Stop the loop
    #             break


my_screen.exitonclick()
