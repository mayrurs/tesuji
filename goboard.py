from gotypes import Point

class GoString:
    def __init__(self, color: str, stones: list[Point], liberties: list[Point]):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def add_liberty(self, point: Point):
        self.liberties.add(point)



class Board:
    def __init__(self, row, col):
        pass
