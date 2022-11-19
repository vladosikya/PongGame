import turtle
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.player1_scr = turtle.Turtle()
        self.player1_scr.hideturtle()
        self.player2_scr = turtle.Turtle()
        self.player2_scr.hideturtle()
        self.reset_score()

    def line_screen(self):
        self.penup()
        self.setheading(90)
        self.goto(0, 250)
        self.pencolor('white')
        self.pensize(3)
        self.pendown()
        while self.ycor() > -250:
            self.back(10)
            self.penup()
            self.back(10)
            self.pendown()

    def reset_score(self):
        self.player2_scr.clear()
        self.player1_scr.clear()
        self.player1_scr = turtle.Turtle()
        self.player2_scr = turtle.Turtle()
        self.player1_scr.penup()
        self.player2_scr.penup()
        self.player1_scr.hideturtle()
        self.player2_scr.hideturtle()
        self.player1_scr.color('white')
        self.player2_scr.color('white')
        self.player1_scr.goto(-50, 220)
        self.player2_scr.goto(50, 220)
        self.player1_scr.write(arg=self.player1_score, align='center', font=('Arial', 45, 'normal'))
        self.player2_scr.write(arg=self.player2_score, align='center', font=('Arial', 45, 'normal'))