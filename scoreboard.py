from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self) -> None:
        self.clear()
        self.goto(-100, 200)
        self.write(
            self.l_score, align="center", font=("Courier", 80, "normal")
        )
        self.goto(100, 200)
        self.write(
            self.r_score, align="center", font=("Courier", 80, "normal")
        )

    def l_point(self) -> None:
        self.l_score += 1
        self.update_score()

    def r_point(self) -> None:
        self.r_score += 1
        self.update_score()
