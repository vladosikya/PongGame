import turtle
from rocket import Rocket
from ball import Ball
from score import ScoreBoard
import time
from collision import Collision

screen = turtle.Screen()
screen.tracer(n=0)

screen.bgcolor('black')

ball = Ball()
score = ScoreBoard()
score.line_screen()
player2 = Rocket([250, 0])
player1 = Rocket([-250, 0])
collus = Collision(ball, player1, player2)
screen.update()

while True:
    screen.onkeypress(player1.controller_up, "w")
    screen.onkeypress(player1.controller_down, "s")

    screen.onkeypress(player2.controller_up, "Up")
    screen.onkeypress(player2.controller_down, "Down")

    ball.move()
    collus.wall_collision()
    collus.players_collision()
    if collus.lose_collision(score):
        score.reset_score()
        ball.goto(0, 0)
        screen.update()
        time.sleep(2)
        ball.rand_position()
        ball.random_move()

    time.sleep(0.05)
    screen.listen()
    screen.update()


screen.exitonclick()