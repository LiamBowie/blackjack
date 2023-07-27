from abc import ABC

class agent(ABC): 
    def __init__(self):
        self.__hands = [[]]
        self.__bust = False
        self.actions = ['twist', 'stand']

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

    def get_hand_value(self, index:int = 0):
        hand_value = 0
        soft_ace = True
        for card in self.__hands[index]:
            hand_value += card.get_numerical_value(soft_ace)
            if card.value == 'A':
                soft_ace = False
        if hand_value > 21 and not soft_ace:
            hand_value -= 10

        return hand_value
    
    def show_hand(self, index:int = 0):
        parts = []
        parts.extend(f'{card}' for card in self.__hands[index])
        parts.append(f'Value: {self.get_hand_value(index)}')
        return ', '.join(parts)

    def show_hands(self):
        parts = []
        for i, hand in enumerate(self.__hands):
            parts.extend(f'{card}' for card in hand)
            parts.append(f'Value: {self.get_hand_value(i)}')
        return ', '.join(parts)
    
    def split(self, hand_index):
        # Move the second card of the indexed hand to a new hand at the end of the list of hands
        self.__hands.append([self.__hands[hand_index][1]])
        # Remove the split card from the initial hand
        self.__hands[hand_index].pop(1)

class Player(agent):
    __id = 1

    def __init__(self, amount):
        super().__init__()
        self.chips = amount
        self.bet = [0]
        self.actions = ['twist', 'stand']
        self.__id = Player.__id
        Player.__id += 1

    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Bet: {self.bet}, ')
        parts.append(f'Chips left: {self.chips}')
        return ' '.join(parts)
    
    @property
    def id(self):
        '''Unique id of each player'''
        return f'{self.__id}'
    
    def increase_bet(self, index, raised):
        if self.bet[index] <= self.chips and self.bet[index] >= 0:
            self.bet[index] += raised
          
    def list_available_actions(self, hand_index:int = 0, first_turn:bool = False):
        if first_turn:
            if sum(self.bet) + self.bet[hand_index] <= self.chips:
                self.actions.append('double down')
            
                if self.hands[hand_index][0].value == self.hands[hand_index][1].value:
                    self.actions.append('split')
        
        return self.actions
    
    def reset_actions(self):
        self.actions = ['twist', 'stand']

    def split(self, hand_index):
        # Run method from abstract parent class
        super().split(hand_index)
        # add a new bet associated with the new hand
        self.bet.append(self.bet[hand_index])

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
    