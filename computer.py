
from player import Player
import random


class Computer(Player):

    def __init__(self, name):
        super().__init__(name)

    def select_gesture(self, list):
        return random.choice(list)
