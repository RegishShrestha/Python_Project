from turtle import Turtle, Screen, colormode
import random

colormode(255)
def random_color():
    r=random.randint(0,255)    
    g=random.randint(0,255)   
    b=random.randint(0,255)   
    return (r,g,b)

tim=Turtle()

tim.speed('fastest')
tim.shape('turtle')

# using right direction
# for _ in range(900):
#     tim.left(_)
#     tim.circle(100)

def draw_spirograph(size_of_graph):
    
    for _ in range(360//size_of_graph):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_graph)

draw_spirograph(5)

screen=Screen()
screen.exitonclick()