#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    names=name_file.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        strip_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt",mode='w') as completed_letter:
            completed_letter.write(new_letter)