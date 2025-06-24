from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
SCORE_HEIGHT = 370


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle cursor
        self.color("white")  # Set the scoreboard text color
        self.goto(0, SCORE_HEIGHT)  # Move the scoreboard to the top of the screen
        self.update_scoreboard()


    def update_scoreboard(self):
        """Update the score and refresh the display."""
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
