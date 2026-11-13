# Character module for the battle simulator (Deliverable 3, INF201)
# Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
# Updated by Zuzanna Magdalena Smolinska and Sondre Aasheim

from items import Weapon        # characters can hold a weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Creating a character with a name, maximum HP, base damage, AND an optional weapon.
        
        name: the name of the character
        hp_max: the maximum HP (default is 100)
        damage: base damage when attacking without a weapon (default is 10)
        weapon: an optional weapon (default is None, meaning no weapon)
        """
        self.name = name
        self._hp = hp_max                   # the character starts with full HP
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target: "Character") -> None:       # using quotes as Character is not fully defined yet
        """
        This method is called when the character attacks another character.
        The target takes care of its own HP by calling its take_damage() method.

        target: the character being attacked
        """
        target.take_damage(self.damage)                  # let the target handle its own damage

    def take_damage(self, damage: int) -> int:
        """ 
        This method only changes the character's own HP. 
        When another character attacks, it calls this method instead of changing the HP directly.
        
        damage: how much HP the character loses (negative damage counts as 0)
        returns: the character's HP after the hit
        """
        damage = max(0, damage)                 # damage cannot be less than 0
        
        self._hp -= damage                      # only change the character's own HP
        self._hp = max(0, self._hp)             # HP cannot be less than 0
        
        if self._hp > 0:
            return self._hp                     # character is still alive, return the new hp
        else:
            print(self.name, "has died")        # HP reached 0, so the character has died
            return self._hp

    def heal(self, amount: int) -> int:
        """
        This method only changes the character's own HP.
        It increases the HP, but never above the character's max HP.

        amount: how much HP the character gains (negative healing counts as 0)
        returns: the character's HP after healing
        """
        amount = max(0, amount)                     # healing cannot be less than 0
        
        self._hp += amount                          # only change the character's own HP
        self._hp = min(self._hp, self.hp_max)       # HP cannot go above max HP
        
        return self._hp

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns True if the character is alive (HP > 0), False otherwise."""
        return self._hp > 0
