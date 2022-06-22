class Dealer:

    def __init__(self):
        self.all_cards = []
        self.total = 0


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

    
    def under_21(self):
        total = 0
        for card in self.all_cards:
            total += card.value
        if total < 21:
            return True
        else:
            return False

    
    def hit(self, new_card):
        self.add_cards(new_card)


    def __str__(self):
        string = "Dealer has the following cards: /n"
        for card in self.all_cards:
            string = string + str(card)
        return string