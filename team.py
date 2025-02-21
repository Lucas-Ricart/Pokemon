import json
from pokemon import Pokemon
from battle import Battle


class Team:
    def __init__(self):
        self.pokemons = self.load_team()
        # If the team is empty, offer a starter Pokémon
        if not self.pokemons:
            self.choose_starter()

    def load_team(self):
        """
        Loads the team from a JSON file.
        If the file is missing or corrupted, initializes an empty team.
        """
        try:
            with open("pokemon.json", "r") as file:
                pokemons_data = json.load(file)
                if not isinstance(pokemons_data, list):
                    print("⚠️ Malformed file. Resetting the team...")
                    return []
                return [Pokemon(**p) for p in pokemons_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("📁 File not found or corrupted. Creating a new team.")
            return []

    def save_team(self):
        """
        Saves the current team to a JSON file.
        """
        try:
            with open("pokemon.json", "w") as file:
                json.dump([p.to_dict() for p in self.pokemons], file, indent=4)
            print("✅ Team successfully saved!")
        except Exception as e:
            print(f"❌ Error while saving the team: {e}")

    def choose_starter(self):
        """
        Allows the player to choose a starter from the first three Pokémon.
        """
        starters = [
            Pokemon(name="Bulbasaur", types=["grass", "poison"], hp=45, attack=49, special_attack=65, defense=49, speed=45),
            Pokemon(name="Charmander", types=["fire"], hp=39, attack=52, special_attack=60, defense=43, speed=65),
            Pokemon(name="Squirtle", types=["water"], hp=44, attack=48, special_attack=50, defense=65, speed=43)
        ]

        print("🌟 CHOOSE YOUR STARTER 🌟")
        for i, starter in enumerate(starters):
            print(f"{i + 1}. {starter.name} (Type: {', '.join(starter.types)})")

        while True:
            choice = input("\nChoose a starter (1-3): ")
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(starters):
                    selected_starter = starters[choice]
                    self.add_pokemon(selected_starter)
                    print(f"✅ You chose {selected_starter.name}!")
                    break
            print("❌ Invalid choice, please try again.")

    def add_pokemon(self, pokemon):
        """
        Adds a Pokémon to the team if there is space.
        :param pokemon: The Pokémon to add.
        """
        if len(self.pokemons) >= 6:
            print("❌ Team is full! Cannot add another Pokémon.")
            return False

        if not isinstance(pokemon, Pokemon):
            print("❌ Invalid Pokémon object.")
            return False

        self.pokemons.append(pokemon)
        self.save_team()
        print(f"✅ {pokemon.name} has been added to the team!")
        return True

    def remove_pokemon(self, index):
        """
        Removes a Pokémon from the team by its index.
        :param index: The index of the Pokémon to remove.
        """
        if 0 <= index < len(self.pokemons):
            removed_pokemon = self.pokemons.pop(index)
            self.save_team()
            print(f"✅ {removed_pokemon.name} has been removed from the team.")
            return True
        else:
            print("❌ Invalid index. No Pokémon removed.")
            return False

    def swap_pokemon(self, index1, index2):
        """
        Swaps the positions of two Pokémon in the team.
        :param index1: The index of the first Pokémon.
        :param index2: The index of the second Pokémon.
        """
        if 0 <= index1 < len(self.pokemons) and 0 <= index2 < len(self.pokemons):
            self.pokemons[index1], self.pokemons[index2] = self.pokemons[index2], self.pokemons[index1]
            self.save_team()
            print(f"✅ The positions of {self.pokemons[index2].name} and {self.pokemons[index1].name} have been swapped.")
            return True
        else:
            print("❌ Invalid indices. No Pokémon swapped.")
            return False

    def display_team(self):
        """
        Displays the current team in a readable format.
        """
        if not self.pokemons:
            print("📁 The team is empty.")
            return

        print("\n🌟 YOUR TEAM 🌟")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}. {pokemon.name} (Level: {pokemon.level}, HP: {pokemon.hp}/{pokemon.max_hp})")
            print(f"   Types: {', '.join(pokemon.types)}")
            print(f"   Moves: {', '.join([move.name for move in pokemon.moves])}")
            print()

    def choose_pokemon(self):
        """
        Allows the player to choose a Pokémon from the team for battle.
        :return: The chosen Pokémon or None if the team is empty.
        """
        if not self.pokemons:
            print("⚠️ Unable to battle, the team is empty.")
            return None

        self.display_team()
        while True:
            choice = input("\nChoose a Pokémon (1-6): ")
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(self.pokemons):
                    return self.pokemons[choice]
            print("❌ Invalid choice, please try again.")

    def is_team_full(self):
        """
        Checks if the team is full.
        :return: True if the team is full, False otherwise.
        """
        return len(self.pokemons) >= 6

    def get_team_size(self):
        """
        Returns the current number of Pokémon in the team.
        :return: The number of Pokémon in the team.
        """
        return len(self.pokemons)

    def get_pokemon_by_index(self, index):
        """
        Returns a Pokémon by its index in the team.
        :param index: The index of the Pokémon.
        :return: The Pokémon or None if the index is invalid.
        """
        if 0 <= index < len(self.pokemons):
            return self.pokemons[index]
        return None

def capture_pokemon(self, pokemon):
    """
    Allows the player to capture a Pokémon and add it to the team.
    If the team is full, the player must choose a Pokémon to replace.
    :param pokemon: The Pokémon to capture.
    """
    if len(self.pokemons) < 6:
        self.add_pokemon(pokemon)
        print(f"✅ {pokemon.name} has been added to your team!")
    else:
        print("❌ Your team is full. Choose a Pokémon to replace:")
        self.display_team()
        while True:
            choice = input("\nChoose a Pokémon to replace (1-6) or cancel (0): ")
            if choice.isdigit():
                choice = int(choice) - 1
                if choice == -1:
                    print("❌ Capture canceled.")
                    return
                elif 0 <= choice < len(self.pokemons):
                    replaced_pokemon = self.pokemons[choice]
                    self.pokemons[choice] = pokemon
                    self.save_team()
                    print(f"✅ {pokemon.name} has replaced {replaced_pokemon.name} in your team!")
                    return
            print("❌ Invalid choice, please try again.")
            
def heal_team(self):
    """Heals all Pokémon in the team."""
    for pokemon in self.pokemons:
        pokemon.hp = pokemon.max_hp
    print("🌟 Your team has been healed!")
def remove_fainted_pokemon(self):
        """Removes fainted Pokémon from the team."""
        self.pokemons = [pokemon for pokemon in self.pokemons if not pokemon.is_fainted()]
        print("💀 Fainted Pokémon have been removed from the team.")

def get_average_level(self):
        """Returns the average level of the team."""
        if not self.pokemons:
            return 0
        return sum(pokemon.level for pokemon in self.pokemons) // len(self.pokemons)
def increment_battle_count(self):
    """Increments the battle counter and heals the team after 5 battles."""
    self.battle_count += 1
    if self.battle_count >= 5:
        self.heal_team()
        self.battle_count = 0  # Reset the counter


