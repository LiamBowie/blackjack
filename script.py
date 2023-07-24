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
    
class Player:
    hand = []
    wager = 0

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        parts = [f'Player\'s hand: '] + self.hand
        parts.append(f'Wager: {self.wager}, ')
        parts.append(f'Money left: {self.amount}')
        return ' '.join(parts)

class Dealer:
    hand = []
    limit = 17

    def __repr__(self):
        parts = ['Dealer\'s hand:'] + self.hand
        parts.append(f'Dealer limit: {self.limit}')
        return ' '.join(parts)

deck = Deck()
player = Player(100)

dealer = Dealer()
print(dealer)
print(player)