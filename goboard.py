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

    def __eq__(self, other):
        return self.color == other.color and \
               self.stones == other.stones and \
               self.liberties == other.liberties


class Board:
    def __init__(self, row, col):
    def is_on_grid(self, point: Point): 
        return 1 <= point.row <= self.num_rows and 1 <= point.col <= self.num_cols

        pass
