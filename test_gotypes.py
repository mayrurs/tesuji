import bz2
from gotypes import Player
from gotypes import Point

def test_player():
    white = Player(1)
    black = Player(2)

    assert white.other == Player.black
    assert black.other == Player.white

def test_point():
    p1 = Point(3,2)
    assert p1.row == 3
    assert p1.col == 2

    
