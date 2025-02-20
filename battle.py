import random
from pokemon import Pokemon

class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def calculate_damage(self, attacker, defender, move):
        """Calculates the damage dealt."""
        damage = move.power
        critical = 1.5 if random.random() < 0.1 else 1.0
        final_damage = max(1, round(damage * critical))
        return final_damage

    def turn(self, attacker, defender):
        """The attacking Pokémon takes its turn."""
        ability = attacker.moves[0]  # Just pick the first move for simplicity
        damage = self.calculate_damage(attacker, defender, ability)
        defender.hp -= damage
        if defender.hp <= 0:
            print(f"💀 {defender.name} is KO!")
            return True
        return False

    def start_battle(self):
        """Starts the battle."""
        print(f"⚔️ Battle between {self.player.name} and {self.opponent.name}!")
        while self.player.hp > 0 and self.opponent.hp > 0:
            if self.turn(self.player, self.opponent):
                break
            if self.turn(self.opponent, self.player):
                break
