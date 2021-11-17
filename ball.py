from turtle import Turtle


class Ball(Turtle):
    """Create ball object"""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self) -> None:
        """Move ball across the screen"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        """Detect collision along y axis and reverse course"""
        self.y_move *= -1

    def bounce_x(self) -> None:
        """Detect collision along x axis and reverse course"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self) -> None:
        """If ball leaves the screen, reset to home and give serve to opp player"""
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
