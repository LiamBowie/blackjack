from abc import ABC

class agent(ABC): 
    def __init__(self):
        self.__hand = []
        self.__bust = False

    @property
    def bust(self):
        '''True if player's hand value is 2 or less. False if otherwise. '''
        return self.__bust
    
    @bust.setter
    def bust(self, bust):
        self.__bust = bust
    
    @property
    def hand(self):
        return self.__hand
    
    @hand.setter
    def hand(self, hand:list):
        self.__hand = hand
        
    def add_card(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.__hand = []

    def get_hand_value(self):
        hand_value = 0
        soft_ace = True
        for card in self.hand:
            hand_value += card.get_numerical_value(soft_ace)
            if card.value == 'A':
                soft_ace = False
            if hand_value > 21 and not soft_ace:
                hand_value -= 10

        return hand_value
    
    def show_hand(self):
        parts = [f'{card}' for card in self.__hand]
        parts.append(f'Value: {self.get_hand_value()}')
        return ', '.join(parts)

class Player(agent):
    __id = 1

    def __init__(self, amount):
        super().__init__()
        self.__money_left = amount
        self.__bet = 0
        self.__id = Player.__id
        Player.__id += 1

    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Bet: {self.bet}, ')
        parts.append(f'Money left: {self.money_left}')
        return ' '.join(parts)
    
    @property
    def id(self):
        '''Unique id of each player'''
        return f'{self.__id}'
    
    # @id.setter
    # def id(self):
    #     self.id  = Player.id
    
    @property
    def bet(self):
        '''The amount of money a player is betting on a hand'''
        return self.__bet
    
    @bet.setter
    def bet(self, bet):
        if bet <= self.money_left and bet >= 0:
            self.__bet = bet
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
    
    def show_upcard(self):
        return f'Dealer  : {self.hand[1]}'
