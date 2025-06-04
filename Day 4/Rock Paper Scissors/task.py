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

import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_int = int(input())
player_choice = ""


if player_int == 0:
    player_choice = rock
elif player_int == 1:
    player_choice = paper
elif player_int == 2:
    player_choice = scissors
else:
    print("You made an invalid choice")

print("\nPlayer chose:" + player_choice)


random_number = random.randint(0, 2)
cpu_choice = ""

if random_number == 0:
    cpu_choice = rock
elif random_number == 1:
    cpu_choice = paper
elif random_number == 2:
    cpu_choice = scissors
else:
    print("Computer made an invalid choice")

print("\nComputer chose:" + cpu_choice)


if player_choice == cpu_choice:
    print("It's a tie!")
elif (player_choice == rock and cpu_choice == scissors) or (player_choice == paper and cpu_choice == rock) or (player_choice == scissors and cpu_choice == paper):
    print("You win!")
else:
    print("Computer wins!")