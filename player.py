class Player:

    def __init__(self):

        self.gestures = []
        self.create_list()

    def create_list(self):
        self.gestures.append("rock")
        self.gestures.append("paper")
        self.gestures.append("scissors")
        self.gestures.append("lizard")
        self.gestures.append("spock")

    def display_gestures(self, list):
        print(list)

    def select_gesture(self, list_of_gestures):

        valid = False
        while not valid:
            self.display_gestures(self.gestures)
            user_input = input(
                "Please type your selection from the list above  :")
            if user_input.upper() == list_of_gestures[0].upper():
                valid = True
                return list_of_gestures[0]
            elif user_input.upper() == list_of_gestures[1].upper():
                valid = True
                return list_of_gestures[1]
            elif user_input.upper() == list_of_gestures[2].upper():
                valid = True
                return list_of_gestures[2]
            elif user_input.upper() == list_of_gestures[3].upper():
                valid = True
                return list_of_gestures[3]
            elif user_input.upper() == list_of_gestures[4].upper():
                valid = True
                return list_of_gestures[4]
            else:
                print("Entry invalid. Please Try again")
