from deck import Deck
from agent import Dealer, Player
from game import Game
from time import sleep

# Functions 
def sanitize(input):
    return input.strip().lower()

# Game set up
player1 = Player(100)
player2 = Player(250)
dealer = Dealer()
game = Game(dealer, [player1, player2])

people_at_the_table = True
while people_at_the_table:
    # Placing bets 
    for i, player in enumerate(game.players):
        placing_bet = True
        while placing_bet: 
            try:
                bet = int(sanitize(input(f'Player {i+1}. You have {player.money_left}. How much would you like to bet?: ')))
                player.bet = bet
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
        print(f'Dealer. {dealer.show_hand()}')
        sleep(1)

    # Resolve the round 
    for i, current_player in enumerate(game.players):
        current_player_balance = game.resolve_hand(dealer, current_player)
        if current_player_balance == 0:
            print('You\'re out of money!')
            game.players.remove(current_player)
        current_player.bet = 0
        print(f'Player {i+1} money left: {current_player_balance}')
    
    exit_phrase = 'exit'
    leaving = sanitize(input(f'Player {i+1}: Type "{exit_phrase}" to leave the table: '))

    if leaving == exit_phrase:
        people_at_the_table == False
