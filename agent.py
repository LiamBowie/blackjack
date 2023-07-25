class Player:

    def __init__(self, amount):
        self.money_left = amount
        self.hand = []
        self.wager = 0
        self.bust = False

    def __repr__(self):
        parts = [f'Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Wager: {self.wager}, ')
        parts.append(f'Money left: {self.money_left}')
        return ' '.join(parts)

    def show_hand(self):
        parts = [f'{card}' for card in self.hand]
        return ', '.join(parts)
    
    def add_card(self, card):
        self.hand.append(card)
    
    def place_bet(self, wagered):
        if wagered < self.money_left and wagered > 0:
            self.wager = wagered
            self.money_left -= self.wager 
            return self.wager
        else:
            return -1
    
    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.get_numerical_value()

        return hand_value
    
class Dealer:
    hand = []
    limit = 17

    def __repr__(self):
        parts = ['Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Dealer limit: {self.limit}')
        return ' '.join(parts)
    
    def show_hand(self):
        return f'Dealer\'s hand: ?? {self.hand[1]}'

    def add_card(self, card):
        self.hand.append(card)
    
    def reveal_hand(self):
        parts = [f'Dealer\'s hand:']
        parts.extend(f'{card}' for card in self.hand)
        return ' '.join(parts)

    def get_hand_value(self):
        hand_value = 0
        for card in self.hand:
            hand_value += card.get_numerical_value()

        return hand_value
