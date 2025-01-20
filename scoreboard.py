from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score=0
        self.penup()
        with open('data/highscore', 'r') as file:
            highscore=file.read()
            self.highscore=int(highscore)
        self.show_score()
        self.show_highscore()

    def show_score(self):

        self.goto(-250,250)

        self.write(f'Score:{self.score}',font=('Arial',20,'normal'))

    def show_highscore(self):

        self.goto(120, 250)

        self.write(f'Highscore:{self.highscore}', font=('Arial', 20, 'normal'))

    def gameover(self):
        self.color('black')
        self.goto(0,50)
        self.write(f'GAMEOVER',align='center',font=('Arial', 24, 'bold'))

