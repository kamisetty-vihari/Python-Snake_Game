from turtle import Turtle
cords=[(0,0),(0,-20),(0,-40)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for t in cords:#creating a initial snake
            self.add_segment(t)
    def add_segment(self,pos):
            new_t=Turtle()
            new_t.shape("square")
            new_t.color("white")
            new_t.penup()
            new_t.goto(pos)
            self.segments.append(new_t)
            
    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for segmet in range(len(self.segments)-1,0,-1):
            new_x=self.segments[segmet-1].xcor()
            new_y=self.segments[segmet-1].ycor()
            self.segments[segmet].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE) 
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for s in self.segments:
            s.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
        
        
            
    