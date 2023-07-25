from abc import ABC

class agent(ABC): 
    def __init__(self):
        self.hand = []
        self.__bust = False

    @property
    def bust(self):
        '''True if player's hand value is 2 or less. False if otherwise. '''
        return self.__bust
    
    @bust.setter
    def bust(self, bust):
        self.__bust = bust

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.get_numerical_value()

        return hand_value
    
    def show_hand(self):
        parts = [f'{card}' for card in self.hand]
        parts.append(f'Value: {self.get_hand_value()}')
        return ', '.join(parts)
    
    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        return ' '.join(parts)

class Player(agent):

    def __init__(self, amount):
        super().__init__()
        self.__money_left = amount
        self.__wager = 0

    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Wager: {self.wager}, ')
        parts.append(f'Money left: {self.money_left}')
        return ' '.join(parts)

    @property
    def wager(self):
        '''The amount of money a player is betting on a hand'''
        return self.__wager
    
    @wager.setter
    def wager(self, wager):
        if wager <= self.money_left and wager >= 0:
            self.__wager = wager
        else:
            raise ValueError
    
    @property
    def money_left(self):
        '''The amount of money a player has left to bet'''
        return self.__money_left
    
    @money_left.setter
    def money_left(self, value):
        self.__money_left = value

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


