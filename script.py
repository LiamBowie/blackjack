class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} {self.suit}'

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for suit in suits:
    for value in values:
        print(f'{Card(value, suit)}')
