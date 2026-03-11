"""
coin.py
Lance Thongsavanh
This class represents a single, tossable coin. It only knows about its current state (heads or tails).
3/11/2026
"""

import random
class Coin:
    """This class represents a coin that can be tossed"""

    def __init__(self) -> None:
        """Initializes the __sideup attribute to 'Heads' or 'Tails'
        """
        self.toss()

    def toss(self) -> None:
        """Generates a random number of 0 or 1 and sets the __sideup attribute to "Heads" or "Tails"
        """
        number: int = random.randint(0,1)
        if(number == 1):
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        """Returns a string that states which side of the coin is facing up

        Returns:
            str: The string statement
        """
        return f"The coin has the {self.__sideup} side facing up."
    
if __name__ == "__main__":
    quarter = Coin()
    print(quarter.get_sideup())
    quarter.toss()
    print(quarter.get_sideup())