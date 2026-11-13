# Battle module for the battle simulator (Deliverable 3, INF201)
# Zuzanna Magdalena Smolinska and Sondre Aasheim

from character import Character         # a battle is fought between two characters


class Battle:
    """
    Manages a turn-based fight between two characters.
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Setting up a battle between two characters.

        hero: the character who attacks first in each round
        enemy: the character who attacks second
        """
        self.hero = hero
        self.enemy = enemy

        self.round = 0                              # how many rounds have been played
    
    def play_round(self) -> None:
        """
        Playing the round: the hero attacks first, then the enemy attacks back if still alive.
        """
        self.round += 1                             # a new round starts
        print(f"--- Round {self.round} ---")

        self.hero.attack(self.enemy)
        print(f"{self.hero.name} attacks! {self.enemy.name} has {self.enemy.hp} HP left")

        # the enemy can only attack back if it survived

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            print(f"{self.enemy.name} attacks! {self.hero.name} has {self.hero.hp} HP left")
    
    def simulate_battle(self, max_rounds: int = 100) -> Character | None:
        """
        Playing rounds until one of the characters dies.
        max_rounds: safety limit, so the battle cannot go on forever (default is 100)
        returns: the winner, or None if nobody won within the round limit
        """
        
        # keep playing as long as both characters are alive

        while self.hero.is_alive and self.enemy.is_alive:
            if self.round >= max_rounds:
                print("The battle took too long, nobody wins!")
                return None
            self.play_round()

        # the loop has ended, so one character is dead: the other one is the winner

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"{winner.name} wins after {self.round} rounds!")
        return winner
