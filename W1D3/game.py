from game_classes.fighter import Fighter
from game_classes.monk import Monk
import random

monk = Monk()
fighter = Fighter()

print("Welcome to Monk vs Fighter, you are the Monk")
while monk.health > 0 and fighter.health > 0:

    response = input("Will you 1) Attack or 2)Heal")
    if response == "1":
        monk.attack(fighter)
    if response == "2":
        monk.heal()
    roll = random.randint(1,2)
    if roll == 1:
        fighter.attack(monk)
    if roll == 2:
        fighter.heal(fighter)

    print(f"Monk's health is {monk.health}")
    print(f"Fighters's health is {fighter.health}")
    
print("Game Over")
# response = input("Please respond: \n >")
# print(f"You responded with {response}")