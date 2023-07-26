import random

class Card:
    def __init__(self, value, suit):
        self.__value = value
        self.suit = suit

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __repr__(self):
        return f'{self.value} {self.suit}'
    
    def get_numerical_value(self, soft_ace):
        if self.value == 'A' and soft_ace:
            return 11
        elif self.value == 'A' and not soft_ace:
            return 1
        elif self.value == 'K' or self.value == 'Q' or self.value == 'J':
            return 10
        else:
            return int(self.value)
    
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
