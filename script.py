class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} {self.suit}'
    
class Deck:
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values]
    
    def __repr__(self):
        output = []
        for card in self.cards:
            output.append(f'{card}')

        return ', '.join(output)    

deck = Deck()
print(deck)