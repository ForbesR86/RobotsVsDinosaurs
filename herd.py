from dinosaur import Dinosaur
import random
names = ('Tyrannosaurus', 'Triceratops', 'Velociraptor', 'Stegosaurus', 'Spinosaurus', 'Archaeopteryx', 'Brachiosaurus', 'Allosaurus')
class Herd:
    def __init__(self):
        self.dinosquad = []
        self.createGoonSquad()
    def createGoonSquad(self):
        dino1 = Dinosaur(random.choice(names), random.randint(30,100), random.randint(30,100))
        dino2 = Dinosaur(random.choice(names), random.randint(30,100), random.randint(30,100))
        dino3 = Dinosaur(random.choice(names), random.randint(30,100), random.randint(30,100))
        self.dinosquad.append(dino1)
        self.dinosquad.append(dino2)
        self.dinosquad.append(dino3)
        print(dino1)