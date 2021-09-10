from weapon import Weapon
class Robot:
    def __init__(self, name, randomHealth, weapon):
        self.name = name
        self.maxHealth = randomHealth
        self.weapon = weapon

    def attack(self, dinosaur):
        # dinosaur.maxHealth -= self.weapon.attackpower
        dinosaur.maxHealth -= 50
    