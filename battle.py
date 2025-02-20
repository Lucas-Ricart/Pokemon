# Battle Class
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
        """Calculates the damage dealt based on attack power, types, and defense."""
        damage = move.power

        # Type modifier (advantages/disadvantages)
        type_multiplier = 1.0
        for attacker_type in attacker.types:
            for defender_type in defender.types:
                if attacker_type in TYPE_ADVANTAGES and defender_type in TYPE_ADVANTAGES[attacker_type]:
                    type_multiplier *= TYPE_ADVANTAGES[attacker_type][defender_type]

        # Critical hit (10% chance, deals 1.5x damage)
        critical = 1.5 if random.random() < 0.1 else 1.0

        # Damage reduction by defender's defense
        final_damage = ((damage * type_multiplier * critical) - defender.defense)

        # Avoid negative damage (minimum 1)
        final_damage = max(1, round(final_damage))

        # Display attack
        critical_msg = " 🔥 Critical Hit!" if critical > 1 else ""
        print(f"💥 {attacker.name} uses {move.name} on {defender.name} and deals {final_damage} damage!{critical_msg}")

        return final_damage

    def turn(self, attacker, defender):
        """The attacking Pokémon takes its turn."""
        move = random.choice(attacker.moves)  # Randomly select a move
        damage = self.calculate_damage(attacker, defender, move)
        defender.hp -= damage

        # Check if the defender is KO
        if defender.hp <= 0:
            print(f"💀 {defender.name} is KO! {attacker.name} wins the battle!")
            return True  # End of the battle
        return False  # Battle continues

    def start_battle(self):
        """Starts the battle and alternates turns based on speed."""
        print(f"⚔️ Battle between {self.player.name} and {self.opponent.name}!")

        while self.player.hp > 0 and self.opponent.hp > 0:
            # Determine who attacks first (the faster one)
            if self.player.speed >= self.opponent.speed:
                first, second = self.player, self.opponent
            else:
                first, second = self.opponent, self.player

            # Turn of the faster Pokémon
            if self.turn(first, second):
                break  # End of battle if KO

            # Turn of the second Pokémon (if still alive)
            if self.turn(second, first):
                break  # End of battle if KO

        print("🏁 End of the battle!")

# Graphical interface with Pygame
def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
