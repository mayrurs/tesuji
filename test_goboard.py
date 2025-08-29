from goboard import GoString
from gotypes import Point

def test_add_liberty():
    stones = [Point(1,1), Point(1,2)]
    liberties = []
    gostring = GoString(color="black", stones=stones, liberties=liberties)

    liberty = Point(2,1)
    gostring.add_liberty(liberty)

    assert liberty in gostring.liberties

def test_remove_liberty():
    stones = [Point(1,1), Point(1,2)]
    liberty = Point(2,1)
    liberties = [liberty]
    gostring = GoString(color="black", stones=stones, liberties=liberties)

    gostring.remove_liberty(liberty)

    assert liberty not in gostring.liberties

def test_merge_with():
    gostring1 = GoString(color="black", stones=[Point(1,1), Point(2,1)], liberties=[Point(1,2), Point(2,2), Point(3,1)])
    gostring2 = GoString(color="black", stones=[Point(3,1)], liberties=[Point(3,2), Point(4,1)])

    merged_string = gostring1.merge_with(gostring2)

    assert merged_string.stones == set([Point(1,1), Point(2,1), Point(3,1)])
    assert merged_string.liberties  == set([Point(1,2), Point(2,2), Point(3,2), Point(4,1)])

def test_return_gostring_len():
    gostring = GoString(color="black", stones=[Point(1,1), Point(2,1)], liberties=[Point(1,2), Point(2,2), Point(3,1)])

    assert gostring.num_liberties == 3

def test_point_is_on_grid_returns_true():
    board = Board(3,3)
    point1 = Point(1,1)
    point2 = Point(3,3)

    assert board.is_on_grid(point1)
    assert board.is_on_grid(point2)

def test_point_is_not_on_grid_returns_false():
    board = Board(3,3)
    point1 = Point(0,1)
    point2 = Point(4,4)

    assert board.is_on_grid(point1) is False
    assert board.is_on_grid(point2) is False

