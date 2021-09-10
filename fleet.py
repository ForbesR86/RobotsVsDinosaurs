from robot import Robot
import random
first_names = ("Brett","Cash","David", "JJ", "Megan", "Nevin", "Pascal")
class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    def create_fleet(self):
        full_name1=random.choice(first_names) + str(random.randint(1000,9999))
        full_name2=random.choice(first_names) + str(random.randint(1000,9999))
        full_name3=random.choice(first_names) + str(random.randint(1000,9999))

        Robot1 = Robot(full_name1,random.randint(80,100))
        Robot2 = Robot(full_name2,random.randint(80,100))
        Robot3 = Robot(full_name3,random.randint(80,100))
        self.robots.append(Robot1)
        self.robots.append(Robot2)
        self.robots.append(Robot3)
