import blackjack
import slotmachine


def playBlackjack(Player, Bet):
    newGame = blackjack.Blackjack()
    print(newGame)
    newGame.drawFirstTwo()
    Playertotal, DealerTotal = newGame.calculateTotal()
    newGame.displayCards()
    

    while True:

        # Check for user bust
        if Playertotal > 21:
            print("\nBust! You lose.")
            newGame.displayCardEndOfGame()
            Player.Funds -= Bet
            break

        # Player's choice to hit or stand
        user_input = input("Enter H to Hit or S to Stand: ").upper()

        if user_input == 'S':
            print("\nYou chose to stand.")
            newGame.displayCardEndOfGame()

            if Playertotal <= 21 and DealerTotal < Playertotal:
                Player.Funds += Bet * 2 # Player wins their bet amount
                print("\nYou Won!")
                break
            elif DealerTotal <= 21 and DealerTotal > Playertotal:
                Player.Funds -= Bet  # Player loses their bet amount
                print("\nHouse Wins!")
                break
            elif Playertotal == DealerTotal:
                print("\nIt's a tie! Bet returned.")
                break
                
        elif user_input == 'H':
            newGame.drawCardPlayer() 
            newGame.drawCardDealer() 
            Playertotal, DealerTotal = newGame.calculateTotal()  
            newGame.displayCards()
            continue

        else:
            print("Invalid input. Please enter H or S.")
            continue



def playSlots(Player):
    while True:
        UserInput = input("Enter 'S' to spin or 'Q' to quit: ")
        if UserInput.upper() == 'S':
            SlotBet = int(input("How much do you want to bet: "))
            Player.Funds -= SlotBet
            NewSlotMachine = slotmachine.Slotmachine(SlotBet)
            NewSlotMachine.spinSlotMachine()
            NewSlotMachine.checkForMatches()
            Result = NewSlotMachine.calculateResult()

            
            if Result > 0:
                Player.Funds += Result
            continue
        else:
            break
