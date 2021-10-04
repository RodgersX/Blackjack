class Card:

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
