from config import TELEGRAM_TOKEN


class Bot:
    token = TELEGRAM_TOKEN

    def __init__(self, offenseOn, muteOn):
        self.offenseOn = offenseOn
        self.mute = muteOn

    def welcome(self):
        ...

    def goodbye(self):
        ...

    def offense(self):
        ...
