import random
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    choice = input("Choose a difficulty type, Easy 'y' or Hard 'h',.")
    if choice == 'y':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess, answer, turns):
    if guess > answer:
        print('Number ia too big!')
        return turns-1
    elif guess < answer:
        print('Number is too small')
        return turns-1
    else:
        print(f"You got the answer, it was {answer}")

def mainGame():
    print(art.logo)

    answer = random.randint(1, 100)
    guess = 0
    turns = set_difficulty()

    while guess != answer:
        print(f"You have {turns} turns remaining to guess the number.")

        guess = int(input("Guess the number!"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You Lost!")
            return
        elif guess != answer:
            print("Guess again!")
