from computer import Computer
from human import Human
from player import Player
import random


class Game:

    def __init__(self):
        self.player = Player()
        self.player_1 = Human()
        self.player_2 = Human()
        self.computer = Computer()
        self.run_game()

    def run_game(self):
        self.display_rules()
        user_input = input(
            "Please select Single Player[1] or Multi-Player[2] Please Type: '1' or '2'.     :")
        if user_input == "1":
            self.single_play()
        elif user_input == "2":
            self.multi_play()

    def display_rules(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        print("The rules of the game are:")
        print("Rock crushes Scissors")
        print("Scissors cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitate Lizard")

    def play1_choice(self, player1, list_of_gestures):
        player_one_choice = player1.player_selection(
            list_of_gestures)
        return player_one_choice

    def play2_choice(self, player2, list_of_gestures):
        player_two_choice = player2.player_selection(
            list_of_gestures)
        return player_two_choice

    def comp_choice(self, AI, list_of_gestures):
        computer_choice = AI.comp_selection(list_of_gestures)
        return computer_choice

    def multi_play(self):

        print("Player 1")
        p1_pick = self.play1_choice(self.player_1, self.player.gestures)
        print("Player2")
        p2_pick = self.play1_choice(self.player_1, self.player.gestures)

    def single_play(self):
        print("Player 1")
        p1_pick = self.play1_choice(self.player_1, self.player.gestures)
        print("Computer Selection:")
        AI_pick = self.comp_choice(self.computer, self.player.gestures)

    def display_winnner(self):
        # display the winner and ask if the users want to play again.
        pass
