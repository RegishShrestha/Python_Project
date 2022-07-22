
from os import stat
import turtle
from click import prompt
import pandas



screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
n=0
new_state=[]
while n<=50:
    
    answer_state=screen.textinput(title=f"{n}/50 States Correct",prompt="What's  another state name? ")
    
    data=pandas.read_csv("50_states.csv")
    data_list=data.state.to_list()
    answer_lower=(str(answer_state)).lower()
    if answer_state=='exit':
        missing_states=[states for states in data_list if states not in new_state]
        # missing_states=[]
        # for states in data_list:
        #     if states not in new_state:
        #         missing_states.append(states)
        print(missing_states)
        break
    if answer_lower in(str(data_list)).lower():
        new_state.append(answer_state)
        n+=1
        state_data=data[data.state==answer_state]
        # print(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.color('black')
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(f'{state_data.state.item()}')
     
        


 