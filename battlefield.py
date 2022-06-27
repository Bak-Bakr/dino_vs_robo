from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self,):
        self.robot = Robot("Optimus")
        self.dinosaur = Dinosaur("T-Rex", 50)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        pass

    def battle_phase(self):
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        pass

    

