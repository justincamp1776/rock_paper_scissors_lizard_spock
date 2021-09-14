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

    def choose_gesture(self):
        # JJ TODO: Override this method in the Human and Computer classes
        # the result will always be the same (returns a string gesture)
        pass
