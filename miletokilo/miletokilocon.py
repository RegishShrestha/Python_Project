from tkinter import *

window=Tk()
window.minsize(width=200,height=200)
window.title("Mile to Km Conerter")
window.config(padx=30,pady=30)



def action():
    value=input.get()
    value_km=float(value)*1.6
    second_label.config(text=f"{value_km}")


input=Entry(width=10)
input.grid(column=1,row=0)
# input.config(padx=10,pady=10)

label=Label(text="Miles")
label.grid(column=3,row=0)
# label.config(padx=20,pady=20)

first_label=Label(text="is equal to")
first_label.grid(column=0,row=1)
# first_label.config(padx=20,pady=20)


second_label=Label(text="0")
second_label.grid(column=1,row=1)
# second_label.config(padx=20,pady=20)

third_label=Label(text="Km")
third_label.grid(column=3,row=1)
# second_label.config(padx=20,pady=20)



button=Button(text="Calculate",command=action)
button.grid(column=1,row=2)


window.mainloop()