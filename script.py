from agent import Dealer, Player
from game import Game

# Constants
MAX_SEATS = 5

# Functions 
def sanitize(input):
    return input.strip().lower()

# Game set up
players = []
people_at_the_table = True
choosing_players = True
while choosing_players:
    try:
        no_of_players = int(sanitize(input('How many players are at the table?: ')))
    except ValueError:
        print('You must input a number.')
        continue

    if no_of_players > MAX_SEATS:
        print('There are only 5 seats at the table.')
        continue 

    if no_of_players < 1:
        print('there is no one at the table, farewell gambler.')
        no_of_players = 0
        people_at_the_table = False

    choosing_players = False

for i in range(no_of_players):
    players.append(Player(100))

dealer = Dealer()
game = Game(dealer, players)

while people_at_the_table:
    # Placing bets 
    for player in game.players:
        placing_bet = True
        while placing_bet: 
            try:
                bet = int(sanitize(input(f'Player {player.id}. You have {player.money_left}. How much would you like to bet?: ')))
                player.bet = bet
            except ValueError:
                print('You must enter an number that is less than the money you have left and more than 0.')
                continue

            placing_bet = False

    # Hands are dealt
    game.deal_cards()
    for player in game.players:
        print(f'Player {player.id}: {player.show_hand()}')

    print(dealer.show_upcard())

    # Player's take their turns 
    for current_player in game.players:
        first_turn = True
        playing = True
        while playing:
            print(f'Player {current_player.id}: {current_player.show_hand()}')
            if current_player.get_hand_value() == 21:
                break

            action = sanitize(input(f'Player {current_player.id}. Would you like to Twist, Stand, or Double Down?: '))

            if action not in game.actions:
                print('Please enter "twist" "stand", or "double down".')
                continue

            playing = game.handle_action(current_player, action, first_turn)

            first_turn = False
        print(f'Player {current_player.id} (final): {current_player.show_hand()}')
    # Dealer's turn
    print(f'Dealer. {dealer.show_hand()}')

    while dealer.get_hand_value() < dealer.limit:
        game.twist(dealer)
        print(f'Dealer. {dealer.show_hand()}')

    # Resolve the round 
    for current_player in game.players:
        current_player_balance = game.resolve_hand(dealer, current_player)
        print(f'Player {current_player.id} money left: {current_player_balance}')
    
    for player in game.players:
        if player.money_left == 0:
            print(f'Player {player.id} leaves the table.')
            game.players.remove(player)
        player.bet = 0
    
    if len(game.players) == 0:
        people_at_the_table == False
        break

    exit_phrase = 'exit'
    leaving = sanitize(input(f'Type "{exit_phrase}" to leave the table: '))
    if leaving == exit_phrase:
        people_at_the_table = False
        break

    # Reset dealer's bust flag
    dealer.bust = False
