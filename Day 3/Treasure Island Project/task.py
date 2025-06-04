print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a split path with a left and right direction. Which way do you want to go?")
choice1 = input('\tType "left" or "right"\n').lower()

if not choice1 == "left":
    print("Fall off a cliff. Game Over.")

print("You've come to a lava river. There is a creaky bridge and an old rope to get across. Which one do you choose?")
choice2 = input('\tType "bridge" to walk across the bridge. Type "rope" to swing across.\n').lower()

if not choice2 == "rope":
    print("The bridge breaks below you. Game Over.")

print("You arrive at the island unharmed. There is a house with 3 doors.")
choice3 = input('\tOne red, one yellow, and one blue. Which color do you choose?\n').lower()

if choice3 == "yellow":
    print("You found the treasure! You win!")
elif choice3 == "red":
    print("Transported to a bottomless pit. Game Over.")
elif choice3 == "blue":
    print("Trapped with the dragon. Game Over.")
else:
    print("Game Over.")