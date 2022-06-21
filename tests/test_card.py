from blackjack.card import Card
import pytest

@pytest.fixture
def example_card():
    return Card("Diamonds","Two")


def test_example_card_suit(example_card):
    assert example_card.suit == "Diamonds"


def test_example_card_rank(example_card):
    assert example_card.rank == "Two"


def test_example_card_value(example_card):
    assert example_card.value == 2
