from blackjack.player import Player
from blackjack.deck import Deck
from blackjack.card import Card
import pytest

@pytest.fixture
def example_player():
    return Player()


def test_example_player_empty_deck_initially(example_player):
    assert example_player.all_cards == []


def test_example_player_20_chips_initially(example_player):
    assert len(example_player.all_chips) == 20


def test_add_chips_increases_chip_no(example_player):
    example_player.add_chips(5)
    assert len(example_player.all_chips) == 25


def test_place_bet_remove_chips_with_enough_chips_succeeds(example_player):
    success = example_player.bet(5)
    assert success == True


def test_place_bet_remove_chips_with_enough_chips_decreases_chip_amount(example_player):
    success = example_player.bet(5)
    assert len(example_player.all_chips) == 15


def test_place_bet_remove_chips_with_not_enough_chips(example_player):
    example_player.all_chips = []
    success = example_player.bet(5)
    assert success == False


def test_place_bet_remove_chips_with_not_enough_chips_doesnt_decreases_chip_amount(example_player):
    example_player.all_chips = []
    success = example_player.bet(5)
    assert len(example_player.all_chips) == 0


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


@pytest.fixture
def example_cards():
    return [Card("Diamond","Two"), Card("Hearts","King")]


def test_calculate_total(example_player, example_cards):
    example_player.add_cards(example_cards)
    assert example_player.total == 12
    


def test_under_21(example_player, example_cards):
    example_player.add_cards(example_cards)
    assert example_player.under_21() == True
