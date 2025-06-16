import art
import game_data
import random

#Get game data for account
def get_data(person):
    data = random.choice(game_data.data)
    #Make sure it is not the same person
    while person == data["name"]:
        print(data)
        data = random.choice(game_data.data)

    return data

#compare accounts to see who has more
def compare(person1, person2):
    followers_a = person1["follower_count"]
    followers_b = person2["follower_count"]

    if followers_a > followers_b:
        return person1["name"]
    else:
        return person2["name"]

def game():
    # Program starts with art, Compare A, vs, Compare B
    print(art.logo)
    score = 0

    #get data of both accounts
    person1 = get_data("")
    person2 = get_data(person1)

    game_over = False
    while not game_over:
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
        print(art.vs)
        print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        while guess.lower() != 'a' and guess.lower() != 'b':
            #check for invalid input
            guess = input("Sorry you entered an invalid answer! Type 'A' or 'B': ")

        #check who has more based on choice
        correct_answer = compare(person1, person2)

        #check if player got it right
        if guess.lower() == 'a' and correct_answer == person1["name"]:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            person2 = get_data(person1)
        elif guess.lower() == "b" and correct_answer == person2["name"]:
            score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            person1 = person2
            person2 = get_data(person1)
        else:
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


#Once the player guesses wrong, game ends and program ends. They will need to run again so no looping game
game()