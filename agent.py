from abc import ABC

class agent(ABC): 
    def __init__(self):
        self.__hands = [[]]
        self.__bust = False

    @property
    def bust(self):
        '''True if player's hand value is 2 or less. False if otherwise. '''
        return self.__bust
    
    @bust.setter
    def bust(self, bust):
        self.__bust = bust
    
    @property
    def hands(self):
        return self.__hands
    
    @hands.setter
    def hands(self, hands:list):
        self.__hands = hands
        
    def add_card(self, card, index=0):
        self.__hands[index].append(card)

    def reset_hand(self):
        self.__hands = [[]]

    def get_hand_value(self):
        hand_value = 0
        soft_ace = True
        for hand in self.__hands:
            for card in hand:
                hand_value += card.get_numerical_value(soft_ace)
                if card.value == 'A':
                    soft_ace = False
                if hand_value > 21 and not soft_ace:
                    hand_value -= 10

        return hand_value
    
    def show_hand(self):
        parts = []
        for hand in self.__hands:
            parts.extend(f'{card}' for card in hand)
            parts.append(f'Value: {self.get_hand_value()}')
        return ', '.join(parts)
    
    def split(self, hand_index):
        # Move the second card of the indexed hand to a new hand at the end of the list of hands
        self.__hands.append([self.__hands[hand_index][1]])
        # Remove the split card from the initial hand
        popped = self.__hands[hand_index].pop(1)

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
        return f'Dealer  : {self.hands[0][1]}'