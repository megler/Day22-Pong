from turtle import Turtle


class Scoreboard(Turtle):
    """Create a scoreboard"""

    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self) -> None:
        """Display scoreboard"""
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
        """Add point to left player"""
        self.l_score += 1
        self.update_score()

    def r_point(self) -> None:
        """Add point to right player"""
        self.r_score += 1
        self.update_score()
