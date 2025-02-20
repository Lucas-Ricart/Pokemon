import json

class Pokemon:
    def __init__(self, id, name, type, hp, attack, defense, special_attack, special_defense, speed, base_xp, evolution, lv = 5):
        self.id = id
        self.name = name
        self.type = type
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.base_special_attack = special_attack
        self.base_special_defense = special_defense
        self.base_speed = speed
        self.base_xp = base_xp
        self.evolution = evolution
        self.lv = lv
        self.need_xp = 0.8*(self.lv**3)

    def __str__(self):
        return f"{self.id} : {self.name} - {self.need_xp}"

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            type=data["type"],
            hp=data["hp"],
            attack=data["attack"],
            defense=data["defense"],
            special_attack=data["special_attack"],
            special_defense=data["special_defense"],
            speed=data["speed"],
            base_xp=data["base_xp"],
            evolution=data.get("evolution", None)
        )

# Charger les données JSON depuis un fichier
with open("list_pokemon.json", "r") as file:
    data = json.load(file)

# Créer une liste d'objets Pokemon
pokemon_list = [Pokemon.from_dict(p) for p in data.values()]

# Afficher les Pokémon chargés
for pokemon in pokemon_list:
    print(pokemon)


print(pokemon)
