import json
import random
import requests
import pygame
import sys
import os  
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



# Chemins des dossiers de sprites
DOSSIER_SPRITES_JOUEUR = os.path.join("sprites", "sprites", "pokemon", "back")
DOSSIER_SPRITES_ADVERSAIRE = os.path.join("sprites", "sprites", "pokemon")
# Fonction pour charger une image locale
def charger_image_locale(numero, est_joueur=True):
    """Charge une image depuis le dossier de sprites en utilisant le numéro."""
    try:
        if est_joueur:
            chemin = os.path.join(DOSSIER_SPRITES_JOUEUR, f"{numero}.png")
        else:
            chemin = os.path.join(DOSSIER_SPRITES_ADVERSAIRE, f"{numero}.png")
        if os.path.exists(chemin):
            return pygame.image.load(chemin)
        else:
            print(f"❌ Fichier introuvable : {chemin}")
            return None
    except Exception as e:
        print(f"❌ Erreur lors du chargement de l'image pour le Pokémon n°{numero}: {e}")
        return None
# Classe Pokémon
class Pokemon:
    def __init__(self, nom, types, pv, attaque, defense, vitesse, niveau=1, exp=0, capacites=None, evolution=None, est_joueur=True):
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
        self.est_joueur = est_joueur  # True si c'est un Pokémon du joueur, False si c'est un adversaire
        self.image = None  # L'image sera chargée dynamiquement
        self.numero = self.recuperer_numero()  # Numéro du Pokémon
        self.charger_image()

class Pokemon:
    def __init__(self, nom, types, pv, attaque, defense, vitesse, niveau=5, exp=0, capacites=None, evolution=None, est_joueur=True):
        self.nom = nom
        self.types = types
        self.pv = pv
        self.pv_max = pv
        self.attaque = attaque
        self.defense = defense
        self.vitesse = vitesse
        self.niveau = niveau
        self.exp = exp
        self.capacites = capacites if capacites is not None else []
        self.evolution = evolution
        self.est_joueur = est_joueur
        self.image = None
        self.numero = self.recuperer_numero()  # Appel de la méthode
        self.charger_image()
        self.mettre_a_jour_capacites()

    def recuperer_numero(self):
        """Récupère le numéro du Pokémon depuis l'API."""
        url = f"https://pokeapi.co/api/v2/pokemon/{self.nom.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["id"]  # Numéro du Pokémon
        else:
            print(f"❌ Erreur lors de la récupération du numéro pour {self.nom}.")
            return None

    def charger_image(self):
        """Charge l'image du Pokémon depuis le dossier de sprites."""
        if self.numero:
            self.image = charger_image_locale(self.numero, self.est_joueur)
    def afficher(self, x, y):
        """Affiche le Pokémon à l'écran."""
        if self.image:
            screen.blit(self.image, (x, y))

    def recevoir_degats(self, degats):
        """Réduit les PV du Pokémon en fonction des dégâts reçus."""
        degats_reels = max(0, degats - self.defense)
        self.pv = max(0, self.pv - degats_reels)
        print(f"{self.nom} subit {degats_reels} dégâts ! PV restants: {self.pv}/{self.pv_max}")

    def est_vivant(self):
        """Retourne True si le Pokémon a encore des PV."""
        return self.pv > 0

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
            "capacites": [c.__dict__ for c in self.capacites],
            "evolution": self.evolution,
            "est_joueur": self.est_joueur
        }

    def monter_niveau(self):
        """Fait monter le Pokémon de niveau et met à jour ses capacités."""
        self.niveau += 1
        self.pv_max += 10
        self.attaque += 5
        self.defense += 5
        self.vitesse += 5
        self.pv = self.pv_max  # Restaure les PV
        print(f"{self.nom} monte au niveau {self.niveau} !")
        self.mettre_a_jour_capacites()

    def evoluer(self):
        """Fait évoluer le Pokémon et met à jour ses capacités."""
        if self.evolution:
            print(f"{self.nom} évolue en {self.evolution} !")
            self.nom = self.evolution
            self.pv_max += 20
            self.attaque += 10
            self.defense += 10
            self.vitesse += 10
            self.pv = self.pv_max
            self.charger_image()
            self.mettre_a_jour_capacites()

def mettre_a_jour_capacites(self):
    """Met à jour les capacités du Pokémon en utilisant l'API."""
    url = f"https://pokeapi.co/api/v2/pokemon/{self.nom.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        self.capacites = []
        for move in data["moves"]:
            # Vérifie si la capacité est apprise au niveau actuel
            for version in move["version_group_details"]:
                if version["level_learned_at"] <= self.niveau:
                    capacite_nom = move["move"]["name"]
                    capacite_url = move["move"]["url"]
                    capacite_data = requests.get(capacite_url).json()
                    # Récupère la puissance de la capacité (40 par défaut si non spécifiée)
                    capacite_puissance = capacite_data.get("power", 40)
                    # Récupère le type de la capacité
                    capacite_type = capacite_data["type"]["name"] if "type" in capacite_data else "normal"
                    self.capacites.append(Capacite(capacite_nom, capacite_puissance, capacite_type))
        
        # Si aucune capacité n'a été trouvée, ajouter des capacités par défaut
        if not self.capacites:
            if "electric" in self.types:
                self.capacites.append(Capacite("Éclair", 40, "electric"))
            if "psychic" in self.types:
                self.capacites.append(Capacite("Psyko", 90, "psychic"))
            if "fire" in self.types:
                self.capacites.append(Capacite("Lance-Flammes", 90, "fire"))
            if "water" in self.types:
                self.capacites.append(Capacite("Hydrocanon", 110, "water"))
            if "grass" in self.types:
                self.capacites.append(Capacite("Fouet Lianes", 45, "grass"))
        
        print(f"{self.nom} a appris de nouvelles capacités !")
    else:
        print(f"❌ Erreur lors de la récupération des capacités pour {self.nom}.")

class Capacite:
    def __init__(self, nom, puissance, type_capacite):
        self.nom = nom
        self.puissance = puissance
        self.type_capacite = type_capacite

    def __str__(self):
        return f"{self.nom} (Type: {self.type_capacite}, Puissance: {self.puissance})"
    
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
            self.afficher_equipe()
        else:
            print("❌ L'équipe est pleine !")

    def sauvegarder_equipe(self):
        """Sauvegarde l'équipe dans pokemon.json."""
        with open("pokemon.json", "w") as file:
            json.dump([p.to_dict() for p in self.pokemons], file, indent=4)

    def afficher_equipe(self):
        """Affiche les Pokémon de l'équipe à l'écran."""
        screen.fill(WHITE)
        y = 50
        for pokemon in self.pokemons:
            pokemon.afficher(100, y)
            y += 120  # Espacement entre les Pokémon
        pygame.display.flip()

    def choisir_pokemon(self):
        """Permet au joueur de choisir un Pokémon pour le combat."""
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

# Classe Combat

class Combat:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.joueur = pokemon_joueur
        self.adversaire = pokemon_adversaire

    def afficher_interface(self):
        """Affiche l'interface de combat."""
        screen.fill(WHITE)
        # Afficher le Pokémon du joueur
        self.joueur.afficher(100, 400)
        afficher_texte(f"{self.joueur.nom} (PV: {self.joueur.pv}/{self.joueur.pv_max})", 100, 380)
        # Afficher le Pokémon adverse
        self.adversaire.afficher(500, 100)
        afficher_texte(f"{self.adversaire.nom} (PV: {self.adversaire.pv}/{self.adversaire.pv_max})", 500, 80)
        pygame.display.flip()

    def lancer_combat(self):
        """Gère le combat entre les deux Pokémon."""
        print(f"\n⚔️ Début du combat : {self.joueur.nom} VS {self.adversaire.nom} !")

        while self.joueur.est_vivant() and self.adversaire.est_vivant():
            self.afficher_interface()
            # Tour du joueur
            if self.joueur.capacites:
                print("\nChoisissez une attaque :")
                for i, capacite in enumerate(self.joueur.capacites, start=1):
                    print(f"{i}. {capacite}")
                choix = input("👉 Votre choix : ")
                if choix.isdigit():
                    choix = int(choix)
                    if 1 <= choix <= len(self.joueur.capacites):
                        capacite = self.joueur.capacites[choix - 1]
                        degats = self.calculer_degats(self.joueur, self.adversaire, capacite)
                        self.adversaire.recevoir_degats(degats)
                    else:
                        print("❌ Choix invalide, réessayez.")
                else:
                    print("❌ Choix invalide, réessayez.")
            else:
                print(f"{self.joueur.nom} n'a aucune capacité !")

            # Vérifie si l'adversaire est KO
            if not self.adversaire.est_vivant():
                print(f"🏆 {self.joueur.nom} a gagné !")
                return

            # Tour de l'adversaire
            if self.adversaire.capacites:
                if random.random() > 0.1:  # 10% de chance de rater
                    capacite = random.choice(self.adversaire.capacites)
                    degats = self.calculer_degats(self.adversaire, self.joueur, capacite)
                    self.joueur.recevoir_degats(degats)
                else:
                    print(f"💨 {self.adversaire.nom} rate son attaque !")
            else:
                print(f"{self.adversaire.nom} n'a aucune capacité !")

        print(f"💀 {self.joueur.nom} a perdu le combat...")

    def calculer_degats(self, attaquant, defenseur, capacite):
        """Calcule les dégâts en fonction des types et de la défense."""
        degats = capacite.puissance
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

# Classe Pokédex
class Pokedex:
    def __init__(self):
        self.pokemons = self.charger_pokedex()

    def charger_pokedex(self):
        try:
            with open("pokedex.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def ajouter_pokemon(self, pokemon):
        """Ajoute un Pokémon au Pokédex s'il n'existe pas déjà."""
        if pokemon.nom not in [p["nom"] for p in self.pokemons]:
            self.pokemons.append(pokemon.to_dict())
            self.sauvegarder_pokedex()
            print(f"✅ {pokemon.nom} ajouté au Pokédex !")
        else:
            print(f"⚠️ {pokemon.nom} est déjà dans le Pokédex.")

    def sauvegarder_pokedex(self):
        """Sauvegarde le Pokédex dans pokedex.json."""
        with open("pokedex.json", "w") as file:
            json.dump(self.pokemons, file, indent=4)

    def afficher_pokedex(self):
        """Affiche le Pokédex."""
        if not self.pokemons:
            print("📁 Le Pokédex est vide.")
        else:
            print("\n📘 POKÉDEX :")
            for pokemon in self.pokemons:
                print(f"- {pokemon['nom']} (Type: {', '.join(pokemon['types'])})")

# Fonction principale
def main():
    equipe = Equipe()
    pokedex = Pokedex()

    while True:
        screen.fill(WHITE)
        afficher_texte("🌟 MENU PRINCIPAL 🌟", 250, 50)
        afficher_texte("1. Ajouter un Pokémon", 250, 150)
        afficher_texte("2. Afficher l'équipe", 250, 200)
        afficher_texte("3. Combattre un adversaire", 250, 250)
        afficher_texte("4. Afficher le Pokédex", 250, 300)
        afficher_texte("5. Quitter", 250, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nom_pokemon = input("Entrez le nom du Pokémon à ajouter : ").strip().lower()
                    pokemon_data = recuperer_pokemon(nom_pokemon)
                    if pokemon_data:
                        pokemon = Pokemon(**pokemon_data, est_joueur=True)
                        equipe.ajouter_pokemon(pokemon)
                        pokedex.ajouter_pokemon(pokemon)
                elif event.key == pygame.K_2:
                    equipe.afficher_equipe()
                elif event.key == pygame.K_3:
                    pokemon_joueur = equipe.choisir_pokemon()
                    if pokemon_joueur:
                        adversaire_nom = random.choice(["squirtle", "charmander", "bulbasaur", "pikachu", "eevee"])
                        adversaire_data = recuperer_pokemon(adversaire_nom)
                        if adversaire_data:
                            pokemon_adversaire = Pokemon(**adversaire_data, est_joueur=False)
                            combat = Combat(pokemon_joueur, pokemon_adversaire)
                            combat.lancer_combat()
                elif event.key == pygame.K_4:
                    pokedex.afficher_pokedex()
                elif event.key == pygame.K_5:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()