from lib2to3.pgen2.token import RIGHTSHIFT
from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
RIGHT=0
DOWN=270
LEFT=180

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
        
    def create_snake(self):    
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
        
    def extend_segment(self):
        self.add_segment(self.segment[-1].position())
        
        
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1 ):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)    

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)            
    
  
 
        
