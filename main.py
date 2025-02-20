import pygame
import sys
import random
from pokemon import Pokemon, fetch_pokemon
from team import Team
from battle import Battle
from pokedex import Pokedex
from utils import display_text

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Main function
def main():
    team = Team()
    pokedex = Pokedex()

    while True:
        screen.fill((255, 255, 255))  # White background
        display_text("🌟 MAIN MENU 🌟", 250, 50)
        display_text("1. Add a Pokémon", 250, 150)
        display_text("2. Display the team", 250, 200)
        display_text("3. Fight an opponent", 250, 250)
        display_text("4. Display the Pokédex", 250, 300)
        display_text("5. Quit", 250, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pokemon_name = input("Enter the name of the Pokémon to add: ").strip().lower()
                    pokemon_data = fetch_pokemon(pokemon_name)
                    if pokemon_data:
                        pokemon = Pokemon(**pokemon_data)
                        team.add_pokemon(pokemon)
                        pokedex.add_pokemon(pokemon)
                elif event.key == pygame.K_2:
                    team.display_team()
                elif event.key == pygame.K_3:
                    player_pokemon = team.choose_pokemon()
                    if player_pokemon:
                        opponent_name = random.choice(["squirtle", "charmander", "bulbasaur", "pikachu", "eevee"])
                        opponent_data = fetch_pokemon(opponent_name)
                        if opponent_data:
                            opponent_pokemon = Pokemon(**opponent_data)
                            battle = Battle(player_pokemon, opponent_pokemon)
                            battle.start_battle()
                elif event.key == pygame.K_4:
                    pokedex.display_pokedex()
                elif event.key == pygame.K_5:
                    pygame.quit()
                    sys.exit()
