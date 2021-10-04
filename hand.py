import deck


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # get card from deck class deal function
        self.cards.append(card)
        self.value += deck.values[card.rank]

        # track the aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value < 21 and self.aces:
            self.value -= 10
            self.aces -= 1


