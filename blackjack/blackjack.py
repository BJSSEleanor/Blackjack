from blackjack.deck import Deck
from blackjack.player import Player
from blackjack.dealer import Dealer

#player goes before dealer
#player aim to get closer to total value of 21 than the dealer
#hit (recieve another card) or stay (stop recieving cards)
class Blackjack:
    def __init__(self):
        self.play = True
        self.won = False
        self.reset_game()

    
    def reset_game(self):
        self.play = True
        self.won = False
        deck = Deck()
        deck.shuffle()
        player = Player()
        player.add_cards([deck.deal_one(),deck.deal_one()])
        dealer = Dealer()
        dealer.add_cards([deck.deal_one(),deck.deal_one()])


    def play_blackjack(self):
        while self.play:
            while not self.won:
                continue