from random import choice

from fluent.cards import Card, Deck


def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck) == 52


def test_can_pick_card_by_location():
    deck = Deck()
    assert deck[0] == Card("2", "spades")


def test_get_random_card():
    deck = Deck()
    card_1 = choice(deck)
    assert card_1


def test_can_slice_deck():
    deck = Deck()
    first_three = deck[:3]
    assert first_three == [
        Card("2", "spades"),
        Card("3", "spades"),
        Card("4", "spades"),
    ]


def test_card_in_deck():
    deck = Deck()
    # performs a sequential scan
    assert Card("Q", "hearts") in deck
    assert Card("2", "dogs") not in deck
