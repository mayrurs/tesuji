from gotypes import Point

class GoString:
    def __init__(self, color: str, stones: list[Point], liberties: list[Point]):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point:Point):
        self.liberties.remove(point)

    def add_liberty(self, point: Point):
        self.liberties.add(point)

    def merge_with(self, other: GoString):
        assert self.color == other.color
        stones = self.stones | other.stones
        liberties = (self.liberties | other.liberties) - stones
        return GoString(self.color, stones, liberties)

    @property
    def num_liberties(self):
        return len(self.liberties)



class Board:
    def __init__(self, row, col):
        pass
