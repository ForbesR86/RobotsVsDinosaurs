class Dinosaur:
    def __init__(self, name, randomHealth, randomAttackP):
        self.name = name
        self.maxHealth = randomHealth
        self.attackPower = randomAttackP

    def attack(self, robot):
        robot.maxHealth -= self.attackPower
        print(self.name, 'hits ', robot.name, ' for ', self.attackPower)