from blackjack.chip import Chip
import pytest

@pytest.fixture
def example_chip():
    return Chip()


def test_example_card_suit(example_chip):
    assert type(example_chip) == Chip


def test_example_card_value(example_chip):
    assert example_chip.value == 10
