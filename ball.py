from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.last_loose = ""
        self.go_pos = [-5, 5]
        self.def_position = (0, 0)
        self.penup()
        self.shape('square')
        self.color('white')
        self.startx_coord = random.choice(self.go_pos)
        self.starty_coord = random.choice(self.go_pos)

    def rand_position(self):
        self.goto(0, random.randint(-150, 150))
        self.random_move()

    def random_move(self):
        if self.last_loose == "player1":
            self.startx_coord = 5
            self.starty_coord = random.choice([-5, 5])
        elif self.last_loose == "player2":
            self.startx_coord = -5
            self.starty_coord = random.choice([-5, 5])
        else:
            self.startx_coord = random.choice(self.go_pos)
            self.starty_coord = random.choice(self.go_pos)

    def move(self):
        self.goto(self.xcor() + self.startx_coord, self.ycor() + self.starty_coord)