# import colorgram
# colors = colorgram.extract('image.jpg', 20)

# rgb_color=[]
# # def color(colors):
# for _ in range(20):
#     rgb=colors[_].rgb
#     rgb_color.append((rgb[0],rgb[1],rgb[2]))
    
# print(rgb_color)    
from turtle import Turtle, Screen,colormode, penup, right
import random
colormode(255)
color_list=[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]


tim=Turtle()
tim.hideturtle() 
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.setheading(0)


for __ in range(10):
    for _ in range(10):
        tim.dot(10,random.choice(color_list))
        tim.penup()
        tim.forward(40)
        tim.pendown()

    tim.penup()
    tim.setheading(90)
    tim.forward(40)
    tim.setheading(180)
    tim.forward(400)
    tim.setheading(0)
    tim.pendown()

  
    
    
screen=Screen()
screen.exitonclick()