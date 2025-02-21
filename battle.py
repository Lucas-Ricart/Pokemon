import random
from constants import TYPE_ADVANTAGES

class Battle:
    def __init__(self, player, opponent, team):
        """
        Initializes a battle between two Pokémon.
        :param player: The player's Pokémon.
        :param opponent: The opponent's Pokémon.
        :param team: The player's team (Team object).
        """
        self.player = player
        self.opponent = opponent
        self.team = team  # The player's team

    def calculate_damage(self, attacker, defender, move):
        """Calculates the damage dealt."""
        damage = move.power

        # Type modifier
        type_multiplier = 1.0
        for attacker_type in attacker.types:
            for defender_type in defender.types:
                if attacker_type in TYPE_ADVANTAGES and defender_type in TYPE_ADVANTAGES[attacker_type]:
                    type_multiplier *= TYPE_ADVANTAGES[attacker_type][defender_type]

        # Critical hit
        critical = 1.5 if random.random() < 0.1 else 1.0

        # Damage reduction by defender's defense
        final_damage = ((damage * type_multiplier * critical) - defender.get_defense())
        final_damage = max(1, round(final_damage))

        # Display attack
        critical_msg = " 🔥 Critical Hit!" if critical > 1 else ""
        print(f"💥 {attacker.name} uses {move.name} on {defender.name} and deals {final_damage} damage!{critical_msg}")

        return final_damage

    def turn(self, attacker, defender):
        """The attacking Pokémon takes its turn."""
        move = attacker.choose_move()  # Choose a move based on the Pokémon's types
        if move:
            damage = self.calculate_damage(attacker, defender, move)
            defender.take_damage(damage)

            # Check if the defender is KO
            if defender.is_fainted():
                print(f"💀 {defender.name} is KO! {attacker.name} wins the battle!")
                return True  # End of the battle
        return False  # Battle continues

    def start_battle(self):
        """Starts the battle."""
        print(f"⚔️ Battle between {self.player.name} and {self.opponent.name}!")
        while self.player.hp > 0 and self.opponent.hp > 0:
            if self.player.speed >= self.opponent.speed:
                first, second = self.player, self.opponent
            else:
                first, second = self.opponent, self.player

            if self.turn(first, second):
                break
            if self.turn(second, first):
                break

        print("🏁 End of the battle!")
        if self.opponent.hp <= 0:
            print(f"🌟 You defeated {self.opponent.name}!")
            capture_choice = input(f"Do you want to capture {self.opponent.name}? (Yes/No): ").strip().lower()
            if capture_choice in ["yes", "y"]:
                self.team.add_pokemon(self.opponent)

        # Remove fainted Pokémon and increment battle count
        self.team.remove_fainted_pokemon()
        self.team.increment_battle_count()