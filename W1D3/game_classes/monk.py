from game_classes.character import Character

class Monk(Character):
    def __init__(self):
        super().__init__()
        self.stamina = 10

    def heal(self):
        heal_val = (self.health / 10 ) * self.stamina
        print(f"Monk heals for {heal_val}")
        self.health += heal_val