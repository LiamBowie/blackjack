from deck import Deck
from agent import Dealer, Player
from game import Game

# Functions 
def sanitize(input):
    return input.strip().lower()

# Game set up
deck = Deck()
player1 = Player(100)
player2 = Player(250)
dealer = Dealer()
game = Game(deck, dealer, [player1])

# First hand starts
deck.shuffle()

# Placing bets 
for i, player in enumerate(game.players):
    placing_bet = True
    wager = 0
    while placing_bet: 
        try:
            wager = int(sanitize(input(f'Player {i+1}. You have {player.money_left}. How much would you like to wager?: ')))
            player.wager = wager
        except ValueError:
            print('You must enter a number.')
            continue

        if wager == -1:
            print('Please bet an acceptable amount.')
            continue

        placing_bet = False

# Hands are dealt
game.deal_cards()
for i, player in enumerate(game.players):
    print(f'Player {i+1}: {player.hand}')

print(dealer.show_one_card())

# Player's take their turns 
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
            try:
                player.wager *= 2
            except ValueError:
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

# Dealer's turn
print(f'{dealer.show_hand()} Value: {dealer.get_hand_value()}')

while dealer.get_hand_value() < dealer.limit:
    game.twist(dealer)
    print(f'{dealer.show_hand()} Value: {dealer.get_hand_value()}')


# Resolve the round 
if dealer.get_hand_value() > 21:
    print('Dealer bust')
    
    for player in game.players:
        if not player.bust:
            player.money_left += player.wager

for player in game.players:
    if player.bust:
        player.money_left -= player.wager
        continue

    if dealer.get_hand_value() < player.get_hand_value():
        print('player wins')
        player.money_left += player.wager
    else:
        print('dealer wins')
        player.money_left -= player.wager


for player in game.players:
    player.wager = 0

print(game)