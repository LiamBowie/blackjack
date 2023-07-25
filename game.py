from deck import Deck
from agent import Dealer, Player

class Game():
    __actions = ['twist', 'stand', 'double down']

    def __init__(self, deck:Deck, dealer:Dealer, players:list):
        self.deck = deck
        self.dealer = dealer
        self.players = players

    @property
    def actions(self):
        '''A list of actions that a player can take during their turn'''
        return self.__actions

    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.hand.append(self.deck.draw())
            self.dealer.hand.append(self.deck.draw())
    
    def twist(self, player:Player):
        '''Adds a card to the players hand. Returns whether the new card busts them or not'''
        player.add_card(self.deck.draw())
        if player.get_hand_value() > 21:
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
        # Player wins with Blackjack
        if player.get_hand_value() == 21 and not dealer.get_hand_value() == 21:
            player.bet *= 1.5
            player.money_left += player.bet
            return player.money_left
        
        # Player busts. Dealer wins 
        if player.bust:
            player.money_left -= player.bet
            return player.money_left
        
        # Dealer busts. Player wins
        if dealer.bust:
            player.money_left += player.bet
            return player.money_left
        
        # Nobody wins. The bet is returned
        if player.get_hand_value() == dealer.get_hand_value():
            return player.money_left
        
        # Player wins
        if player.get_hand_value() > dealer.get_hand_value():
            player.money_left += player.bet
            return player.money_left
        # Dealer wins
        else:
            player.money_left -= player.bet
            return player.money_left

    def __repr__(self):
        parts = []
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)