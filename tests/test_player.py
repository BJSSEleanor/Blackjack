from blackjack.player import Player
from blackjack.deck import Deck
import pytest

@pytest.fixture
def example_player():
    return Player("Eleanor")


def test_example_player_name(example_player):
    assert example_player.name == "Eleanor"


def test_example_player_empty_deck_initially(example_player):
    assert example_player.all_cards == []


@pytest.fixture
def example_deck():
    return Deck()
    

def test_player_given_one_card(example_player,example_deck):
    example_deck.shuffle()
    new_card = example_deck.deal_one()
    example_player.add_cards(new_card)
    assert example_player.all_cards == [new_card]


def test_player_given_multiple_cards(example_player,example_deck):
    example_deck.shuffle()
    new_cards = []
    for num in range(0,3):
        card = example_deck.deal_one()
        new_cards.append(card)
    example_player.add_cards(new_cards)
    assert example_player.all_cards == new_cards