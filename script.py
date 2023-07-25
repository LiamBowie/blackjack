from deck import Deck
from agent import Dealer, Player
from game import Game
import os

# Functions 
def sanitize(input):
    return input.strip().lower()

# Game set up
deck = Deck()
player1 = Player(100)
player2 = Player(250)
dealer = Dealer()
game = Game(deck, dealer, [player1, player2])

# First hand starts
deck.shuffle()

# Placing bets 
for i, player in enumerate(game.players):
    placing_bet = True
    while placing_bet: 
        try:
            wager = int(sanitize(input(f'Player {i+1}. You have {player.money_left}. How much would you like to wager?: ')))
            player.wager = wager
        except ValueError:
            print('You must enter an number that is less than the money you have left and more than 0.')
            continue

        placing_bet = False

# Hands are dealt
game.deal_cards()
for i, player in enumerate(game.players):
    print(f'Player {i+1}: {player.show_hand()}')

print(dealer.show_one_card())

# Player's take their turns 
for i, current_player in enumerate(game.players):
    
    first_turn = True
    playing = True
    while playing:
        print(f'Player {i+1}: {current_player.show_hand()}')
        if current_player.get_hand_value() == 21:
            print('Blackjack!')
            break

        action = sanitize(input(f'Player {i+1}. Would you like to Twist, Stand, or Double Down?: '))

        if action not in game.actions:
            print('Please enter "twist" "stand", or "double down".')
            continue

        playing = game.handle_action(current_player, action, first_turn)

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