from turtle import Turtle
class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.color('light green')
        self.shape('square')
        self.penup()
        self.goto(0,-270)
        self.turtlesize(stretch_len=5)


    def left(self):
        self.backward(20)

    def right(self):
        self.forward(20)
