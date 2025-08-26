from snake import Snake
from food import Food
from turtle import Screen,Turtle
from scoreboard import ScoreBoard
from bigfood import BigFood
import time
score=0
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
sb=ScoreBoard()
bf=BigFood()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

temp=0
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect the collision with the food
    
    if snake.head.distance(food) <15:
        print ("num mom nom")
        food.makefood()
        snake.extend_segment()
        sb.increase_score()
        temp+=1
    if temp==5:
        bf.makefood()
        temp=0
        #eating big food
    if snake.head.distance(bf) <20:
        bf.goto(1000,2000)
        for _ in range (3):
            sb.increase_score()
            snake.extend_segment()
        
        
        
        
        
    #detect collision with walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295 :
        
        sb.reset()
        snake.reset()
        bf.goto(1000,2000)
        temp=0
        screen.update()
        
    #detect the collision with the tail
    for segment in snake.segments:
        if snake.head==segment:
            pass
        elif snake.head.distance(segment)<=5:
            print("ate body")
            sb.reset()
            snake.reset()
            screen.update()
            
screen.exitonclick()