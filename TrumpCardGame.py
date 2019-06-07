import random
import time

## creating trump cards for the game ##
class Card:
    def __init__(self, wrestler, height, weight, chest, biceps, rank):
        self.wrestler = wrestler
        self.height = height
        self.weight = weight
        self.chest = chest
        self.biceps = biceps
        self.rank = rank

trumpcards = []
trumpcards.append(Card("Hulk Hogan", 190, 269, 52, 19, 18))
trumpcards.append(Card("Big Show", 210, 323, 60, 26, 1))
trumpcards.append(Card("Batista", 191, 280, 51, 21, 13))
trumpcards.append(Card("Rock", 192, 280, 50, 22, 5))
trumpcards.append(Card("Triple H", 188, 300, 53, 20, 9))
trumpcards.append(Card("John Cena", 189, 290, 55, 24, 3))
trumpcards.append(Card("Randy Ortan", 195, 286, 47, 23, 6))
trumpcards.append(Card("Stone Cold", 186, 267, 46, 18, 20))
trumpcards.append(Card("Khalli", 205, 312, 58, 25, 2))
trumpcards.append(Card("Undertaker", 201, 305, 56, 27, 4))

random.shuffle(trumpcards)

player1Deck = []
player2Deck = []
outdatedDeck = []

## dealing cards among the players equally ##
while len(trumpcards) > 0:
    player1Deck.append(trumpcards.pop(0))
    player2Deck.append(trumpcards.pop(0))

## rolling dices to check who starts first ##
print("Card game between two entities: Player 1 and Player 2.")
print("Cards will be distributed equally among both players face down such that players cannot see the characters they have been given.")
print("Each player gets two special spells (God and Resurrect) which can only be used once by each player.")
startGame = input("Would you like to start the card game? Please enter 'yes' or 'no' to proceed.")
def rollDice():
    player1DiceResult=random.randint(1,6)
    player2DiceResult=random.randint(1,6)
    global playerTurn
    print("Player1 dice roll result is: " + str(player1DiceResult))
    print("Player2 dice roll result is: " + str(player2DiceResult))  
    if player1DiceResult>player2DiceResult:
        print("Player1 won the dice roll and will start first!")
        playerTurn = True
    elif player1DiceResult<player2DiceResult:
        print("Player2 won the dice roll and will start first!")
        playerTurn = False
    else:
        print("It's a tie. Roll again!")
        rollDice()
    
if (startGame == "yes" or startGame == 'YES'):
    print("Game begins, rolling the dice!")
    rollDice()
elif (startGame == "no" or startGame == 'NO'):
    print("Goodbye, please come again!")
    raise SystemExit
else:
    print("Input not recognized, please enter again!")
    

## starting the trump card game ##
acceptedResponses = ["a", "b", "c", "d", "e"]

    
godSpellPlayer1 = 0
godSpellPlayer2 = 0
resurrectSpellPlayer1 = 0
resurrectSpellPlayer2 = 0
player1Points = 0
player2Points = 0
rspell = "no"
rspell1 = "no"

while len(player1Deck) > 0 and len(player2Deck) > 0:
    
    time.sleep(1)

    if playerTurn == True:
        ## Resurrect Spell for Player1 ##
        ra = 0
        if (resurrectSpellPlayer1 == 0 and len(outdatedDeck) > 1 and ra == 0):
            rspell = input("Player1, would you like to play Resurrect Spell? Please answer: ‘yes’ or ‘no’")
            if (rspell == "yes" and resurrectSpellPlayer1 == 0):
                z1 = random.randint(1,len(outdatedDeck))
                player1Card = outdatedDeck.pop(int(z1)-1)
                outdatedDeck.append(player1Card)
                resurrectSpellPlayer1 = 1
                ra = 1
            else:
                player1Card = player1Deck.pop(0)
                outdatedDeck.append(player1Card)

        else:
            player1Card = player1Deck.pop(0)
            outdatedDeck.append(player1Card)

            
        print("Player1’s current card:")
        print("Wrestler Name:", player1Card.wrestler)
        print("a. Height:", player1Card.height)
        print("b. Weight:", player1Card.weight)
        print("c. Chest:", player1Card.chest)
        print("d. Biceps:", player1Card.biceps)
        print("e. Rank:", player1Card.rank)
        answer = input("Player1, which characteristic would you choose?")
        
        while acceptedResponses.count(answer) == 0:
            answer = input("That isn't a valid input, please try again: ")
        #player1 god spell
        if (godSpellPlayer1 == 0  and len(player2Deck) > 1 and ra == 0):
            gspell = input("Player1, would you like to play God Spell? Please answer: ‘yes’ or ‘no’")
            if (gspell == "yes" and godSpellPlayer1 == 0):
                godSpellPlayer1 = 1
                lec = len(player2Deck)
                print("No of cards in Player2’s deck:", lec)
                cardno = input("Which card should Player2 play with?")
                if (resurrectSpellPlayer2 == 0 and len(outdatedDeck) > 1):
                    rspell1 = input("Player2, would you like to play Resurrect Spell? Please answer: ‘yes’ or ‘no’")
                    if (rspell1 == "yes" and resurrectSpellPlayer2 == 0):
                        z2 = random.randint(1,len(outdatedDeck))
                        mn = outdatedDeck.pop(int(z2)-1)
                        player2Deck.insert(0,mn)
                        choice = input("Player1: a. Force resurrected card or b. Force earlier choice ")
                        if (choice == "a"):
                            player2Card = player2Deck.pop(0)
                            outdatedDeck.append(player2Card)
                            resurrectSpellPlayer2 = 1
                        else:    
                            player2Card = player2Deck.pop(int(cardno)-1)
                            outdatedDeck.append(player2Card)
                            resurrectSpellPlayer2 = 1
                    else:
                        player2Card = player2Deck.pop(int(cardno)-1)
                        outdatedDeck.append(player2Card)
                else:
                    player2Card = player2Deck.pop(int(cardno)-1)
                    outdatedDeck.append(player2Card)    
            else:
                player2Card = player2Deck.pop(0)
                outdatedDeck.append(player2Card) 
        else:
            player2Card = player2Deck.pop(0)
            outdatedDeck.append(player2Card) 
        
        print("Player2’s current card:")
        print("Wrestler Name:", player2Card.wrestler)
        print("a. Height:", player2Card.height)
        print("b. Weight:", player2Card.weight)
        print("c. Chest:", player2Card.chest)
        print("d. Biceps:", player2Card.biceps)
        print("e. Rank:", player2Card.rank)
     
    
    else:
        ## Resurrect Spell for Player2 ##
        rb = 0
        if (resurrectSpellPlayer2 == 0 and len(outdatedDeck) > 1 and rb == 0):
            rspell1 = input("Player2, would you like to play Resurrect Spell? Please answer: ‘yes’ or ‘no’")
            if (rspell1 == "yes" and resurrectSpellPlayer2 == 0):
                z2 = random.randint(1,len(outdatedDeck))
                player2Card = outdatedDeck.pop(int(z2)-1)
                outdatedDeck.append(player2Card)
                resurrectSpellPlayer2 = 1
                rb = 1
            else:
                player2Card = player2Deck.pop(0)
                outdatedDeck.append(player2Card)

        else:
            player2Card = player2Deck.pop(0)
            outdatedDeck.append(player2Card)
        
       
        print("Player2’s current card:")
        print("Wrestler Name:", player2Card.wrestler)
        print("a. Height:", player2Card.height)
        print("b. Weight:", player2Card.weight)
        print("c. Chest:", player2Card.chest)
        print("d. Biceps:", player2Card.biceps)
        print("e. Rank:", player2Card.rank)
        
        answer = input("Player2, which characteristic would you choose? ")
        print("Player2 chooses", answer)
        
        #Player2 god spell
        if (godSpellPlayer2 == 0 and len(player1Deck) > 1 and rb == 0):
            gspell1 = input("Player2, would you like to play God Spell? Please answer: ‘yes’ or ‘no’")
            if (gspell1 == "yes" and godSpellPlayer2 == 0):
                godSpellPlayer2 = 1
                lep = len(player1Deck)
                print("No of cards in Player1’s deck:", lep)
                cardno1 = input("Which card should Player1 play with? ")
                if (resurrectSpellPlayer1 == 0 and len(outdatedDeck) > 1):
                    rspell = input("Player1, would you like to play Resurrect Spell? Please answer: ‘yes’ or ‘no’")
                    if (rspell == "yes" and resurrectSpellPlayer1 == 0):
                        z1 = random.randint(1,len(outdatedDeck))
                        nm = outdatedDeck.pop(int(z1)-1)
                        player1Deck.insert(0,nm)
                        choice1 = input("Player2: a. Force resurrected card or b. Force earlier choice ")
                        if (choice1 == "a"):
                            player1Card = player1Deck.pop(0)
                            outdatedDeck.append(player1Card)
                            resurrectSpellPlayer1 = 1
                        else:
                            player1Card = player1Deck.pop(int(cardno1)-1)
                            outdatedDeck.append(player1Card)
                            resurrectSpellPlayer1 = 1
                    else:
                        player1Card = player1Deck.pop(int(cardno1)-1)
                        outdatedDeck.append(player1Card)
                else:                 
                    player1Card = player1Deck.pop(int(cardno1)-1)
                    outdatedDeck.append(player1Card)
            else:
                player1Card = player1Deck.pop(0)
                outdatedDeck.append(player1Card)

        
        else:
            player1Card = player1Deck.pop(0)
            outdatedDeck.append(player1Card)
                                   
        print("Player1’s current card:")
        print("Wrestler Name:", player1Card.wrestler)
        print("a. Height:", player1Card.height)
        print("b. Weight:", player1Card.weight)
        print("c. Chest:", player1Card.chest)
        print("d. Biceps:", player1Card.biceps)
        print("e. Rank:", player1Card.rank)
    
    
    playerWins = False
    #comparing cards of player1 and player2
    if answer == "a":
        playerWins = (player1Card.height > player2Card.height)
    elif answer == "b":
        playerWins = (player1Card.weight > player2Card.weight)
    elif answer == "c":
        playerWins = (player1Card.chest > player2Card.chest)
    elif answer == "d":
        playerWins = (player1Card.biceps > player2Card.biceps)
    elif answer == "e":
        playerWins = (player1Card.rank < player2Card.rank)

    time.sleep(1)
    
    ## Displays who won the particular round ##
    if playerWins:
        print("Player1 won this round!")
        player1Points=player1Points+1      
        playerTurn = True
    else:
        print("Player2 won this round!")
        player2Points=player2Points+1
        playerTurn = False

time.sleep(2)

## Displays who won the game ##
if player1Points<player2Points:
    print("Player2 is the winner of this game!")
elif player1Points>player2Points:
    print("Player1’s is the winner of this game!")
else:
    print("The game ended in a tie!")
 

time.sleep(2)

## Displays total points of each player and the card count in outdated deck ##
print("Total points for Player1: ", player1Points)
print("Total points for Player2: ", player2Points)
print("Total number of cards in Outdated Deck: ", len(outdatedDeck))
