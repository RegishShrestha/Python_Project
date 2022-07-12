import random
from art import logo

chances = 0
# actual_answer stores the random number between 1 and 100
actual_answer = random.randint(1, 100)
print(actual_answer)
# answer stores the answer taken from user
answer = 0

# checks the difficult level


def check_difficulty(difficulty):
    global chances
    if difficulty == "easy":
        chances = 10
    elif difficulty == 'hard':
        chances = 5
    else:
        print("You typed wrong input!!!")

# checks the answer is equal to actual_answer or not


def check_answer(actual_answer, answer, chances):
    # This while loop runs until the chances are 0 or if the correct answer is matched
    while(chances > 0):
        print(f"You have {chances} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        if answer == actual_answer:
            print(f"You got it! The answer was {actual_answer}.")
            chances = 0
        elif(answer < actual_answer):
            print("Too low")
            chances -= 1
        elif(answer > actual_answer):
            print("Too high.")
            chances -= 1

        if chances > 0:
            print("Guess again")
        elif chances <= 0 and answer != actual_answer:
            print("You've run out of guesses, you lose.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # difficulty is the variable that takes easy or hard input from user and stores it
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    check_difficulty(difficulty)
    check_answer(actual_answer, answer, chances)


game()
