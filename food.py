from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a random position on the grid."""
        random_x = random.randrange(-280, 280, 20)  # Step of 20
        random_y = random.randrange(-280, 280, 20)  # Step of 20
        self.goto(x=random_x, y=random_y)
