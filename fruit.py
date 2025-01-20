from turtle import Turtle
import random

class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.x=random.randint(-200,180)
        self.y=random.randint(-20,180)
        self.goto(self.x,self.y)





