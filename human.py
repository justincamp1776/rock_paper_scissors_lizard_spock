
from player import Player


class Human(Player):

    # what is has
    def __init__(self):
        super().__init__()

    def select_gesture(self, list_of_gestures):
        self.display_gestures(self.gestures)
        user_input = input("Please type your selection from the list above  :")

        if user_input.upper() == list_of_gestures[0].upper():
            return list_of_gestures[0]
        elif user_input.upper() == list_of_gestures[1].upper():
            return list_of_gestures[1]
        elif user_input.upper() == list_of_gestures[2].upper():
            return list_of_gestures[2]
        elif user_input.upper() == list_of_gestures[3].upper():
            return list_of_gestures[3]
        elif user_input.upper() == list_of_gestures[4].upper():
            return list_of_gestures[4]
        else:
            print("Entry invalid. Please Try again")
            self.player_selection(self, list_of_gestures)
