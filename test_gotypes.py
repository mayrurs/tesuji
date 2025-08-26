from gotypes import Player

def test_player():
    white = Player(1)

    assert white.other == Player.black
    
