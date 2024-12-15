import casino

class Player:
    def __init__(self, Name, Funds):
        self.Name = Name
        self.Funds = Funds



def createPlayer():
    NameInput = input("What is your name: ")
    FundsInput = int(input("How much do you want to add to your casino account: "))
    newPlayer = Player(NameInput, FundsInput)
    return newPlayer

myPlayer = createPlayer()

def menu():
    print("\nWelcome to the Casino!")
    print("1. Play Blackjack")
    print("2. Play Slot Machine")
    print("3. Play Roulette")
    print("0. Quit")
    while True:
        user_input = int(input("Enter your choice (0-3):"))

        if user_input == 0:
            print("Thank you for playing.")
            break
        elif user_input == 1:
            casino.playBlackjack(Player = myPlayer, Bet = 100)
            print(f"\nYou account has been updated.\nCurrent balance:{myPlayer.Funds}")
            continue
        else:
            print("Invalid input.\n")
            continue

menu()



        