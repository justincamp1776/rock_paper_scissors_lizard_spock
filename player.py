class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = []
        self.create_list()

    # List of gestures
    def create_list(self):
        self.gestures.append("rock")
        self.gestures.append("paper")
        self.gestures.append("scissors")
        self.gestures.append("lizard")
        self.gestures.append("spock")

    # Allows user to select a gesture
    def select_gesture(self, list_of_gestures):
        valid = False
        while not valid:
            self.display_gestures(self.gestures)
            user_input = input(
                "Please type your selection from the list above  ")
            for index in list_of_gestures:
                if user_input.lower() == index:
                    valid = True
                    return index
            else:
                print("Entry invalid. Please Try again")

    # Displays list of gestures
    def display_gestures(self, list):
        print(list)
