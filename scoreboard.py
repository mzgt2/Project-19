from turtle import Turtle


FONT = ('Arial', 14, 'normal')
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", move=False, align=ALIGN,font=FONT)
        self.hideturtle()


    def current_score(self):
        self.clear()
        self.score += 1
        self.goto(0,280)
        self.write(f"Score: {self.score}", move=False, align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
