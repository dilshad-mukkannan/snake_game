from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 24, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'scoreboard: {self.score}',align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


