from deck import Deck
from agent import Dealer, Player

class Game():

    def __init__(self, dealer:Dealer, players:list):
        self.dealer = dealer
        self.players = players
        self.deck = Deck()

    def deal_cards(self):
        self.deck = Deck()
        self.deck.shuffle()
        for _ in range(2):
            for player in self.players:
                player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())
    
    def twist(self, player:Player, hand_index:int = 0):
        '''Adds a card to the players hand. Returns whether the new card busts them or not'''
        player.add_card(self.deck.draw(), hand_index)

        if player.get_hand_value() > 21:
            for hand in player.hands:
                for card in hand:
                    if card.value == 11:
                        card.value = 1
                        return player.bust
            player.bust = True
        return player.bust

    def handle_action(self, player:Player, hand_index, action:str):
        '''Resolves an agents action. Returns a Boolean that indicates whether their turn is still in progress'''
        if action == 'split':
            player.split(hand_index)

            player.add_card(self.deck.draw(), -1)
            player.add_card(self.deck.draw(), hand_index)

            return True

        if action == 'double down':
            player.bet *= 2
            self.twist(player, hand_index)
            return False 

        if action == 'twist':
            return not self.twist(player, hand_index)

        if action == 'stand':
            return False
        
    def resolve_hand(self, dealer:Dealer, player:Player, index):
        player_hand = player.get_hand_value(index)
        player_blackjack = True if player_hand == 21 and len(player.hands[index]) == 2 else False
        dealer_hand = dealer.get_hand_value()
        dealer_blackjack = True if dealer_hand == 21 and len(dealer.hands[index]) == 2 else False
        
        player.reset_hand()
        dealer.reset_hand()
        # Player wins with Blackjack
        if player_blackjack and not dealer_blackjack:
            print('Player wins with Blackjack!')
            player.bet *= 1.5
            player.chips += round(player.bet)
            return player.chips
        
        # Player busts. Dealer wins 
        if player.bust:
            print('Player busts. Dealer wins!')
            player.chips -= player.bet
            player.bust = False
            return player.chips
        
        # Dealer busts. Player wins
        if dealer.bust:
            print('Dealer busts. Player wins!')
            player.chips += player.bet
            return player.chips
        
        # Nobody wins. The bet is returned
        if player_hand == dealer_hand:
            print('It\'s a push! The bet is returned.')
            return player.chips
        
        # Player wins
        if player_hand > dealer_hand:
            print('Player wins!')
            player.chips += player.bet
            return player.chips
        # Dealer wins
        else:
            print('Dealer wins!')
            player.chips -= player.bet
            return player.chips

    def __repr__(self):
        parts = []
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)
