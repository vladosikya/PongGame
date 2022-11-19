class Collision():
    def __init__(self, ball, player1, player2):
        self.ball = ball
        self.player1 = player1
        self.player2 = player2

    def wall_collision(self):
        if self.ball.ycor() >= 250 or self.ball.ycor() <= -250:
            self.ball.starty_coord = -self.ball.starty_coord

    def players_collision(self):
        for block in self.player1.rocket:
            if self.ball.xcor() <= -230 and self.ball.distance(block) <= 25:
                self.ball.startx_coord *=-1
                break
        for block in self.player2.rocket:
            if self.ball.xcor() >= 230 and self.ball.distance(block) <= 25:
                self.ball.startx_coord *=-1
                break

    def lose_collision(self, score):
        if self.ball.xcor() >= 350:
            score.player1_score +=1
            self.ball.last_loose = "player2"
            return True
        elif self.ball.xcor() <= -350:
            score.player2_score +=1
            self.ball.last_loose = "player1"
            return True
        else:
            return False

