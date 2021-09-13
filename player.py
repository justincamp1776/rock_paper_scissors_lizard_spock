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
