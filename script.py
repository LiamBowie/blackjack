from agent import Dealer, Player
from game import Game
import os

# Constants
MAX_SEATS = 5

# Functions 
def sanitize(input):
    return input.strip().lower()

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')  # Use the 'cls' command to clear the screen on Windows
    else:
        os.system('clear')  # Use the 'clear' command to clear the screen on Unix-based systems

# Game set up
clear_screen()
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
                initial_bet = int(sanitize(input(f'Player {player.id}. You have {player.chips} chips left. How much would you like to bet?: ')))
            except ValueError:
                print('You must enter an number.')
                continue

            if initial_bet <= player.chips and initial_bet > 0:
                player.add_initial_bet(initial_bet)
            else:
                print('You must bet less than your total number of chips and more than 0 chips.')
                continue 

            placing_bet = False

    # Hands are dealt
    game.deal_cards()
    # Player's take their turns 
    for current_player in game.players:
        from deck import Card
        current_player.hands = [[Card('8', 'Hearts'), Card('8', 'Diamonds')]]
        for i, hand in enumerate(current_player.hands):
            clear_screen()
            print('================================================')
            for player in game.players:
                print(f'Player {player.id}: {player.show_hands()}')

            print(dealer.show_upcard())
            print('================================================')
            first_turn = True
            playing = True
            while playing:
                print(f'Player {current_player.id} ({current_player.bet[i]}): {current_player.show_hand(i)}')

                if current_player.get_hand_value(i) == 21:
                    print('Blackjack!') if first_turn else print('You\'ve hit 21!')
                    break

                print(f'Player {current_player.id}. What would you like to do?')
                for action in current_player.list_available_actions(i, first_turn):
                    print(f'-{action}')

                action = sanitize(input('Enter your action: '))

                if action not in current_player.actions:
                    print('Please enter an action from the list.')
                    current_player.reset_actions()
                    continue

                playing = game.handle_action(current_player, i, action)

                current_player.reset_actions()
                
                first_turn = True if action == 'split' else False
            
        print('================================================')
        print(f'Player {current_player.id} (final): {current_player.show_hands()}')
        print('Press enter to continue')
        print('================================================')
        input()
        
    print('================================================')
    # Dealer's turn
    print(f'Dealer. {dealer.show_hand()}')
    while dealer.get_hand_value() < dealer.limit:
        game.twist(dealer)
        print(f'Dealer. {dealer.show_hand()}')
    print('================================================')
    # Resolve the round 
    for current_player in game.players:
        for i, _ in enumerate(current_player.hands):
            game.resolve_hand(dealer, current_player, i-1)
        print()
    print('================================================')

    for player in game.players:
        if player.chips == 0:
            print(f'Player {player.id} leaves the table.')
            game.players.remove(player)
        player.reset_hand()
        player.bet = 0

    dealer.reset_hand()
    
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
    clear_screen()
