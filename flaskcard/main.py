
from tkinter import *
from matplotlib import image
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records",index=False)
else:    
    to_learn=data.to_dict(orient='records')


def flip_card():
    canvas.itemconfig(card_backround,image=card_back_img)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_backround,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)
    
    
def is_known():
    to_learn.remove(current_card)
    next_card()
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)



canvas=Canvas(height=526,width=800)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_backround=canvas.create_image(400,263,image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)



cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)


correct_image=PhotoImage(file="images/right.png")
known_button=Button(image=correct_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()


window.mainloop()