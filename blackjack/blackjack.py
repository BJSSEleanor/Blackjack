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
        self.winner = ""
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.player_bet = 0
        self.dealer = Dealer()
        print("---BlackJack---")

    
    def reset_game(self):
        self.play = True
        self.won = False
        self.winner = ""
        self.deck = Deck()
        self.deck.shuffle()
        self.player.all_cards = []
        self.player_bet = 0
        self.dealer.all_cards = []

    
    def get_player_input(self):
        valid_player_input = False
        while not valid_player_input:
            try:
                player_choice = str(input("Hit or Stay? [h or s]"))   
            except:
                print("Not a valid input, please provide h to hit or s to stay")
            else:
                if player_choice == "h" or player_choice == "s":
                    valid_player_input = True
                    return player_choice
                else:
                    print("Not a valid input, please provide h to hit or s to stay")


    def get_player_bet(self):
        valid_player_bet = False
        while not valid_player_bet:
            try:
                player_bet = int(input("How many chips will you bet? ")) 
            except:
                print("Not a valid input, please provide a number between 1 and 20")
            else:
                if player_bet <= 0 or player_bet >20:
                    print("Not a valid input, please provide a number between 1 and 20")
                else:
                    valid_player_bet = self.player.bet(player_bet)
                    self.player_bet = player_bet
        print("Your bet has been successful!\nA bet of {} has been placed".format(player_bet*10))


    def ask_play_again(self):
        play_again = str(input("Would you like to play again? [y/n]"))
        if play_again.lower() == "n" or play_again.lower() == "no":
            self.play = False
        else:
            self.reset_game


    def play_blackjack(self):
        while self.play:
            while not self.won:
                self.get_player_bet()
                self.dealer.add_cards([self.deck.deal_one(),self.deck.deal_one()])
                print("The Dealer's first card is: /n{}".format(self.dealer.all_cards[0]))
                self.player.add_cards([self.deck.deal_one(),self.deck.deal_one()])
                print(self.player)
                #player turn
                player_choice = self.get_player_input()
                if player_choice == "h":
                    self.player.hit(self.deck.deal_one())
                elif player_choice == "s":
                    self.player.stay()
                #dealer's turn
                player_under_21 = self.player.under_21()
                
                if player_under_21:
                    self.dealer.add_cards(self.deck.deal_one())
                    dealer_under_21 = self.dealer.under_21()
                    while dealer_under_21 and self.dealer.total < self.player.total:
                        self.dealer.hit(self.deck.deal_one())
                    if self.dealer.total > self.player.total and dealer_under_21:
                        self.winner = "Dealer"
                        print("The Dealer has won!")
                        self.won = True
                    else:
                        self.winner = "Player"
                        print("You have won!")
                        self.won = True
                else:
                    self.winner = "Dealer"
                    print("The Dealer has won!")
                    self.won = True
            if self.winner == "Player":
                print("You have won your bet of {} back!".format(self.player_bet))
                self.player.add_chips(self.player_bet)
            self.ask_play_again()



