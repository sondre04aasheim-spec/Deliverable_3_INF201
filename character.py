# Character module for the battle simulator (Deliverable 3, INF201)
# Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
# Zuzanna Magdalena Smolinska and Sondre Aasheim (updated by)

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

        The damage comes from the weapon if the character has one, otherwise from the base damage.

        target: the character being attacked
        """

        if self.weapon is not None:
            damage = self.weapon.roll_damage()           # with a weapon: roll the weapon's dice to decide the damage
        else:
            damage = self.damage                         # without a weapon: use the base damage

        target.take_damage(damage)                       # let the target handle its own damage

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


class Warrior(Character):
    """A defensive character whose armor reduces incoming damage."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Creating a warrior character.

        armor: how much of each attack is blocked (default is 5)
        (the other parameters are the same as for Character)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage: int) -> int:
        """
        Reducing the incoming damage by the armor before it is taken from the HP.

        damage: how much damage the attack deals before armor
        returns: the warrior's HP after the hit
        """
        reduced_damage = max(0, damage - self.armor)        # armor cannot turn damage into healing
        return super().take_damage(reduced_damage)          # Character.take_damage handles the HP rules


class Mage(Character):
    """A magic character whose spells cost mana."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Creating a mage, with or without a weapon.

        mana: how much mana the mage starts with (default is 30)
        mana_max: the most mana the mage can have (default is 30)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = min(mana, mana_max)                         # mana cannot start above the max

    def attack(self, target: "Character") -> None:
        """
        Attacking with a spell if there is enough mana, otherwise with a normal attack.
        """
        
        if self.mana >= 10:                                     # checking if the mage has at least 10 mana to cast a spell
            # enough mana: cast a spell that deals double base damage (no weapon)

            self.mana -= 10                                     # losing 10 mana for the spell
            print(f"{self.name} casts a spell! ({self.mana} mana left)")
            target.take_damage(self.damage * 2)                 # base damage is doubled for the spell, and the target handles its own HP
        else:
            # not enough mana: normal attack (with weapon if there is one), and regain 5 mana

            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)       # mana cannot go above the max
