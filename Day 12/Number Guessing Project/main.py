import art
import random

def compare_guess(guess, correct_number, lives):
    if guess < correct_number and lives != 0:
        print("Too low, try again!")
    elif guess > correct_number and lives != 0:
        print("Too high, try again!")

def intro():
    print(art.logo2)
    print("Welcome to Guess The Number!")
    print("I'm thinking of a number between 1 and 100.")

def difficulty():
    choice = ""
    while choice.lower() != "easy" or choice.lower() != "hard":
        choice = input("Choose a difficulty - Type 'easy' or 'hard': ")
        if choice.lower() == "easy":
            return 10
        elif choice.lower() == "hard":
            return 5
        else:
            print("You entered an invalid input!")
    return None

def game():
    intro()
    lives = difficulty()
    correct_number = random.randint(1, 100)

    game_over = False
    while not game_over:
        if lives <= 0:
            game_over = True
            print(f"You have run out of guesses. The answer was {correct_number}. Run the file again to play again")
        else:
            print(f"You have {lives} attempts left to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == correct_number:
                print(f"You guessed right! The answer was {correct_number}")
                game_over = True
            else:
                lives -= 1
                compare_guess(guess, correct_number, lives)



#Play the game
game()