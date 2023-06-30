from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        xcor = coordinates[0]
        ycor = coordinates[1]
        self.shape("square")
        self.color("purple")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, ycor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





