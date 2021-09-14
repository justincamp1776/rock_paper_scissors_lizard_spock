
from player import Player
import random


class Computer(Player):

    # Inherits from Player and Overrides select_gesture function
    def __init__(self, name):
        super().__init__(name)

    def select_gesture(self, list):
        return random.choice(list)
