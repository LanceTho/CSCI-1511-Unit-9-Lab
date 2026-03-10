"""
coin.py
Lance Thongsavanh
This class represents a single, tossable coin. It only knows about its current state (heads or tails).
Date.
"""

"""
Attributes:
    __sideup: A private string attribute, initialized to 'Heads' or 'Tails'.

Methods:
    __init__(): The initalizer method that sets up the __sideup attribute.
    toss(): Generates a random timber (0 or 1) and sets __sideup to 'Heads' or 'Tails' accordingly.
    get_sideup(): Returns the current value of __sideup.
"""
import random
class Coin:
    def __init__(self, __sideup: str) -> None:
        self.__sideup = __sideup

    def toss(self) -> None:
        number: int = random.randint(0,1)
        if(number == 1):
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        return f"The coin has the {self.__sideup} side facing up."
    
if __name__ == "__main__":
    quarter = Coin("Heads")
    quarter.toss()
    print(quarter.get_sideup())