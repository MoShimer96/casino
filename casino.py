import blackjack



def playBlackjack(Player, Bet):
    newGame = blackjack.Blackjack()
    print(newGame)
    newGame.drawFirstTwo()
    Playertotal, DealerTotal = newGame.calculateTotal()
    newGame.displayCards()
    

    while True:

        # Check for user bust
        if Playertotal > 21:
            print("Bust! You lose.")
            newGame.displayCardEndOfGame()
            Player.Funds -= Bet
            break

        # Player's choice to hit or stand
        user_input = input("Enter H to Hit or S to Stand: ").upper()

        if user_input == 'S':
            print("You chose to stand.")
            newGame.displayCardEndOfGame()

        if Playertotal <= 21 and DealerTotal < Playertotal:
            Player.Funds += Bet * 2 # Player wins their bet amount
            print("You Won!")
            break
        elif DealerTotal <= 21 and DealerTotal > Playertotal:
            Player.Funds -= Bet  # Player loses their bet amount
            print("House Wins!")
            break
        elif Playertotal == DealerTotal:
            print("It's a tie! Bet returned.")
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







