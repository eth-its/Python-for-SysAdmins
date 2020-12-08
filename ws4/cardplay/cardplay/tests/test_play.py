from cardplay.play import Card, Deck

def test_card():
    card = Card("Hearts", "K")
    assert card == "K of Hearts"
