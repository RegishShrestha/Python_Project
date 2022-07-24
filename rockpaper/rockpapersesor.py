import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

all=[rock,paper,scissors]
value=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp_value=random.randint(0,2)

#0-rock
#1-peper
#2-scissors

#conditions to follow 
#0<1
#1<2
#2<0
real_val=value-comp_value
if(value<0 or value>2):
    print("Invalid Number entered")
elif(real_val==0):
  print(f"Your Choose: {all[value]} \n Computer Choose: {all[comp_value]} \n Its Draw")
elif((real_val==-1 and value!=1 and value!=0) or(real_val==2 and value!=2) or real_val==1 or real_val==-2):
  print(f"{all[value]} \n Computer Choose: {all[comp_value]} /n You Win")
else:
  print(f"{all[value]} \n Computer Choose: {all[comp_value]} /n You Lose")
  
# https://github.com/RegishShrestha/Rockpaperscissor.git

  # git remote add origin https://github.com/RegishShrestha/Rockpaperscissor.git
  # git branch -M main
  # git push -u origin main

