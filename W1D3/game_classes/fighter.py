from game_classes.character import Character
import random

class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.defense = 8
        self.weapon_damage = 5

    def rally_cry(self):
        print("This is Sparta!")
        self.stamina += 5

    def attack(self, target):
        print("fighter attacks")
        # super().attack(target)
        damage = self.strength + self.weapon_damage - target.defense
        target.health -= damage
        roll = random.randint(1,20)
        if (roll > 18):
            target.health -= self.weapon_damage

    

