import random

SlotMachineSymbols = [
    "🍒",  # Cherry
    "🍋",  # Lemon
    "🍊",  # Orange
    "🍉",  # Watermelon
    "🍇",  # Grapes
    "⭐",   # Star
    "🔔",  # Bell
    "🍀",  # Four-leaf clover
    "💎",  # Diamond
    "🎰",  # Jackpot
    "7️⃣",  # Lucky seven
    "🍎",  # Apple
    "🔥",  # Fire
    "💰",  # Money bag
    "🪙"   # Coin
]

class Slotmachine:

    def __init__(self, Bet):
        self.Bet = Bet
        self.ResultList = [[],[],[]]
        self.RowsMultiplier = 0
        self.Count = 0
        pass
    

    def spinSlotMachine(self):
        for i in range(0, len(self.ResultList)):
            for j in range(3):
                RandomSymbol = random.randint(0, len(SlotMachineSymbols)-1)
                self.ResultList[i].append(SlotMachineSymbols[RandomSymbol])
        
        for row in self.ResultList:
            print("| ".join(row))
        
        pass

    def checkForMatches(self):
        ListOfRows = []

        # check for rows
        for i in range(0,3):
            if self.ResultList[i][0] == self.ResultList[i][1] and self.ResultList[i][0] == self.ResultList[i][2]:
                print(f"Row {i+1} is a match")
                self.RowsMultiplier += 2
                ListOfRows.append(i) # Adding the row to this list to check later in horizontal matches.

        # check adjacent elements horizontally
        for i in range(0,3):
            if i in ListOfRows:
                pass
            else:
                for j in range(0,2):
                    if self.ResultList[i][j] == self.ResultList[i][j+1]:
                        print("Horizontal match " + self.ResultList[i][j] , self.ResultList[i][j+1]+ ": 0.5")
                        self.Count += 0.5

        # check adjacent elements vertically
        for i in range(0,2):
            for j in range(0,3):
                if self.ResultList[i][j] == self.ResultList[i+1][j]:
                    print("Vertical match "+ self.ResultList[i][j], self.ResultList[i+1][j] + ": 0.5")
                    self.Count += 0.5

    def calcaulteMultiplier(self):
        BetMultiplier = 0

        if self.Count > 0:
            BetMultiplier += self.Count
        if self.RowsMultiplier > 0:
            BetMultiplier *= self.RowsMultiplier

        if BetMultiplier > 0:
            print(f"Your total winning: {self.Bet*BetMultiplier}")
        else:
            print("You lost")
        return BetMultiplier
        
    def __repr__(self):
        return """Welcome to the slot machine. Row matches like this 🍀 🍀 🍀 will multiply winnings by X2\nPartial matches 0.5"""