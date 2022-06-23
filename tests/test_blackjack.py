from blackjack import __version__
from blackjack.blackjack import Blackjack
import pytest

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def example_game():
    return Blackjack()


#@pytest.mark.parametrize("game_feature,status", [
#    (win, False),
#    (play, True),
#    (winner, ""),
#    (player_bet, 0)])


#def test_blackjack_setup_correctly(example_game, game_feature, status):
#    assert example_game.game_feature == status


def test_blackjack_setup_correctly(example_game):
    example_game.play = False
    example_game.reset_game()
    assert example_game.play == True