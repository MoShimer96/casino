import casino

class Player:
    def __init__(self, Name, Funds):
        self.Name = Name
        self.Funds = Funds


def createPlayer():
    NameInput = input("What is your name: ")
    FundsInput = float(input("How much do you want to add to your casino account: "))
    NewPlayer = Player(NameInput, FundsInput)
    return NewPlayer

MyPlayer = createPlayer()

def menu():
    print("\nWelcome to the Casino!")
    print("1. Play Blackjack")
    print("2. Play Slot Machine")
    print("3. Play Roulette")
    print("0. Quit")
    while True:
        UserInput = int(input("Enter your choice (0-3):"))

        if UserInput == 0:
            print("\nThank you for playing.")
            break
        elif UserInput == 1:
            PlaceBet = float(input("Place your bet: "))
            casino.playBlackjack(Player = MyPlayer, Bet = PlaceBet)
            print(f"\nYou account has been updated.\nCurrent balance:{MyPlayer.Funds}")
            continue
        elif UserInput == 2:
            casino.playSlots(MyPlayer)
            print(f"\nYou account has been updated.\nCurrent balance:{MyPlayer.Funds}")
        else:
            print("Invalid input.\n")
            continue

menu()



        