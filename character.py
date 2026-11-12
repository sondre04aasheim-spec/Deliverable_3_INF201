# Character module for the battle simulator (Deliverable 3, INF201)
# Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
# Updated by Zuzanna Magdalena Smolinska and Sondre Aasheim

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

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
