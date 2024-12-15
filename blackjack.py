import random

class Blackjack:

    def __init__(self):
        self.Deck = {
        1: ['2', 2, 4],
        2: ['3', 3, 4],
        3: ['4', 4, 4],
        4: ['5', 5, 4],
        5: ['6', 6, 4],
        6: ['7', 7, 4],
        7: ['8', 8, 4],
        8: ['9', 9, 4],
        9: ['10', 10, 4],
        10: ['J', 10, 4],  # Jack
        11: ['Q', 10, 4],  # Queen
        12: ['K', 10, 4],  # King
        13: ['A', [1, 11], 4]  # Ace can be 1 or 11
        }
        self.PlayerTotal = 0
        self.DealerTotal = 0
        self.PlayerHand = []
        self.DealerHand = []
        pass

    def drawCard(self):
        # Index: ['Face', Value, Number of cards in the deck]
        while True:
            CardIndex = random.randint(1,13)
            if self.Deck[CardIndex][2] > 0:
                self.Deck[CardIndex][2] -= 1
                return [self.Deck[CardIndex][0], self.Deck[CardIndex][1]]
                break
            else:
                continue
        

    def drawCardPlayer(self):
        Card = self.drawCard()
        self.PlayerHand.append(Card)
        pass

    def drawCardDealer(self):
        Card = self.drawCard()
        self.DealerHand.append(Card)
        pass

    def drawFirstTwo(self):
        for i in range(0,2):
            self.drawCardDealer()
            self.drawCardPlayer()
        pass

    def displayCards(self):

        print("\nDealer's cards:")
        
        for i in range(0, len(self.DealerHand)):
            if i == 0:
                print(self.DealerHand[0])
            else:
                print("[*]")
        
        print("\nPlayer's cards: ")
        for Card in self.PlayerHand:
            print(Card)
        print(f"Player's point total: {self.PlayerTotal}\n")
        pass

    def sortHands(self):
        PlayerHandSorted = []
        DealerHandSorted = []
        
        for Card in self.PlayerHand:
            if Card[0] == 'A':
                PlayerHandSorted.append(Card)
            else:
                PlayerHandSorted.insert(0, Card)
        
        for Card in self.DealerHand:
            if Card[0] == 'A':
                DealerHandSorted.append(Card)
            else:
                DealerHandSorted.insert(0, Card)
        
        self.PlayerHand = PlayerHandSorted
        self.DealerHand = DealerHandSorted
        pass

    def calculateTotal(self):
        self.sortHands()
        self.PlayerTotal = 0
        self.DealerTotal = 0

        for Card in self.PlayerHand:
            if Card[0] == 'A' and self.PlayerTotal + 11 > 21:
                self.PlayerTotal += Card[1][0]
            elif Card[0] == 'A' and self.PlayerTotal + 11 <= 21:
                self.PlayerTotal += Card[1][1]
            else:
                self.PlayerTotal += Card[1]

        for Card in self.DealerHand:
            if Card[0] == 'A' and self.DealerTotal + 11 > 21:
                self.PlayerTotal += 1
            elif Card[0] == 'A' and self.DealerTotal + 11 <= 21:
                self.DealerTotal += 11
            else:
                self.DealerTotal += Card[1]

        print(f"Player's total: {self.PlayerTotal}\n")
        return self.PlayerTotal, self.DealerTotal

    def displayPoint(self):
        print(f"Dealer's total: {self.DealerTotal} Player's total: {self.PlayerTotal}\n")
        pass
    
    def displayCardEndOfGame(self):
        print("Dealer's hand: ")
        for Card in self.DealerHand:
            print("|".join([Card[0], str(Card[1])]))
        
        print("Player's hand:" )
        for Card in self.PlayerHand:
            print("|".join([Card[0], str(Card[1])]))

        self.displayPoint()

    def __repr__(self):
        return ("""1)Each player is dealt two cards; they can \"hit\" (draw another card) or \"stand\" (end their turn).
2)Face cards are worth 10, Aces are 1 or 11, and all others are their number value.
3)If the total exceeds 21, the player \"busts\" and loses their wager.""")
        

