from computer import Computer
from human import Human
from player import Player
import random


class Game:

    def __init__(self):

        self.player_1 = None
        self.player_2 = None
        self.run_game()

    # Instantiates 2 objects and assigns them as values to attribute player_1 and attribute player_2
    def run_game(self):
        self.display_rules()
        user_input = input(
            "Please select Single Player[1] or Multi-Player[2] Please Type: '1' or '2'  ")
        if user_input == "1":
            self.player_1 = Human(input("Please enter Player 1's name :"))
            self.player_2 = Computer("AI")
            self.play_game()
        elif user_input == "2":
            self.player_1 = Human(input("Please enter Player 1's name  "))
            self.player_2 = Human(input("Please enter Player 2's name  "))
            self.play_game()

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

    # Prompts user to select_gesture and calls determine_winner

    def play_game(self):
        print(f'{self.player_1.name}, make the first move!')
        while self.player_1.score < 2 or self.player_2.score < 2:
            p1_pick = self.player_1.select_gesture(self.player_1.gestures)
            print(f'{self.player_1.name} selects: {p1_pick}')
            p2_pick = self.player_2.select_gesture(self.player_2.gestures)
            print(f'{self.player_2.name} selects: {p2_pick}')
            self.decide_winner(p1_pick, p2_pick, self.player_1.gestures)
            if self.player_1.score == 2:
                self.display_winner(self.player_1)
            elif self.player_2.score == 2:
                self.display_winner(self.player_2)

    def decide_winner(self, p1, p2, list):

        # compares opponents gesture to rock rules
        if p1 == list[0]:
            if p2 == list[2] or p2 == list[3]:
                self.player_1.score += 1
                print(f'{self.player_1.name} wins the round!')
        if p2 == list[0]:
            if p1 == list[2] or p1 == list[3]:
                self.player_2.score += 1
                print(f'{self.player_2.name} wins the round!')

        # compares opponents gesture to paper rules
        if p1 == list[1]:
            if p2 == list[0] or p2 == list[4]:
                self.player_1.score += 1
                print(f'{self.player_1.name} wins the round!')
        if p2 == list[1]:
            if p1 == list[0] or p1 == list[4]:
                self.player_2.score += 1
                print(f'{self.player_2.name} wins the round!')

        # compares opponents gesture to scissors rules
        if p1 == list[2]:
            if p2 == list[1] or p2 == list[3]:
                self.player_1.score += 1
                print(f'{self.player_1.name} wins the round!')
        if p2 == list[2]:
            if p1 == list[1] or p1 == list[3]:
                self.player_2.score += 1
                print(f'{self.player_2.name} wins the round!')

        # compares opponents gesture to lizard rules
        if p1 == list[3]:
            if p2 == list[4] or p2 == list[1]:
                self.player_1.score += 1
                print(f'{self.player_1.name} wins the round!')
        if p2 == list[3]:
            if p1 == list[4] or p1 == list[1]:
                self.player_2.score += 1
                print(f'{self.player_2.name} wins the round!')

        # compares opponents gesture to spock rules
        if p1 == list[4]:
            if p2 == list[2] or p2 == list[0]:
                self.player_1.score += 1
                print(f'{self.player_1.name} wins the round!')
        if p2 == list[4]:
            if p1 == list[2] or p1 == list[0]:
                self.player_2.score += 1
                print(f'{self.player_2.name} wins the round!')

    # Displays the winner and asks user if they would like to play again
    def display_winner(self, player):
        print(f'{player.name} wins the game!!!')
        valid = False
        while not valid:
            user_input = input(
                "Would you like a Rematch[1] or Main Menu[2]? Enter '1' or '2'  ")
            if user_input.upper() == "1".upper():
                valid = True
                self.player_1.score = 0
                self.player_2.score = 0
                self.play_game()
            elif user_input.upper() == "2".upper():
                valid = True
                self.run_game()
