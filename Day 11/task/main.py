import art
import random

def count_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 21

    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def check_ace(deck):
    card = draw_cards()
    score = count_score(deck)
    if card == 11 and score + card > 21:
        card = 1
    deck.append(card)
    return deck

def results(player_score, cpu_score):
    if player_score == cpu_score:
        return "It's a draw!"
    elif cpu_score == 21:
        return "Blackjack, you lose!"
    elif player_score == 21:
        return "Blackjack, you win!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif cpu_score > 21:
        return "Opponent went over. You win!"
    elif player_score > cpu_score:
        return "You win!"
    else:
        return "You lose!"

def final_scores(player, cpu, player_score, cpu_score):
    print(f"\tYour final hand: {player}, final score: {player_score}")
    print(f"\tComputer's final hand: {cpu}, final score: {cpu_score}")


def blackjack():
    print(art.logo)

    player_deck = []
    computer_deck = []
    player_score = 0
    computer_score = 0

    # Set up first 2 cards for both players
    for card in range(2):
        player_deck.append(draw_cards())
        computer_deck.append(draw_cards())


    player_turn = True
    while player_turn:

        player_score = count_score(player_deck)
        computer_score = count_score(computer_deck)
        print(f"\tYour cards: {player_deck}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_deck[0]}")

        #check for blackjack
        if computer_score == 21 or player_score == 21 or player_score > 21:
            player_turn = False
        else:
            # figure out how to loop when requesting another card
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                player_deck.append(draw_cards())
            else:
                player_turn = False

    while computer_score < 17:
        computer_deck.append(draw_cards())
        computer_score = count_score(computer_deck)

    final_scores(player_deck, computer_deck, player_score, computer_score)
    print(results(player_score, computer_score))



#play again? use calculator mechanics
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()
