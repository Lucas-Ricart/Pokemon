import json
import pygame
from pokemon import Pokemon

class Pokedex:
    def __init__(self):
        self.pokemons = self.load_pokedex()
        self.scroll_offset = 0  # Initial scroll position

    def load_pokedex(self):
        """Loads the Pokédex from a JSON file."""
        try:
            with open("data/pokedex.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_pokemon(self, pokemon):
        """Adds a Pokémon to the Pokédex."""
        if pokemon.name not in [p["name"] for p in self.pokemons]:
            self.pokemons.append(pokemon.to_dict())
            self.save_pokedex()
            print(f"✅ {pokemon.name} added to the Pokédex!")

    def save_pokedex(self):
        """Saves the Pokédex to a JSON file."""
        with open("data/pokedex.json", "w") as file:
            json.dump(self.pokemons, file, indent=4)

    def display_pokedex(self, screen):
        """Displays the Pokédex with Pokémon sprites and information."""
        if not self.pokemons:
            print("📁 The Pokédex is empty.")
            return

        font = pygame.font.Font(None, 36)
        y = 50 - self.scroll_offset  # Apply scrolling
        for pokemon_data in self.pokemons:
            pokemon = Pokemon(**pokemon_data)

            # Display only visible Pokémon
            if y + 80 > 0 and y < HEIGHT:  # HEIGHT is the screen height
                # Display the sprite
                if pokemon.sprite:
                    sprite = pygame.transform.scale(pokemon.sprite, (64, 64))  # Resize the sprite
                    screen.blit(sprite, (50, y))

                # Display name and information
                text = font.render(f"{pokemon.name} (Level: {pokemon.level})", True, (0, 0, 0))
                screen.blit(text, (150, y + 20))

            y += 80  # Spacing between Pokémon

        pygame.display.flip()

    def handle_scroll(self, event):
        """Handles Pokédex scrolling."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.scroll_offset = max(0, self.scroll_offset - 20)
            elif event.button == 5:  # Scroll down
                self.scroll_offset = min(len(self.pokemons) * 80 - HEIGHT, self.scroll_offset + 20)

    def select_pokemon(self, screen):
        """Allows the player to select a Pokémon from the Pokédex."""
        running = True
        while running:
            screen.fill((255, 255, 255))  # Clear the screen
            self.display_pokedex(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        x, y = event.pos
                        # Calculate the clicked Pokémon index considering scrolling
                        index = (y + self.scroll_offset - 50) // 80

                        # Check if the Pokémon is visible on screen
                        if 0 <= index < len(self.pokemons):
                            pokemon_y = 50 + index * 80 - self.scroll_offset
                            if 0 <= pokemon_y < HEIGHT:  # Ensure visibility
                                selected_pokemon = Pokemon(**self.pokemons[index])
                                print(f"🌟 You selected {selected_pokemon.name}!")
                                return selected_pokemon
                            else:
                                print("❌ This Pokémon is not visible on the screen.")
                self.handle_scroll(event)  # Handle scrolling

            pygame.display.flip()
