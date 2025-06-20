MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Print report
#  When the user enters “report” to the prompt, a report should be generated that shows
#  the current resource values. e.g.

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# Make Coffee.
#   If the transaction is successful and there are enough resources to make the drink the
#   user selected, then the ingredients to make the drink should be deducted from the
#   coffee machine resources.
#   E.g. report before purchasing latte:
#   Water: 300ml
#   Milk: 200ml
#   Coffee: 100g
#   Money: $0
#   Report after purchasing latte:
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

#each drink takes in money and returns change
def espresso():
    resources["water"] -= 50
    resources["coffee"] -= 18
    print("Here is your espresso ☕. Enjoy!")

def latte():
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    print("Here is your latte ☕. Enjoy!")

def cappuccino():
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    print("Here is your cappuccino ☕. Enjoy!")

# Check resources sufficient?
#   When the user chooses a drink, the program should check if there are enough
#   resources to make that drink.
#   E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#   not continue to make the drink but print: “Sorry there is not enough water.”
#   The same should happen if another resource is depleted, e.g. milk or coffee

def check_resources(drink):
    if drink == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < 18:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    elif drink == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    elif drink == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    else:
        return None

# Process coins.
#   If there are sufficient resources to make the drink selected, then the program should
#   prompt the user to insert coins.
#   Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#   pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# Check transaction successful?
#   Check that the user has inserted enough money to purchase the drink they selected.
#   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#   program should say “Sorry that's not enough money. Money refunded.”.
#   But if the user has inserted enough money, then the cost of the drink gets added to the
#   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

def get_money():
    print("--Please insert coins--")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    return (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)


# Turn off the Coffee Machine by entering “
#  off” to the prompt. Ends program execution through secret word

def coffee_machine():
    on = True
    while on:
        #make_coffee = False
        # Prompt user by asking “
        #  What would you like? (espresso/latte/cappuccino)”
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice.lower() == "report":
            report()
            make_coffee = False
        elif choice.lower() == "off":
            on = False
            make_coffee = False
        elif choice.lower() == "espresso" or choice.lower() == "latte" or choice.lower() == "cappuccino":
            make_coffee = check_resources(choice.lower())
        else:
            print("Sorry, you entered an invalid choice! Please pick one of our options")
            make_coffee = False

        if make_coffee:
            money = get_money()

            if money < 1.50:
                print("Sorry, that's not enough money. Money refunded")
            else:
                #change = 0
                if choice.lower() == "espresso":
                    if money > 1.50:
                        change = money - 1.50
                        change = round(change, 2)
                        print(f"Here is ${change} in change.")
                    resources["money"] += 1.50
                    espresso()
                elif choice.lower() == "latte":
                    if money > 2.50:
                        change = money - 2.50
                        change = round(change, 2)
                        print(f"Here is ${change} in change.")
                    resources["money"] += 2.50
                    latte()
                elif choice.lower() == "cappuccino":
                    if money > 3.00:
                        change = money - 3.00
                        change = round(change, 2)
                        print(f"Here is ${change} in change.")
                    resources["money"] += 3.00
                    cappuccino()

coffee_machine()