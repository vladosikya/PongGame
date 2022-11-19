import turtle
from turtle import Turtle

class Rocket():
    def __init__(self, coord):
        self.rocket = []
        self.coord = coord
        for _ in range(3):
            block = turtle.Turtle()
            block.shape('square')
            block.color('white')
            block.penup()
            block.setheading(90)
            block.goto(coord)
            self.coord[1] +=20
            self.rocket.append(block)

    def controller_up(self):
        if self.rocket[2].ycor() >= 250:
            pass
        else:
            for block in self.rocket:
                block.forward(10)

    def controller_down(self):
        if self.rocket[0].ycor() <= -250:
            pass
        else:
            for block in self.rocket:
                block.back(10)

