from art import logo
import random
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks the guess against answer and returns the turns remaining."""
    if guess > answer:
        print("Too high !")
        return turns - 1
    elif guess < answer:
        print("Too low !")
        return turns - 1
    else:
        print(f"You got it ! The answer was {answer}.")


def set_difficulty():
    level = input("Choose difficulty .Type 'easy' or 'hard' :").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    if level == "hard":
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game !")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    # print(f"The number you are going to guess is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Guess a number :"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose !")
            return
        elif guess != answer:
            print("Guess again !")


game()

# returning functions can do a great job (See the check_answer function)
