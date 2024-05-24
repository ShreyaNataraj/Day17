from random import randint

EASY_LEVEL_RETURNS = 10
HARD_LEVEL_RETURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print("You have won the game!")
        return turns

def set_difficulty():
    level = input("Choose a difficulty level ('easy' or 'hard'): ").lower()
    if level == "easy":
        return EASY_LEVEL_RETURNS
    else:
        return HARD_LEVEL_RETURNS

def game():
    print("Welcome to the number guessing game!")   
    print("Think of a number between 1 and 100.")   
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You have run out of attempts. The game is over.")
            print(f"The correct answer was {answer}.")
            break
        elif guess != answer:
            print("Guess again.")

game()
