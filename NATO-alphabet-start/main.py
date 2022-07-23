import pandas

# with open("nato_phonetic_alphabet.csv") as data:
#     data_list=data.readlines()
# print(data_list)
datas=pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict={row.letter: row.code for (index,row) in datas.iterrows()}


answer=input("Enter the name: ")
answer_lower=list((str(answer)).upper())
answer_list=[data_dict[letter] for letter in answer_lower ]
print(answer_list)