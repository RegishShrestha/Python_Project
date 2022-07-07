# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_low=name1.lower()
name2_low=name2.lower()

name_low=name1_low+name2_low

count_t=name_low.count('t')
count_r=name_low.count('r')
count_u=name_low.count('u')
count_e=name_low.count('e')
total_1=count_t+count_r+count_u+count_e

count_l=name_low.count('l')
count_o=name_low.count('o')
count_v=name_low.count('v')
count_e=name_low.count('e')
total_2=count_l+count_o+count_v+count_e

love_score=int(str(total_1)+str(total_2))
if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score>40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}")