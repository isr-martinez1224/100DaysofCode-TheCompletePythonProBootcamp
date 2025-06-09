import art
print(art.logo)

names_dictionary = {}
entering_names = True
while entering_names:

    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    # TODO-2: Save data into dictionary {name: price}
    names_dictionary[name] = bid
    # TODO-3: Whether if new bids need to be added
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.")
    if yes_or_no.lower() == 'no':
        entering_names = False
    else:
        print("\n" * 20)
# TODO-4: Compare bids in dictionary
bid = 0
winner = ""
for key in names_dictionary:
    if bid < names_dictionary[key]:
        winner = key
        bid = names_dictionary[key]

print(f"The winner is {winner} with a bid of ${names_dictionary[winner]}")

