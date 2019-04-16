from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []
bid_pile = []
player1_cards = []
player2_cards = []
player3_cards = []

#card enum for playing cards
class Card(IntEnum):
    ACE = 11
    TEN = 10
    KING = 4
    QUEEN = 3
    JACK = 2
    SEVEN = 0

#suit enum for playing cards
class Suit(Enum):
    SPADES = "spades"
    HEARTS = "hearts"
    CLUBS = "clubs"
    DIAMONDS = "diamonds"

#class to hold info for playing cards
class PlayingCard():
    def __init__(self,card_value,card_suit,card_number):
        self.card = card_value
        self.suit = card_suit
        self.num = card_number

#functiong to deal full deck of cards
def create_deck():
    num = 1
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card),Suit(suit),num))
            num+=1
            full_deck.append(PlayingCard(Card(card),Suit(suit),num))
            num+=1
    return full_deck

# Draw a card from "deck"
def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

#deal 3 players and bid pile for Binochle
def deal_3player():
    bid_pile.append(draw_card(partial_deck))
    bid_pile.append(draw_card(partial_deck))
    bid_pile.append(draw_card(partial_deck))
    while(len(partial_deck)>0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))
        player3_cards.append(draw_card(partial_deck))

def sortThird(val): 
    return val.num 

create_deck()
partial_deck = list(full_deck)
deal_3player()



player3_cards.sort(key=sortThird)

for i in player3_cards:
    print (i.card, " ", i.suit, "     ", i.num)

"""
for i in range(0, len(player1_cards)):
    if (player)
"""
points=0
#I may have to use numbers
def meld(deck):
    if (PlayingCard.num == 5) in deck:
        print("huzzah")

#meld(player3_cards)
skipThis
if 8 cardVal in list: #for each card val
    points+=1000
#but needs to be different than the 8 card
if 4 different aces in list:
    points+=100
if 4 different kings in list:
    points +=80
if 4 different queens in list:
    points +=60
if 4 different jacks in list:
    points +=40

if 2 families of same in list:
    points+=200
    if trump.suit=family.suit:
        points+=100
elif 1 family in list:
    points +=100
    if trump


if 7 and 8 and 45 and 46 in list:
    points+=300
elif (7 or 8) and (45 or 46) in list:
    points +=40

if 2 7 of trump in list:
    points += 20
elif 1 7 of trump in list:
    points +=10


