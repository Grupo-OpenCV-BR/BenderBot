class Bot:
    token = ''


    def __init__(self, offenseOn, muteOn):
        self.offenseOn = offenseOn
        self.mute = muteOn

    def welcome(self):
        ...

    def goodbye(self):
        ...

    def offense(self):
        ...
