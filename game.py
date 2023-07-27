from deck import Deck
from agent import Dealer, Player

class Game():
    __actions = ['twist', 'stand', 'double down']

    def __init__(self, dealer:Dealer, players:list):
        self.dealer = dealer
        self.players = players

    @property
    def actions(self):
        '''A list of actions that a player can take during their turn'''
        return self.__actions

    def deal_cards(self):
        self.deck = Deck()
        self.deck.shuffle()
        for i in range(2):
            for player in self.players:
                player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())
    
    def twist(self, player:Player):
        '''Adds a card to the players hand. Returns whether the new card busts them or not'''
        player.add_card(self.deck.draw())

        if player.get_hand_value() > 21:
            for hand in player.hands:
                for card in hand:
                    if card.value == 11:
                        card.value = 1
                        return player.bust
            player.bust = True
        return player.bust

    def handle_action(self, player:Player, action:str, first_turn_flag:bool):
        '''Resolves an agents action. Returns a Boolean that indicates whether their turn is still in progress'''
        if action == 'double down' and first_turn_flag:
            try:
                player.bet *= 2
            except ValueError:
                print('You do not have enough money to double down.')

            return False  

        elif action == 'double down' and not first_turn_flag:
            print('You can only double down as your first action.')
            return True

        if action == 'twist':
            return not self.twist(player)

        if action == 'stand':
            return False
        
    def resolve_hand(self, dealer:Dealer, player:Player):
        player_hand = player.get_hand_value()
        player_blackjack = True if player_hand == 21 and len(player.hand) == 2 else False
        dealer_hand = dealer.get_hand_value()
        dealer_blackjack = True if dealer_hand == 21 and len(dealer.hand) == 2 else False
        
        player.reset_hand()
        dealer.reset_hand()
        # Player wins with Blackjack
        if player_blackjack and not dealer_blackjack:
            print('Player wins with Blackjack!')
            player.bet *= 1.5
            player.money_left += round(player.bet)
            return player.money_left
        
        # Player busts. Dealer wins 
        if player.bust:
            print('Player busts. Dealer wins!')
            player.money_left -= player.bet
            player.bust = False
            return player.money_left
        
        # Dealer busts. Player wins
        if dealer.bust:
            print('Dealer busts. Player wins!')
            player.money_left += player.bet
            return player.money_left
        
        # Nobody wins. The bet is returned
        if player_hand == dealer_hand:
            print('It\'s a push! The bet is returned.')
            return player.money_left
        
        # Player wins
        if player_hand > dealer_hand:
            print('Player wins!')
            player.money_left += player.bet
            return player.money_left
        # Dealer wins
        else:
            print('Dealer wins!')
            player.money_left -= player.bet
            return player.money_left

    def __repr__(self):
        parts = []
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)

