from turtle import Screen, Turtle
import time
# Constants
START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """A class to represent the Snake in the game."""

    def __init__(self):
        """Initialize the snake by creating its segments and setting the head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with 3 starting segments."""
        for segment_position in START_COORDINATES:
            self.add_segment(segment_position)

    def add_segment(self, segment_position):
        """Add a segment at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(segment_position)
        self.segments.append(new_segment)

    def reset_segments(self):
        for seg in self.segments:
            seg.goto(6000,6000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Add a segment to the snake at the last segment's position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by shifting the positions of its segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Set the snake's direction to up unless it's moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set the snake's direction to down unless it's moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set the snake's direction to left unless it's moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set the snake's direction to right unless it's moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)