
class Character:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.defense = 5
        self.stamina = 5

    def attack(self, target):
        print("attacking")
        target.health -= self.strength - target.defense
    
    def heal(self, target):
        print("a character is healing")
        target.health += self.stamina
    
