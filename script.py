import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{self.suit[0]}'
    
class Deck:
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    values = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    def __init__(self):
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values]
    
    def __repr__(self):
        output = []
        for card in self.cards:
            output.append(f'{card}')

        return ', '.join(output)    
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)

deck = Deck()

print(deck)
deck.shuffle()
print(deck)
for i in range(5):
    print(deck.draw())