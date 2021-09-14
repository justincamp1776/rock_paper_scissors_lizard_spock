
from player import Player
import random


class Computer(Player):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def comp_selection(self, list):
        return random.choice(list)
