import enum

class Player(enum.Enum):
    white = 1
    black = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white



