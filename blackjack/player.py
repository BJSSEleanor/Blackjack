from blackjack.chip import Chip

class Player:

    def __init__(self):
        self.all_cards = []
        self.stay = False
        self.total = 0
        self.all_chips = []
        for i in range(20):
            self.all_chips.append(Chip())


    def add_chips(self, no_chips):
        for i in range(no_chips):
            self.all_chips.append(Chip())


    def bet(self, no_chips):
        if no_chips > len(self.all_chips):
            return False
        else:
            for num in range(0, no_chips):
                self.all_chips.pop()
            return True


    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        self.calculate_total()


    def calculate_total(self):
        total = 0
        for card in self.all_cards:
            total += card.value
        self.total = total


    def hit(self, new_card):
        self.add_cards(new_card)


    def stay(self):
        self.stay = True


    def under_21(self):
        total = 0
        for card in self.all_cards:
            total += card.value
        if total < 21:
            return True
        else:
            return False


    def __str__(self):
        string = "You have the following cards: /n"
        for card in self.all_cards:
            string = string + str(card)
        return string