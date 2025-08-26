from gotypes import Player

def test_player():
    white = Player(1)
    black = Player(2)

    assert white.other == Player.black
    assert black.other == Player.white

    
