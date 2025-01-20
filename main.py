import time
from turtle import Turtle,Screen
from bar import Bar
from fruit import Fruit
from scoreboard import Scoreboard
import random
screen=Screen()
screen.tracer(0)
turtle=Turtle()
bar=Bar()
fruit=Fruit()
scoreboard=Scoreboard()

image='data/images/tree.gif'

screen.addshape(image)
turtle.shape(image)

screen.setup(600,600)
screen.bgcolor('sea green')
screen.setup(width=600,height=600)
screen.listen()
screen.onkey(key='Left',fun=bar.left)
screen.onkey(key='Right',fun=bar.right)

screen.tracer(0)

a=0
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.06)


    if fruit.ycor() <=-245 and fruit.distance(bar)<=50 :
        fruit.clear()
        fruit.goto(1000,1000)
        fruit=Fruit()
        scoreboard.score+=1
        scoreboard.clear()
        scoreboard.show_score()
        scoreboard.show_highscore()

    elif fruit.ycor() <=-275:
        fruit.clear()
        fruit.goto(1000, 1000)
        scoreboard.gameover()
        if scoreboard.score>scoreboard.highscore:
            scoreboard.highscore=scoreboard.score
            with open('data/highscore', 'w') as file:
                file.write(f'{scoreboard.highscore}')
        ask=screen.textinput(title='Continue',prompt='Play Again? Y or N').lower()
        screen.listen()
        if ask=='y':
            fruit = Fruit()
            scoreboard.color('white')
            scoreboard.score=0
            scoreboard.clear()
            scoreboard.show_score()
            scoreboard.show_highscore()

        else:
            game_is_on=False


    a=10
    fruit.y-=a


    fruit.goto(fruit.x, fruit.y)


