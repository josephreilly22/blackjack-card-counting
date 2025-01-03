import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # def __repr__(self):
    #     return f'{self.value}'


class Shoe:
    def __init__(self, numOfDecks):
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        self.cards = []
        for i in range(numOfDecks):
            for value in range(1, 14):
                for suit in suits:
                    if value > 10:
                        self.cards.append(10)
                    else:
                        self.cards.append(value)
        self.shuffle()

    def get_cards(self):
        return self.cards
    
    def shuffle(self):
        random.shuffle(self.cards)

