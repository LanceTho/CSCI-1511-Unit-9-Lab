"""
Lab9_LanceTho-1.py
Lance Thongsavanh
This file runs the game. It creates the Player objects and manages the game loop and rules.
Date.
"""

"""
Requirements:
    Import: you must import the Player class (from player import Player).
    Contain a main() function.
    Inside main(), create 2 Player objects (e.g., player1 = Player("Player 1") and player2 = Player("Player 2")).
    Use a while loop to ask the user if they want to play ('y' or 'n').
    
    Inside the loop:
        Tell each player to toss their coin (e.g., player1.toss_coin()).
        Get the result from each player (e.g., side1 = player1.get_coin_side()).
        print the results of the toss (e.g., "Player 1 tossed Heads", "Player 2 tossed Tails").
        If the sides match: call the appropriate methods for the winner to win_coin() and the loser to lose_coin(). Print who won the round.
        Report the toal coins for each player using get_wallet().
        ask the user if they want to play again.
    
    After the loop: print the final results, stating which player finished with more coins.
"""
from player import Player

def main() -> None:
    """Simulates the Coin Match Game and loops until the user enters the exit condition
    """
    player1: Player = Player("Player 1")
    player2: Player = Player("Player 2")
    print("Coin Match Game")
    user_input: str = ""
    while user_input != "n":
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        user_input = input("Do you want to toss the coins? (y/n): ")
        
        match user_input:
            case "y":
                print("Tossing...")
                player1.toss_coin()
                print(f"{player1.get_name()} tossed {player1.get_coin_side()}")
                player2.toss_coin()
                print(f"{player2.get_name()} tossed {player2.get_coin_side()}")
                if(player1.get_coin_side() == player2.get_coin_side()):
                    print(f"It's a Match! {player1.get_name()} wins a coin.")
                    player1.win_coin()
                    player2.lose_coin()
                else:
                    print(f"No Match! {player2.get_name()} wins a coin.")
                    player2.win_coin()
                    player1.lose_coin()

            case "n":
                print("Final Score")
                print(f"{player1.get_name()}: {player1.get_wallet()}")
                print(f"{player2.get_name()}: {player2.get_wallet()}")
                if(player1.get_wallet() == player2.get_wallet()):
                    print(f"It's a draw!")
                elif(player1.get_wallet() > player2.get_wallet()):
                    print(f"{player1.get_name()} Wins!")
                else:
                    print(f"{player2.get_name()} Wins!")

            case _:
                print("Error: Invalid input. Please type y or n")
    
if __name__ == "__main__":
    main()