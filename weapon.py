class Weapon:
    def __init__(self, name, attackpower):
        self.name = name
        self.attackpower = int(attackpower)
        self.weapon = []
        self.create_weapon()

    def create_weapon(self,):
        weapon1 = Weapon("Sword", 80)
        weapon2 = Weapon("Blaster", 100)
        weapon3 = Weapon("Rifle", 110)
        self.weapon.append(weapon1)
        self.weapon.append(weapon2)
        self.weapon.append(weapon3)
