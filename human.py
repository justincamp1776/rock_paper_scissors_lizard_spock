
from player import Player


class Human(Player):

    # what is has
    def __init__(self, name):
        self.name = name
        super().__init__()
