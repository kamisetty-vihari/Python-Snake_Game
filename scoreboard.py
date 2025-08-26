from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(r"C:\Users\nikun\Desktop\project\snake game\snakedata.txt") as file:
            self.highscore=int(file.read().strip())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.score} HighScore:{self.highscore}",align="center",font=("Arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open(r"C:\Users\nikun\Desktop\project\snake game\snakedata.txt","w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()
        
        
'''
    def gameend(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",24,"normal"))
'''
    