class Move:
    def __init__(self, name, power, move_type):
        self.name = name
        self.power = power
        self.move_type = move_type

    def __str__(self):
        return f"{self.name} (Type: {self.move_type}, Power: {self.power})"