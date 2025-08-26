from turtle import Turtle
import random
class BigFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(1000,2000)        
    def makefood(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
        
        
