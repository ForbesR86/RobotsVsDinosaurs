from weapon import Weapon
class Robot:
    def __init__(self, name, randomHealth):
        self.name = name
        self.maxHealth = randomHealth
        self.weapon = []
        self.create_weapon()
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attackpower
    def create_weapon(self,):
        weapon1 = Weapon("Sword", 80)
        weapon2 = Weapon("Blaster", 100)
        weapon3 = Weapon("Rifle", 110)
        self.weapon.append(weapon1)
        self.weapon.append(weapon2)
        self.weapon.append(weapon3)