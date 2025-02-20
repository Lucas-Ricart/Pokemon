import random
from utils  import TYPE_ADVANTAGES

class Battle:
    def __init__(self, player, opponent):
        """
        Initializes a battle between two Pokémon.
        :param player: The player's Pokémon.
        :param opponent: The opponent's Pokémon.
        """
        self.player = player
        self.opponent = opponent

    def calculate_damage(self, attacker, defender, move):
        """
        Calculates the damage dealt based on attack, types, and defense.
        """
        damage = move.power

        # Type modifier (advantages/disadvantages)
        type_multiplier = 1.0
        for attacker_type in attacker.types:
            for defender_type in defender.types:
                if attacker_type in TYPE_ADVANTAGES and defender_type in TYPE_ADVANTAGES[attacker_type]:
                    type_multiplier *= TYPE_ADVANTAGES[attacker_type][defender_type]

        # Critical hit (10% chance, 1.5x damage)
        critical = 1.5 if random.random() < 0.1 else 1.0

        # Damage reduction based on the defender's defense
        final_damage = ((damage * type_multiplier * critical) - defender.defense)

        # Prevent negative damage (minimum 1)
        final_damage = max(1, round(final_damage))

        # Display the attack
        critical_msg = " 🔥 Critical Hit!" if critical > 1 else ""
        print(f"💥 {attacker.name} uses {move.name} on {defender.name} and deals {final_damage} damage!{critical_msg}")

        return final_damage

    def turn(self, attacker, defender):
        """
        The attacking Pokémon takes its turn.
        """
        move = random.choice(attacker.moves)  # Select a random move
        damage = self.calculate_damage(attacker, defender, move)
        defender.hp -= damage

        # Check if the defender is KO
        if defender.hp <= 0:
            print(f"💀 {defender.name} is KO! {attacker.name} wins the battle!")
            return True  # End the battle
        return False  # Continue the battle

    def start_battle(self, team):
        """
        Starts the battle and alternates turns based on speed.
        After a win, the player is offered the chance to capture the opponent's Pokémon.
        :param team: The player's team.
        """
        print(f"⚔️ Battle between {self.player.name} and {self.opponent.name}!")

        while self.player.hp > 0 and self.opponent.hp > 0:
            # Determine who attacks first (the faster Pokémon)
            if self.player.speed >= self.opponent.speed:
                first, second = self.player, self.opponent
            else:
                first, second = self.opponent, self.player

            # Turn for the faster Pokémon
            if self.turn(first, second):
                break  # End battle if KO

            # Turn for the second Pokémon (if still alive)
            if self.turn(second, first):
                break  # End battle if KO

        print("🏁 Battle Ended!")

        # If the player wins, offer to capture the opponent's Pokémon
        if self.opponent.hp <= 0:
            print(f"🌟 You defeated {self.opponent.name}!")
            capture_choice = input(f"Do you want to capture {self.opponent.name}? (Yes/No): ").strip().lower()
            if capture_choice in ["yes", "y"]:
                team.capture_pokemon(self.opponent)


    def calculate_damage(self, attacker, defender, move):
        """Calculates the damage dealt."""
        damage = move.power
        critical = 1.5 if random.random() < 0.1 else 1
        if critical == 1:
            fail = 0 if random.random() < 0.1 else 1
        final_damage = max(1, round(damage * critical * fail))
        return final_damage
