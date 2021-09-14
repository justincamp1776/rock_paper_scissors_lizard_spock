from computer import Computer
from human import Human
from player import Player
import random


class Game:

    def __init__(self):
        """
        JJ TODO: Refactor so that Game only has two player attributes: self.player_1 and self.player_2
        Based on the user's selection of single or multiplayer, these will be assigned to either Human and Human or Human and Computer
        """
        self.player = Player()
        self.player_1 = Human("Player 1")
        self.player_2 = Human("Player 2")
        self.computer = Computer("AI")
        self.p1_wins = []
        self.p2_wins = []
        self.run_game()

    def run_game(self):
        self.display_rules()
        user_input = input(
            "Please select Single Player[1] or Multi-Player[2] Please Type: '1' or '2'.  :")
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
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")

    def play1_choice(self, player1, list_of_gestures):
        player_one_choice = player1.select_gesture(
            list_of_gestures)
        return player_one_choice

    def play2_choice(self, player2, list_of_gestures):
        player_two_choice = player2.select_gesture(
            list_of_gestures)
        return player_two_choice

    def comp_choice(self, AI, list_of_gestures):
        computer_choice = AI.comp_selection(list_of_gestures)
        return computer_choice

    def multi_play(self):
        while len(self.p1_wins) < 2 or len(self.p2_wins < 2):
            print("Player One's Turn")
            p1_pick = self.play1_choice(self.player_1, self.player.gestures)
            print(f'Player 1 selects: {p1_pick}')
            print("Player Two's Turn")
            p2_pick = self.play2_choice(self.player_2, self.player.gestures)
            print(f'Player 2 selects: {p2_pick}')
            self.decide_winner(p1_pick, p2_pick, self.player.gestures)
            if len(self.p1_wins) == 2:
                self.display_winner(self.player_1)
            elif len(self.p2_wins) == 2:
                self.display_winner(self.player_2)

    def single_play(self):
        while len(self.p1_wins) < 2 or len(self.p2_wins) < 2:
            print("Player One's Turn")
            p1_pick = self.play1_choice(self.player_1, self.player.gestures)
            print(f'Player 1 selects: {p1_pick}')
            AI_pick = self.comp_choice(self.computer, self.player.gestures)
            print(f'Player 2 selects: {AI_pick}')
            self.decide_winner(p1_pick, AI_pick, self.player.gestures)
            if len(self.p1_wins) == 2:
                self.display_winner(self.player_1)
            elif len(self.p2_wins) == 2:
                self.display_winner(self.computer)

    def decide_winner(self, p1, p2, list):
        # rock
        if p1 == list[0]:
            if p2 == list[2] or p2 == list[3]:
                self.p1_wins.append("win")
                print("Player 1 wins the round.")
        if p2 == list[0]:
            if p1 == list[2] or p1 == list[3]:
                self.p2_wins.append("win")
                print("Player 2 wins the round.")

        # paper
        if p1 == list[1]:
            if p2 == list[0] or p2 == list[4]:
                self.p1_wins.append("win")
                print("Player 1 wins the round.")
        if p2 == list[1]:
            if p1 == list[0] or p1 == list[4]:
                self.p2_wins.append("win")
                print("Player 2 wins the round.")

        # scissors
        if p1 == list[2]:
            if p2 == list[1] or p2 == list[3]:
                self.p1_wins.append("win")
                print("Player 1 wins the round.")
        if p2 == list[2]:
            if p1 == list[1] or p1 == list[3]:
                self.p2_wins.append("win")
                print("Player 2 wins the round.")

        # lizard
        if p1 == list[3]:
            if p2 == list[4] or p2 == list[1]:
                self.p1_wins.append("win")
                print("Player 1 wins the round.")
        if p2 == list[3]:
            if p1 == list[4] or p1 == list[1]:
                self.p2_wins.append("win")
                print("Player 2 wins the round!")

        # spock
        if p1 == list[4]:
            if p2 == list[2] or p2 == list[0]:
                self.p1_wins.append("win")
                print("Player 1 wins the round!")
        if p2 == list[4]:
            if p1 == list[2] or p1 == list[0]:
                self.p2_wins.append("win")
                print("Player 2 wins the round!")

    def display_winner(self, player):
        print(f'{player.name} wins the game!!!')
        user_input = input(
            "Would you like to play again? Enter 'yes' or 'no'.  :")
        if user_input.upper() == "yes".upper():
            self.p1_wins = []
            self.p2_wins = []
            self.run_game()
