from blackjack import __version__
from blackjack.blackjack import Blackjack
import pytest
import mock

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def example_game():
    return Blackjack()


#@pytest.mark.parametrize("game_feature,status", [
#    (example_game.play, True),
#    (example_game.winner, ""),
#    (example_game.player_bet, 0)])


#def test_blackjack_setup_correctly(example_game, game_feature, status):
#    assert game_feature == status


def test_blackjack_reset__works_correctly(example_game):
    example_game.play = False
    example_game.reset_game()
    assert example_game.play == True

def test_ask_play_again(example_game):
    with mock.patch.object(__builtins__, 'input', lambda: "n"):
        assert example_game.play == False