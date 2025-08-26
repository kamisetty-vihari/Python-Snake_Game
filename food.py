from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(10)
        self.makefood()
    def makefood(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
    
        
        
