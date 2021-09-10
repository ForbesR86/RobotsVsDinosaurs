from fleet import Fleet
from herd import Herd
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    def run_game(self):
        startgame = self.display_welcome()
        if startgame == True:
            
            print("We shall begin the game.")
            playeruser = input("Would you like to be 'dinosaurs' or 'robots'?")
            print('Home field advantage for the dinos, so they go first')
            outcome = self.battle(playeruser)
            self.display_winners(outcome)
        else:
            self.run_game()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs")

        startgame = input("Would you like to begin the game?yes or no")
        if startgame == "yes":
            return True
        else:
            return False


    def battle(self, playeruser):
        turncounter = 0
        isaliven = True
        while isaliven:
            turncounter += 1
            print('Turn ', turncounter, ' :')
            self.dino_turn(playeruser)
            isaliven = self.isalive("robots")
            if isaliven == False:
                return "Dinosaurs"
            self.robo_turn(playeruser)
            isaliven = self.isalive("dinosaur")
            if isaliven == False:
                return "Robots"
            
            


    def dino_turn(self, playeruser):
        if playeruser == "dinosaurs":
            dinopick = self.show_dinos()
            targetaquired = self.show_dino_opponent_options()
            self.herd.dinosquad[dinopick].attack(self.fleet.robots[targetaquired])
        elif playeruser != "dinosaurs":
            pass
                


    def robo_turn(self, playeruser):
        if playeruser == "robots":
            robopick = self.show_robos()
            targetaquired = self.show_robo_opponent_options()
            self.fleet.robots[robopick].attack(self.herd.dinosquad[targetaquired])
        else:
            pass

                

    def show_dino_opponent_options(self):
        health1 = self.fleet.robots[0].maxHealth
        health2 = self.fleet.robots[1].maxHealth
        health3 = self.fleet.robots[2].maxHealth
        if health1 >= 0:
            print("Option 1: ", self.fleet.robots[0].name)
        else:
            print("Bot 1 ", self.fleet.robots[0].name, " is dead")

        if health2 >= 0:
            print("Option 2: ", self.fleet.robots[1].name)
        else:
            print("Bot 2 ", self.fleet.robots[1].name, " is dead")

        if health3 >= 0:
            print("Option 3: ", self.fleet.robots[2].name)
        else:
            print("Bot 3 ", self.fleet.robots[2].name, " is dead")

        thechosenone = int(input("Pick a target 1-3:")) - 1
        if self.fleet.robots[thechosenone].maxHealth <= 0:
            print(f"{self.fleet.robots[thechosenone].name} is dead! pick a new dino")
        elif self.fleet.robots[thechosenone].maxHealth > 0:
            return thechosenone
        else:
            print("Lets pick a real target please")
        


    def show_dinos(self):
        print("Option 1: ", {self.herd.dinosquad[0].name}, "with ", {self.herd.dinosquad[0].maxHealth}, " health and ", {self.herd.dinosquad[0].attackPower}, "attack power")
        print("Option 2: ", {self.herd.dinosquad[1].name}, "with ", {self.herd.dinosquad[1].maxHealth}, " health and ", {self.herd.dinosquad[1].attackPower}, "attack power")
        print("Option 3: ", {self.herd.dinosquad[2].name}, "with ", {self.herd.dinosquad[2].maxHealth}, " health and ", {self.herd.dinosquad[2].attackPower}, "attack power")
        thechosenone = int(input("Pick a dino 1-3:")) - 1
        if self.herd.dinosquad[thechosenone].maxHealth <= 0:
            print(f"{self.herd.dinosquad[thechosenone].name} is dead! pick a new dino")
        elif self.herd.dinosquad[thechosenone].maxHealth > 0:
            return thechosenone
        else:
            print("Lets pick a real dino please")
        
    def show_robo_opponent_options(self):
        if {self.herd.dinosquad[0]}.health >= 0:
            print("Option 1: ", {self.herd.dinosquad[0].name})
        else:
            print("Bot 1 ", {self.herd.dinosquad[0].name}, " is dead")

        if {self.herd.dinosquad[1]}.health >= 0:
            print("Option 2: ", {self.herd.dinosquad[1].name})
        else:
            print("Bot 2 ", {self.herd.dinosquad[1].name}, " is dead")

        if {self.herd.dinosquad[2]}.health >= 0:
            print("Option 3: ", {self.herd.dinosquad[2].name})
        else:
            print("Bot 3 ", {self.herd.dinosquad[2].name}, " is dead")

        thechosenone = input("Pick a dino 1-3:") - 1
        if self.herd.dinosquad[thechosenone].health <= 0:
            print(f"{self.herd.dinosquad[thechosenone].name} is dead! but lets go ahead and beat a dead body")
            return thechosenone
        elif self.herd.dinosquad[thechosenone].health > 0:
            return thechosenone


    def show_robos(self):
        print("Option 1: ", {self.fleet.robots[0].name}, "with ", self.fleet.robots[0].maxHealth)
        print("Option 2: ", {self.fleet.robots[1].name}, "with ", self.fleet.robots[1].maxHealth)
        print("Option 3: ", {self.fleet.robots[2].name}, "with ", self.fleet.robots[2].maxHealth)

        thechosenone = input("Pick a robot 1-3:") - 1
        
        return thechosenone
        
    
    
    def display_winners(self, outcome):
        if outcome == "Dinosaurs":
            print("Dino's win!!!!")
        elif outcome == "Robots":
            print("Robots win!!!!")
    
    def isalive(self, character):
        ##check if they are alive character = fleet/herd
        if character == "dinosaur":
            din1 = self.herd.dinosquad[0].maxHealth
            din2 = self.herd.dinosquad[1].maxHealth
            din3 = self.herd.dinosquad[2].maxHealth
            if din1 > 0 or din2 > 0 or din3 > 0:
                return True
            else:
                return False
        if character == "robots":
            rob1 = self.fleet.robots[0].maxHealth
            rob2 = self.fleet.robots[1].maxHealth
            rob3 = self.fleet.robots[2].maxHealth
            if rob1 > 0 or rob2 > 0 or rob3 > 0:
                return True
            else:
                return False

