from goboard import GoString
from gotypes import Point

def test_add_liberty():
    stones = [Point(1,1), Point(1,2)]
    liberties = []
    gostring = GoString(color="black", stones=stones, liberties=liberties)

    liberty = Point(2,1)
    gostring.add_liberty(liberty)

    assert liberty in gostring.liberties


