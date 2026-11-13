# Items module for the battle simulator (Deliverable 3, INF201)
# Zuzanna Magdalena Smolinska and Sondre Aasheim

from dice import Dice           # weapons use a dice to decide their damage


class Weapon:
    """
    Represents a weapon that deals damage using a dice.
    """

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Creating a weapon with a name and a dice for damage.

        name: the name of the weapon
        damage_dice: the dice that is rolled to decide the damage
        """
        self.name = name
        self.damage_dice = damage_dice              # the weapon holds its own dice

    def roll_damage(self) -> int:
        """
        Rolling the weapon's dice to decide how much damage it deals.
        """
        return self.damage_dice.roll()              # the dice does the rolling

    def __repr__(self) -> str:
        """
        Showing the weapon as text.
        An example: Weapon(name='sword', damage_dice=Dice(sides=8)).
        """
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"
