from weapon import Weapon
class Robot:
    def __init__(self, name, randomHealth):
        self.name = name
        self.maxHealth = randomHealth
        self.weapon = []
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attackpower