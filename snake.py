from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]  # Head of the snake

    def createSnake(self):
        # Prepare the starting snake
        for position in START_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def extend(self):
        self.addSegment(self.segments[-1].position())  # Adds new segment to the position of the last segment

    def move(self):
        # for loop that controls the automatic movements of each snake piece
        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # start at last position (snake length -1), stop at zeroth position
            # get (x, y) of the second to last segment
            newX = self.segments[seg_num - 1].xcor()
            newY = self.segments[seg_num - 1].ycor()
            # and getting last segment to go to the position of the second to last segment
            self.segments[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)  # first segment moves 20 paces

    def up(self):
        # If conditions to prevent instantaneous reverse directions
        if self.head.heading() != DOWN:  # If snake is not facing south, it can go up
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # If snake is not facing north, it can go down
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # If snake is not facing east, it can go west
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # If snake is not facing west, it can go east
            self.head.setheading(RIGHT)
