from blackjack.dealer import Dealer
from blackjack.deck import Deck
from blackjack.card import Card
import pytest

@pytest.fixture
def example_dealer():
    return Dealer()


def test_example_dealer_empty_deck_initially(example_dealer):
    assert example_dealer.all_cards == []


@pytest.fixture
def example_deck():
    return Deck()
    

def test_player_given_one_card(example_dealer,example_deck):
    example_deck.shuffle()
    new_card = example_deck.deal_one()
    example_dealer.add_cards(new_card)
    assert example_dealer.all_cards == [new_card]


def test_player_given_multiple_cards(example_dealer,example_deck):
    example_deck.shuffle()
    new_cards = []
    for num in range(0,3):
        card = example_deck.deal_one()
        new_cards.append(card)
    example_dealer.add_cards(new_cards)
    assert example_dealer.all_cards == new_cards


@pytest.fixture
def example_cards():
    return [Card("Diamond","Two"), Card("Hearts","King")]


def test_calculate_total(example_dealer, example_cards):
    example_dealer.add_cards(example_cards)
    assert example_dealer.total == 12
    


def test_under_21(example_dealer, example_cards):
    example_dealer.add_cards(example_cards)
    assert example_dealer.under_21() == True
