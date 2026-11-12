# Dice module for the battle simulator (Deliverable 3, INF201)
# Zuzanna Magdalena Smolinska and Sondre Aasheim

import random                   # used to roll the dice (random whole numbers)


class Dice:
    """
    Represents a dice used for random damage rolls.
    """

    def __init__(self, sides: int = 6) -> None:
        """
        Creating a dice with the given number of sides.
        Our dice needs at least 2 sides, otherwise stop with a clear error.

        sides: how many sides the dice has (default is 6, must be at least 2)
        """   
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")

        # store the number of sides, so other methods can use it
        self.sides = sides

    def roll(self) -> int:
        """
        Rolling the dice and returning a random number from 1 to the number of sides.
        """
        # randint includes values from both ends, so a 6-sided dice gives 1, 2, 3, 4, 5 or 6
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """
        Showing the dice as text, for example: Dice(sides=6).
        """
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """
        Rolling the dice by calling it directly, for example: d20() instead of d20.roll().
        """
        # calling the dice does the same thing as rolling it
        return self.roll()
