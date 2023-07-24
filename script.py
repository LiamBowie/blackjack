import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} {self.suit}'
    
    def get_numerical_value(self):
        if self.value == 'A':
            return 11
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
        parts.append(f'Money left: {self.amount}')
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

    def show_hand(self):
        return f'Dealer\'s hand: ?? {self.hand[1]}'
    
    def reveal_hand(self):
        parts = [f'Dealer\'s hand:']
        parts.extend(f'{card}' for card in self.hand)
        return ' '.join(parts)

    def __repr__(self):
        parts = ['Hand:']
        parts.extend(f'{card}' for card in self.hand)
        parts.append(f'Dealer limit: {self.limit}')
        return ' '.join(parts)
    
class Game():
    def __init__(self, deck:Deck, dealer:Dealer, players:list):
        self.deck = deck
        self.dealer = dealer
        self.players = players
    
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.hand.append(self.deck.draw())
            dealer.hand.append(self.deck.draw())
    
    def twist(self, player):
        player.add_card(self.deck.draw())
        print(player.hand)
        
    def __repr__(self):
        parts = [f'{self.deck}']
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)

def sanitize(input):
    return input.strip().lower()

deck = Deck()
player1 = Player(100)
player2 = Player(250)
dealer = Dealer()
game = Game(deck, dealer, [player1])

# First hand starts
deck.shuffle()

for i, player in enumerate(game.players):
    placing_bet = True
    wager = 0
    while placing_bet: 
        try:
            wager = int(sanitize(input(f'Player {i+1}. You have {player.money_left}. How much would you like to wager?: ')))
            player.wager = wager
            wager = player.place_bet(player.wager)
        except ValueError:
            print('You must enter a number.')
            continue

        if wager == -1:
            print('Please bet an acceptable amount.')
            continue

        placing_bet = False

game.deal_cards()
for i, player in enumerate(game.players):
    print(f'Player {i+1}: {player.hand}')

print(dealer.show_hand())

for i, player in enumerate(game.players):
    
    print(f'Player {i+1}: {player.show_hand()} {player.get_hand_value()}')
    available_actions = ['twist', 'stand', 'double down']

    first_turn = True
    while player.get_hand_value() <= 21:

        if player.get_hand_value() == 21:
            print('Blackjack!')
            break

        action = sanitize(input(f'Player {i+1}. Would you like to Twist, Stand, or Double Down?: '))

        if action not in available_actions:
            print('Please enter "twist" "stand", or "double down".')
            continue

        if action == 'double down' and first_turn:
            approved = player.place_bet(player.wager)

            if approved == -1:
                print('You do not have enough money to double down.')
                continue

            game.twist(player)
            if player.get_hand_value() > 21:
                print('You\'re bust')
                player.bust = True
            break

        elif action == 'double down' and not first_turn:
            print('You can only double down on your first action.')

        if action == 'twist':
            game.twist(player)
            if player.get_hand_value() > 21:
                print('You\'re bust')
                player.bust = True
                break

        if action == 'stand':
            break

        first_turn = False
    
