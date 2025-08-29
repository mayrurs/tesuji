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

def test_point_neighbors(): 
    point = Point(2,2)

    assert point.neighbors == [
        Point(1,2), Point(2,3), Point(3,2), Point(2,1)
    ]
    
