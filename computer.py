
from player import Player
import random


class Computer(Player):

    def __init__(self):
        super().__init__()

    def comp_selection(self):
        print("Computer Selection:")
        return random.choice(self.gestures)
