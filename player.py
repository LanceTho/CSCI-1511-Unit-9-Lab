"""
player.py
Lance Thongsavanh
This class represents a player. A player has a name, has a wallet of coins, and has a Coin object to toss.
Date.
"""

"""
Requirements:
    Import: Import the Coin class at the top of this file (from coin import Coin).

Attributes:
    __name: A private string attribute (e.g., "Player 1").
    __wallet: A private integer attribute, intialized to 20.
    __coin: A private attribute that is an instance of the Coin class (e.g., self.__coin = Coin()).

Methods:
    __init__(name): The intitalizer method. It should take a name as an argument and set up all three private attributes.
    toss_coin(): This method tells the player's coin to toss itself (e.g., self.__coin.toss()).
    get_coin_side(): This method gets the side of the player's coin by calling the coin's get_sideup() method and returning its value.
    win_coin(): Adds 1 to the __wallet.
    lose_coin(): Subtracts 1 from the __wallet
    get_wallet(): Returns the current value of __wallet.
    get_name(): Returns the value of __name.
"""
from coin import Coin
class Player:
    """This class represents a player
    """
    def __init__(self, name: str) -> None:
        """Initializes the player object and sets up 3 private attributes

        Args:
            name (str): The name of the player
        """
        self.__name = name
        self.__wallet: int = 20
        self.__coin = Coin()

    def toss_coin(self) -> None:
        """This method tells the player's coin to toss itself
        """
        self.__coin.toss()
    
    def get_coin_side(self) -> str:
        """This method gets the side of the player's coin by calling the coin's get_sideup() method and returning its value

        Returns:
            str: The string statement that says the coin's value
        """
        return self.__coin.get_sideup()
    
    def win_coin(self) -> None:
        """Adds 1 to the __wallet
        """
        self.__wallet += 1

    def lose_coin(self) -> None:
        """Subtracts 1 to the __wallet
        """
        self.__wallet -= 1

    def get_wallet(self) -> int:
        """Returns the current value of __wallet

        Returns:
            int: The current value of __wallet
        """
        return self.__wallet
    
    def get_name(self) -> str:
        """Returns the current value of __name

        Returns:
            str: The current value of __name
        """
        return self.__name
    
if __name__ == "__main__":
    p1 = Player("Cj")
    print(p1.get_name())
    p1.toss_coin()
    print(p1.get_coin_side())
    p1.win_coin()
    print(p1.get_wallet())
    p1.toss_coin()
    print(p1.get_coin_side())
    p1.lose_coin()
    print(p1.get_wallet())