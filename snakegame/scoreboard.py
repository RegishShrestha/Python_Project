from distutils.file_util import move_file
from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            gh_score=int(data.read())
            self.high_score=gh_score
            
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()
        
        
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()