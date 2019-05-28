""" Binocle
Binocle.py
Emily B
24/05/2019 """

import pygame
from random import *

playFor3 = True

#Insert a ML Algorithm that is trained at different levels plz

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Lady Luck"     #Miraculous Ladybug
        self.cardHand = []
        self.lead = False		#First to play a card
        self.deal = False		#Dealer
        self.bidFirst = False		#Bids for the cards first
        self.playGame = False		#Highest bidder plays the game
        self.meldPoints = 0		#Add points to score
        self.tricks = [	]	#Keeps track of cards won to count points at end
        self.wonLastTrick = False	#Winner leads next hand
        self.durch = False		#Playing a durch
        self.score = 0			#Overall score

        self.trumpCount = 0		#Counting for computer
        self.cardDisplay = [    ]	#All cards on table/played
        self.cardDisplayComp1 = [    ]	#All cards on table/played by computer1
        self.cardDisplayComp2 = [    ]	#All cards on table/played by computer2
        self.cardDisplayHuman = [    ]	#All cards on table/played by user
    def update(self):
        #update cardHand, tricks, wonLastTrick and score
        print ("meow") #because

class Card(pygame.sprite.Sprite):
    def __init__(self,suit,val,num,name="KD"):
        pygame.sprite.Sprite.__init__(self)
        self.suit = suit
        self.pointValue = val
        self.number = num
        self.name = name

def drawCard(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

def deal3(deck,P1,P2,P3):
    bidPile=[]
    bidPile.append(drawCard(deck))
    bidPile.append(drawCard(deck))
    bidPile.append(drawCard(deck))
    while(len(deck)>0):
        P1.cardHand.append(drawCard(deck))  #human player
        P2.cardHand.append(drawCard(deck))
        P3.cardHand.append(drawCard(deck))
    return bidPile
    
def sortThird(val): 
    return val.number 

def game():
    #this is where we make a deck
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    AS1 = Card(suits[0],11,1,"AS")      #Ace of Spades
    deck.append(AS1)
    AS2 = Card(suits[0],11,2,"AS")
    deck.append(AS2)
    TS1 = Card(suits[0],10,3,"TS")
    deck.append(TS1)
    TS2 = Card(suits[0],10,4,"TS")
    deck.append(TS2)
    KS1 = Card(suits[0],4,5,"KS")
    deck.append(KS1)
    KS2 = Card(suits[0],4,6,"KS")
    deck.append(KS2)
    OS1 = Card(suits[0],3,7,"OS")
    deck.append(OS1)
    OS2 = Card(suits[0],3,8,"OS")
    deck.append(OS2)
    US1 = Card(suits[0],2,9,"US")
    deck.append(US1)
    US2 = Card(suits[0],2,10,"US")
    deck.append(US2)
    VS1 = Card(suits[0],0,11,"VS")
    deck.append(VS1)
    VS2 = Card(suits[0],0,12,"VS")
    deck.append(VS2)

    AD1 = Card(suits[3],11,13,"AD")
    deck.append(AD1)
    AD2 = Card(suits[3],11,14,"AD")
    deck.append(AD2)
    TD1 = Card(suits[3],10,15,"TD")
    deck.append(TD1)
    TD2 = Card(suits[3],10,16,"TD")
    deck.append(TD2)
    KD1 = Card(suits[3],4,17,"KD")
    deck.append(KD1)
    KD2 = Card(suits[3],4,18,"KD")
    deck.append(KD2)
    OD1 = Card(suits[3],3,19,"OD")
    deck.append(OD1)
    OD2 = Card(suits[3],3,20,"OD")
    deck.append(OD2)
    UD1 = Card(suits[3],2,21,"UD")
    deck.append(UD1)
    UD2 = Card(suits[3],2,22,"UD")
    deck.append(UD2)
    VD1 = Card(suits[3],0,23,"VD")
    deck.append(VD1)
    VD2 = Card(suits[3],0,24,"VD")
    deck.append(VD2)

    AH1 = Card(suits[1],11,25,"AH")
    deck.append(AH1)
    AH2 = Card(suits[1],11,26,"AH")
    deck.append(AH2)
    TH1 = Card(suits[1],10,27,"TH")
    deck.append(TH1)
    TH2 = Card(suits[1],10,28,"TH")
    deck.append(TH2)
    KH1 = Card(suits[1],4,29,"KH")
    deck.append(KH1)
    KH2 = Card(suits[1],4,30,"KH")
    deck.append(KH2)
    OH1 = Card(suits[1],3,31,"OH")
    deck.append(OH1)
    OH2 = Card(suits[1],3,32,"OH")
    deck.append(OH2)
    UH1 = Card(suits[1],2,33,"UH")
    deck.append(UH1)
    UH2 = Card(suits[1],2,34,"UH")
    deck.append(UH2)
    VH1 = Card(suits[1],0,35,"VH")
    deck.append(VH1)
    VH2 = Card(suits[1],0,36,"VH")
    deck.append(VH2)
    
    AC1 = Card(suits[2],11,37,"AC")
    deck.append(AC1)
    AC2 = Card(suits[2],11,38,"AC")
    deck.append(AC2)
    TC1 = Card(suits[2],10,39,"TC")
    deck.append(TC1)
    TC2 = Card(suits[2],10,40,"TC")
    deck.append(TC2)
    KC1 = Card(suits[2],4,41,"KC")
    deck.append(KC1)
    KC2 = Card(suits[2],4,42,"KC")
    deck.append(KC2)
    OC1 = Card(suits[2],3,43,"OC")
    deck.append(OC1)
    OC2 = Card(suits[2],3,44,"OC")
    deck.append(OC2)
    UC1 = Card(suits[2],2,45,"UC")
    deck.append(UC1)
    UC2 = Card(suits[2],2,46,"UC")
    deck.append(UC2)
    VC1 = Card(suits[2],0,47,"VC")
    deck.append(VC1)
    VC2 = Card(suits[2],0,48,"VC")
    deck.append(VC2)
    inits = False
    deck2 = deck
    players = []
    playPile = []
    bidPile=[]
    handPointH = 0
    handPoint1 = 0
    handPoint2 = 0
    minPoints = 40
    Human = Player()
    Comp1 = Player()
    Comp2 = Player()
    inits = True
    #somehow in here y'all need to write a function that allows game to be played as games are played
    #like right about here is good
    #while (Human.score<1500 and Comp1.score<1500 and Comp2<1500):
        #play another round
        #figure out stuff
    if playFor3:
        minPoints = 40
        Human.deal = True
        Comp1.lead = True
        Comp2.bidFirst = True
        players = [Human, Comp1, Comp2]
        bidPile = deal3(deck2,Human,Comp1,Comp2)
        
    Human.cardHand.sort(key=sortThird)
    Human.cardHand.sort(key=sortThird)
    for i in Human.cardHand:
        print (i.name)
        handPointH+=i.pointValue
    print (handPointH, " points in hand")

    for i in Comp1.cardHand:
        handPoint1+=i.pointValue
    if handPoint1<minPoints:
        print ("Please reshuffle or play durch")
    for i in Comp2.cardHand:
        handPoint2+=i.pointValue
    if handPoint2<minPoints:
        print ("Please reshuffle or play durch")

    keywords = ["toss", "durch", "up", "weg", "vec","veck","wec"]

    print("\n")
    print ("At this point we need to insert a bidding function\nCurrent bid is 200")
    bet = 200
    myBet = input("How high?  ")
    if myBet in keywords:
        Comp2.playGame = True
    elif int(myBet)>bet:
        bet = myBet
        Human.playGame = True
    else:
        Comp2.playGame = True
    print ("The highest bid is ", bet, "\n")
    print ("The bid pile; ")
    for i in bidPile:
        print (i.name)
    if Human.playGame:
        trump = input("What is trump?  ")
        while not trump in suits:
            trump = input("What is trump? Spades, Hearts, Clubs, Diamonds:  ")
    else:
        trump = suits[randint(0,len(suits)-1)]
    print ("Trump is ", trump, "\n")

    
    #this is where the meld begins. Ideally the user will have to see themselves what their cards are worth
    #Also ideally would be if I would be able to move this function out. sigh.
    for i in players:
        points = 0
        #meld for 'of a kind's
        if AS1 in i.cardHand and AS2 in i.cardHand and AH1 in i.cardHand and AH2 in i.cardHand and AD1 in i.cardHand and AD2 in i.cardHand and AC1 in i.cardHand and AC2 in i.cardHand:
            points += 1000
            print ("1000 Aces")
        elif (AS1 in i.cardHand or AS2 in i.cardHand) and (AH1 in i.cardHand or AH2 in i.cardHand) and (AD1 in i.cardHand or AD2 in i.cardHand) and (AC1 in i.cardHand or AC2 in i.cardHand):
            points += 100
            print ("100 Aces")
        if TS1 in i.cardHand and TS2 in i.cardHand and TH1 in i.cardHand and TH2 in i.cardHand and TD1 in i.cardHand and TD2 in i.cardHand and TC1 in i.cardHand and TC2 in i.cardHand:
            points += 1000
            print ("1000 Tens")
        if KS1 in i.cardHand and KS2 in i.cardHand and KH1 in i.cardHand and KH2 in i.cardHand and KD1 in i.cardHand and KD2 in i.cardHand and KC1 in i.cardHand and KC2 in i.cardHand:
            points += 1000
            print ("1000 Kings")
        elif (KS1 in i.cardHand or KS2 in i.cardHand) and (KH1 in i.cardHand or KH2 in i.cardHand) and (KD1 in i.cardHand or KD2 in i.cardHand) and (KC1 in i.cardHand or KC2 in i.cardHand):
            points += 80
            print ("80 Kings")
        if OS1 in i.cardHand and OS2 in i.cardHand and OH1 in i.cardHand and OH2 in i.cardHand and OD1 in i.cardHand and OD2 in i.cardHand and OC1 in i.cardHand and OC2 in i.cardHand:
            points += 1000
            print ("1000 Queens")
        elif (OS1 in i.cardHand or OS2 in i.cardHand) and (OH1 in i.cardHand or OH2 in i.cardHand) and (OD1 in i.cardHand or OD2 in i.cardHand) and (OC1 in i.cardHand or OC2 in i.cardHand):
            points += 60
            print ("60 Queens")
        if US1 in i.cardHand and US2 in i.cardHand and UH1 in i.cardHand and UH2 in i.cardHand and UD1 in i.cardHand and UD2 in i.cardHand and UC1 in i.cardHand and UC2 in i.cardHand:
            points += 1000
            print ("1000 Johns")
        elif (US1 in i.cardHand or US2 in i.cardHand) and (UH1 in i.cardHand or UH2 in i.cardHand) and (UD1 in i.cardHand or UD2 in i.cardHand) and (UC1 in i.cardHand or UC2 in i.cardHand):
            points += 40
            print ("40 Johns")
        if VS1 in i.cardHand and VS2 in i.cardHand and VH1 in i.cardHand and VH2 in i.cardHand and VD1 in i.cardHand and VD2 in i.cardHand and VC1 in i.cardHand and VC2 in i.cardHand:
            points += 1000
            print ("1000 Sevens")
        
        #meld for family heirarchy
        if AS1 in i.cardHand and AS2 in i.cardHand and TS1 in i.cardHand and TS2 in i.cardHand and KS1 in i.cardHand and KS2 in i.cardHand and OS1 in i.cardHand and OS2 in i.cardHand and US1 in i.cardHand and US2 in i.cardHand:
            points+=200
            print ("Double Spade family")
            if trump == suits[0]:
                points +=100
                print ("of trump")
        elif (AS1 in i.cardHand or AS2 in i.cardHand) and (TS1 in i.cardHand or TS2 in i.cardHand) and (KS1 in i.cardHand or KS2 in i.cardHand) and (OS1 in i.cardHand or OS2 in i.cardHand) and (US1 in i.cardHand or US2 in i.cardHand):
            points+=100
            print ("Spade family")
            if trump == suits[0]:
                points +=50
                print ("of trump")
            if KS1 in i.cardHand and KS2 in i.cardHand and OS1 in i.cardHand and OS2 in i.cardHand:
                points +=20
                print("and double spade king queen")
                if trump == suits[0]:
                    points +=20
                    print ("of trump")
        elif KS1 in i.cardHand and KS2 in i.cardHand and OS1 in i.cardHand and OS2 in i.cardHand:
            points +=40
            print("double spade king queen")
            if trump == suits[0]:
                points +=40
                print ("of trump")
        elif (KS1 in i.cardHand or KS2 in i.cardHand) and (OS1 in i.cardHand or OS2 in i.cardHand):
            points +=20
            print("spade king queen")
            if trump == suits[0]:
                points +=20
                print ("of trump")

        if AH1 in i.cardHand and AH2 in i.cardHand and TH1 in i.cardHand and TH2 in i.cardHand and KH1 in i.cardHand and KH2 in i.cardHand and OH1 in i.cardHand and OH2 in i.cardHand and UH1 in i.cardHand and UH2 in i.cardHand:
            points+=200
            print ("Double Heart family")
            if trump == suits[1]:
                points +=100
                print ("of trump")
        elif (AH1 in i.cardHand or AH2 in i.cardHand) and (TH1 in i.cardHand or TH2 in i.cardHand) and (KH1 in i.cardHand or KH2 in i.cardHand) and (OH1 in i.cardHand or OH2 in i.cardHand) and (UH1 in i.cardHand or UH2 in i.cardHand):
            points+=100
            print ("Heart family")
            if trump == suits[1]:
                points +=50
                print ("of trump")
            if KH1 in i.cardHand and KH2 in i.cardHand and OH1 in i.cardHand and OH2 in i.cardHand:
                points +=20
                print("and double heart king queen")
                if trump == suits[1]:
                    points +=20
                    print ("of trump")
        elif KH1 in i.cardHand and KH2 in i.cardHand and OH1 in i.cardHand and OH2 in i.cardHand:
            points +=40
            print("double heart king queen")
            if trump == suits[1]:
                points +=40
                print ("of trump")
        elif (KH1 in i.cardHand or KH2 in i.cardHand) and (OH1 in i.cardHand or OH2 in i.cardHand):
            points +=20
            print("heart king queen")
            if trump == suits[1]:
                points +=20
                print ("of trump")

        if AC1 in i.cardHand and AC2 in i.cardHand and TC1 in i.cardHand and TC2 in i.cardHand and KC1 in i.cardHand and KC2 in i.cardHand and OC1 in i.cardHand and OC2 in i.cardHand and UC1 in i.cardHand and UC2 in i.cardHand:
            points+=200
            print ("Double Club family")
            if trump == suits[2]:
                points +=100
                print ("of trump")
        elif (AC1 in i.cardHand or AC2 in i.cardHand) and (TC1 in i.cardHand or TC2 in i.cardHand) and (KC1 in i.cardHand or KC2 in i.cardHand) and (OC1 in i.cardHand or OC2 in i.cardHand) and (UC1 in i.cardHand or UC2 in i.cardHand):
            points+=100
            print ("Club family")
            if trump == suits[2]:
                points +=50
                print ("of trump")
            if KC1 in i.cardHand and KC2 in i.cardHand and OC1 in i.cardHand and OC2 in i.cardHand:
                points +=20
                print("and double club king queen")
                if trump == suits[2]:
                    points +=20
                    print ("of trump")
        elif KC1 in i.cardHand and KC2 in i.cardHand and OC1 in i.cardHand and OC2 in i.cardHand:
            points +=40
            print("double club king queen")
            if trump == suits[2]:
                points +=40
                print ("of trump")
        elif (KC1 in i.cardHand or KC2 in i.cardHand) and (OC1 in i.cardHand or OC2 in i.cardHand):
            points +=20
            print("club king queen")
            if trump == suits[2]:
                points +=20
                print ("of trump")

        if AD1 in i.cardHand and AD2 in i.cardHand and TD1 in i.cardHand and TD2 in i.cardHand and KD1 in i.cardHand and KD2 in i.cardHand and OD1 in i.cardHand and OD2 in i.cardHand and UD1 in i.cardHand and UD2 in i.cardHand:
            points+=200
            print ("Double Diamond family")
            if trump == suits[3]:
                points +=100
                print ("of trump")
        elif (AD1 in i.cardHand or AD2 in i.cardHand) and (TD1 in i.cardHand or TD2 in i.cardHand) and (KD1 in i.cardHand or KD2 in i.cardHand) and (OD1 in i.cardHand or OD2 in i.cardHand) and (UD1 in i.cardHand or UD2 in i.cardHand):
            points+=100
            print ("Diamond family")
            if trump == suits[3]:
                points +=50
                print ("of trump")
            if KD1 in i.cardHand and KD2 in i.cardHand and OD1 in i.cardHand and OD2 in i.cardHand:
                points +=20
                print("and double diamond king queen")
                if trump == suits[3]:
                    points +=20
                    print ("of trump")
        elif KD1 in i.cardHand and KD2 in i.cardHand and OD1 in i.cardHand and OD2 in i.cardHand:
            points +=40
            print("double diamond king queen")
            if trump == suits[3]:
                points +=40
                print ("of trump")
        elif (KD1 in i.cardHand or KD2 in i.cardHand) and (OD1 in i.cardHand or OD2 in i.cardHand):
            points +=20
            print("diamond king queen")
            if trump == suits[3]:
                points +=20
                print ("of trump")

        if OS1 in i.cardHand and OS2 in i.cardHand and UD1 in i.cardHand and UD2 in i.cardHand:
            points +=300
            print ("Binochle!!")
        elif (OS1 in i.cardHand or OS2 in i.cardHand) and (UD1 in i.cardHand or UD2 in i.cardHand):
            points +=40
            print ("Half binochle")

        if VS1 in i.cardHand and trump == suits[0]:
            points += 10
            print ("7 o trump")
        if VS2 in i.cardHand and trump == suits[0]:
            points += 10
            print ("7 o trump")
        if VH1 in i.cardHand and trump == suits[1]:
            points += 10
            print ("7 o trump")
        if VH2 in i.cardHand and trump == suits[1]:
            points += 10
            print ("7 o trump")
        if VC1 in i.cardHand and trump == suits[2]:
            points += 10
            print ("7 o trump")
        if VC2 in i.cardHand and trump == suits[2]:
            points += 10
            print ("7 o trump")
        if VD1 in i.cardHand and trump == suits[3]:
            points += 10
            print ("7 o trump")
        if VD2 in i.cardHand and trump == suits[3]:
            points += 10
            print ("7 o trump")

        i.meldPoints = points
        print (i, points, "\n")
        
    play3()

    #so the play begins
    b=0
    potentialCard = []

    while len(Human.cardHand)>0:
        print ("\n")
        for i in players:
            if i.wonLastTrick == True:
                b = players.index(i)
                i.wonLastTrick = False
                break
            elif i.lead:#if a person starts
                b = players.index(i)#how does?
        for i in range(len(players)):
            if (b+i)%len(players) ==0:
                while True:
                    cardName = input(" - ")
                    for x in players[0].cardHand:
                        if x.name == cardName:      #FIX ME
                            card = players[0].cardHand.pop(index(x)) #If card in hand get that card outta there
                            break

            elif len(playPile)<1:
                #randomly pulls card from hand
                card = drawCard(players[(i+b)%len(players)].cardHand)
                print (card.name)
                playPile.append(card)    #make this do something
            else:
                #randomly pulls card from hand
                for card in players[(i+b)%len(players)].cardHand:
                    if card.suit == playPile[0].suit:
                        potentialCard.append(card)

                if len(potentialCard)==0:
                    for card in players[(i+b)%len(players)].cardHand:
                        if card.suit == trump:
                            potentialCard.append(card)
                if len(potentialCard)==0:
                    card = drawCard(players[(i+b)%len(players)].cardHand)
                else:
                    card = drawCard(potentialCard)
                print (card.name)
                playPile.append(card)
                #potentialCard = []
                #check if card on pile, compare to cards you have, play accordingly
        
        n=playPile[0]   #the card with the standards    
        for m in playPile:
            if m.pointValue<n.pointValue and m.suit == n.suit:
                n=m
            elif m.suit == trump and n.suit != trump:
                n=m
        d=playPile.index(n)
        #add playPile to winner's trick hand stuff
        for i in playPile:
            players[(d+b)%len(players)].tricks.append(i)
            playPile = []
        players[(d+b)%len(players)].wonLastTrick = True
    
    #after it all       (currently only does the one person...)
    for h in players:
        print ("\n")
        trickPoints = 0
        if h.wonLastTrick:
            trickPoints += 10
        for j in h.tricks:
            print (j.pointValue)
            trickPoints += j.pointValue
        trickPoints=round(trickPoints/10)*10
        if h.playGame and (trickPoints + h.meldPoints)<bet:
            h.score -= bet
        else:
            h.score += trickPoints
            h.score += h.meldPoints
        h.meldPoints = 0
        h.tricks = []
        print (" Someone is at ", h.score, " points")       #help after
        


def play3():
    print ("loooool wut u doin")
    #print (len(Human.cardHand))
    #while len(Human.cardHand)>0:



if __name__ == "__main__":
    game()


