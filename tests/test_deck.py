from blackjack.deck import Deck
import pytest

@pytest.fixture
def example_deck():
    return Deck()


def test_example_deck_len(example_deck):
    assert len(example_deck.all_cards) == 52


def test_example_deck_shuffled(example_deck):
    old_first_card = example_deck.all_cards[0]
    example_deck.shuffle()
    new_first_card = example_deck.all_cards[0]
    assert old_first_card != new_first_card