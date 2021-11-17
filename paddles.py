from turtle import Turtle, Screen


class Paddle(Turtle):
    """Create a paddle and position on screen"""

    def __init__(self, posn: tuple) -> None:
        super().__init__()
        self.shape("square")
        self.screen = Screen()
        self.shapesize(1, 5, 0)
        self.color("White")
        self.penup()
        self.seth(90)
        self.goto(posn)

    def up(self) -> None:
        """Move paddle up"""
        self.forward(20)

    def down(self) -> None:
        """Move paddle down"""
        self.backward(20)

    def move_paddle(self, u: str, d: str) -> None:
        """Event listener to move paddle"""
        self.screen.listen()
        self.screen.onkeypress(self.up, u)
        self.screen.onkeypress(self.down, d)
