import json
import random
import requests
import pygame
import sys
from io import BytesIO

# Initialisation de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Constantes
TYPE_ADVANTAGES = {
    "feu": {"plante": 2, "eau": 0.5, "feu": 0.5},
    "eau": {"feu": 2, "plante": 0.5, "eau": 0.5},
    "plante": {"eau": 2, "feu": 0.5, "plante": 0.5},
}

# Dictionnaire pour mapper les noms des Pokémon à leurs numéros
POKEMON_SPRITES = {
    "bulbasaur": 1,
    "ivysaur": 2,
    "venusaur": 3,
    "charmander": 4,
    "charmeleon": 5,
    "charizard": 6,
    "squirtle": 7,
    "wartortle": 8,
    "blastoise": 9,
    "pikachu": 25,
    "eevee": 133,
    # Ajoutez d'autres Pokémon ici
}

# Fonction pour charger une image locale
def charger_image_locale(nom_pokemon):
    """Charge une image depuis le dossier sprites/pokemon."""
    try:
        numero = POKEMON_SPRITES.get(nom_pokemon.lower())
        if numero is not None:
            chemin = f"\\sprites\sprites\pokemon/{numero}.png"
            return pygame.image.load(chemin)
        else:
            print(f"❌ Aucun sprite trouvé pour {nom_pokemon}.")
            return None
    except Exception as e:
        print(f"❌ Erreur lors du chargement de l'image pour {nom_pokemon}: {e}")
        return None


# Classe Pokémon
class Pokemon:
    def __init__(self, nom, types, pv, attaque, defense, vitesse, niveau=1, exp=0, capacites=None, evolution=None):
        self.nom = nom
        self.types = types
        self.pv = pv
        self.pv_max = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.niveau = niveau
        self.exp = exp
        self.capacites = capacites if capacites is not None else []  # Liste des capacités
        self.evolution = evolution  # Nom du Pokémon après évolution
        self.image = None  # L'image sera chargée dynamiquement

    def charger_image(self):
        """Charge l'image du Pokémon depuis le dossier sprites/pokemon."""
        self.image = charger_image_locale(self.nom)

    def afficher(self, x, y):
        """Affiche le Pokémon à l'écran."""
        if self.image:
            screen.blit(self.image, (x, y))

    def to_dict(self):
        """Retourne un dictionnaire sérialisable représentant le Pokémon."""
        return {
            "nom": self.nom,
            "types": self.types,
            "pv": self.pv,
            "attaque": self.attaque,
            "defense": self.defense,
            "vitesse": self.vitesse,
            "niveau": self.niveau,
            "exp": self.exp,
            "capacites": self.capacites,
            "evolution": self.evolution
        }

    def __str__(self):
        return f"{self.nom} (Niveau {self.niveau}, PV: {self.pv}/{self.pv_max}, Exp: {self.exp})"

    def recevoir_degats(self, degats):
        degats_reels = max(0, degats - self.defense)
        self.pv = max(0, self.pv - degats_reels)
        print(f"{self.nom} subit {degats_reels} dégâts ! PV restants: {self.pv}/{self.pv_max}")

    def est_vivant(self):
        return self.pv > 0

    def gagner_exp(self, exp_gagnee):
        self.exp += exp_gagnee
        print(f"{self.nom} a gagné {exp_gagnee} points d'expérience !")
        if self.exp >= self.niveau * 100:  # Exemple : 100 exp par niveau
            self.monter_niveau()

    def monter_niveau(self):
        self.niveau += 1
        self.pv_max += 10
        self.attaque += 5
        self.defense += 5
        self.vitesse += 5
        self.pv = self.pv_max  # Restaure les PV
        print(f"{self.nom} monte au niveau {self.niveau} !")
        if self.evolution and self.niveau >= 10:  # Exemple : évolution au niveau 10
            self.evoluer()

    def evoluer(self):
        print(f"{self.nom} évolue en {self.evolution} !")
        self.nom = self.evolution
        self.pv_max += 20
        self.attaque += 10
        self.defense += 10
        self.vitesse += 10
        self.pv = self.pv_max

    def ajouter_capacite(self, capacite):
        if len(self.capacites) < 4:
            self.capacites.append(capacite)
            print(f"{self.nom} apprend {capacite.nom} !")
        else:
            print(f"{self.nom} ne peut pas apprendre plus de 4 capacités.")

class Capacite:
    def __init__(self, nom, puissance, type_capacite):
        self.nom = nom
        self.puissance = puissance
        self.type_capacite = type_capacite

    def __str__(self):
        return f"{self.nom} (Type: {self.type_capacite}, Puissance: {self.puissance})"

# Classe Équipe
class Equipe:
    def __init__(self):
        self.pokemons = self.charger_equipe()

    def charger_equipe(self):
        try:
            with open("pokemon.json", "r") as file:
                pokemons_data = json.load(file)
                if not isinstance(pokemons_data, list):
                    print("⚠️ Fichier mal formatté. Réinitialisation...")
                    return []
                equipe = [Pokemon(**p) for p in pokemons_data]
                for pokemon in equipe:
                    pokemon.charger_image()  # Charge les images des Pokémon
                return equipe
        except (FileNotFoundError, json.JSONDecodeError):
            print("📁 Fichier introuvable ou corrompu. Création d'un nouveau.")
            return []

    def ajouter_pokemon(self, pokemon):
        """Ajoute un Pokémon à l’équipe et le sauvegarde."""
        if len(self.pokemons) < 6:
            self.pokemons.append(pokemon)
            self.sauvegarder_equipe()
            print(f"✅ {pokemon.nom} ajouté à l’équipe !")
        else:
            print("❌ L'équipe est pleine !")

    def sauvegarder_equipe(self):
        """Sauvegarde l'équipe dans pokemon.json."""
        with open("pokemon.json", "w") as file:
            json.dump([p.to_dict() for p in self.pokemons], file, indent=4)
    def choisir_pokemon(self):
        self.afficher_equipe()
        if not self.pokemons:
            print("⚠️ Impossible de combattre, équipe vide.")
            return None

        while True:
            choix = input("\nSélectionnez un Pokémon (1-6) : ")
            if choix.isdigit():
                choix = int(choix)
                if 1 <= choix <= len(self.pokemons):
                    return self.pokemons[choix - 1]
            print("❌ Choix invalide, réessayez.")

class Combat:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.joueur = pokemon_joueur
        self.adversaire = pokemon_adversaire

    def lancer_combat(self):
        print(f"\n⚔️ Début du combat : {self.joueur.nom} VS {self.adversaire.nom} !")

        # Déterminer qui attaque en premier
        if self.joueur.vitesse > self.adversaire.vitesse:
            attaquant, defenseur = self.joueur, self.adversaire
        else:
            attaquant, defenseur = self.adversaire, self.joueur

        while self.joueur.est_vivant() and self.adversaire.est_vivant():
            # Attaque de l'attaquant
            if random.random() > 0.1:  # 10% de chance de rater
                degats = self.calculer_degats(attaquant, defenseur)
                defenseur.recevoir_degats(degats)
            else:
                print(f"💨 {attaquant.nom} rate son attaque !")

            # Vérifier si le défenseur est KO
            if not defenseur.est_vivant():
                print(f"🏆 {attaquant.nom} a gagné !")
                if attaquant == self.joueur:
                    self.joueur.gagner_exp(self.adversaire.niveau * 20)
                return

            # Changer les rôles
            attaquant, defenseur = defenseur, attaquant

    def calculer_degats(self, attaquant, defenseur):
        degats = attaquant.attaque
        for type_attaquant in attaquant.types:
            for type_defenseur in defenseur.types:
                if type_attaquant in TYPE_ADVANTAGES and type_defenseur in TYPE_ADVANTAGES[type_attaquant]:
                    degats *= TYPE_ADVANTAGES[type_attaquant][type_defenseur]
        return degats

def recuperer_pokemon(nom):
    url = f"https://pokeapi.co/api/v2/pokemon/{nom.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        types = [t["type"]["name"] for t in data["types"]]
        pv = data["stats"][0]["base_stat"]
        attaque = data["stats"][1]["base_stat"]
        defense = data["stats"][2]["base_stat"]
        vitesse = data["stats"][5]["base_stat"]
        
        return {
            "nom": data["name"].capitalize(),
            "types": types,
            "pv": pv,
            "attaque": attaque,
            "defense": defense,
            "vitesse": vitesse,
            "niveau": 1,
            "exp": 0,
            "capacites": [],
            "evolution": None  # À définir selon les besoins
        }
    else:
        print("❌ Erreur lors de la récupération du Pokémon.")
        return None

# Interface graphique avec Pygame
def afficher_texte(texte, x, y, couleur=BLACK):
    texte_surface = font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))

def main():
    equipe = Equipe()
    while True:
        screen.fill(WHITE)
        afficher_texte("🌟 MENU PRINCIPAL 🌟", 250, 50)
        afficher_texte("1. Ajouter un Pokémon", 250, 150)
        afficher_texte("2. Afficher l'équipe", 250, 200)
        afficher_texte("3. Combattre un adversaire", 250, 250)
        afficher_texte("4. Quitter", 250, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nom_pokemon = input("Entrez le nom du Pokémon à ajouter : ").strip().lower()
                    pokemon_data = recuperer_pokemon(nom_pokemon)
                    if pokemon_data:
                        pokemon = Pokemon(**pokemon_data)
                        pokemon.charger_image()  # Charge l'image du nouveau Pokémon
                        equipe.ajouter_pokemon(pokemon)
                elif event.key == pygame.K_2:
                    equipe.afficher_equipe()
                elif event.key == pygame.K_3:
                    pokemon_joueur = equipe.choisir_pokemon()
                    if pokemon_joueur:
                        adversaire_nom = random.choice(["squirtle", "charmander", "bulbasaur", "pikachu", "eevee"])
                        adversaire_data = recuperer_pokemon(adversaire_nom)
                        if adversaire_data:
                            pokemon_adversaire = Pokemon(**adversaire_data)
                            pokemon_adversaire.charger_image()  # Charge l'image de l'adversaire
                            combat = Combat(pokemon_joueur, pokemon_adversaire)
                            combat.lancer_combat()
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
