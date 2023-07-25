from abc import ABC, abstractmethod

class agent(ABC): 
    def __init__(self):
        self.hand = []
        self.bust = False

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.get_numerical_value()

        return hand_value
    
    def show_hand(self):
        parts = [f'{card}' for card in self.hand]
        return ', '.join(parts)

class Player(agent):

    def __init__(self, amount):
        super().__init__()
        self.money_left = amount
        self.wager = 0

    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Wager: {self.wager}, ')
        parts.append(f'Money left: {self.money_left}')
        return ' '.join(parts)
    
    
    def place_bet(self, wagered):
        if wagered < self.money_left and wagered > 0:
            self.wager = wagered
            self.money_left -= self.wager 
            return self.wager
        else:
            return -1

class Dealer(agent):
    def __init__(self, limit=17):
        super().__init__()
        self.limit = limit

    def __repr__(self):
        parts = ['Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Dealer limit: {self.limit}')
        return ' '.join(parts)
    
    def show_one_card(self):
        return f'Dealer\'s hand: ?? {self.hand[1]}'


