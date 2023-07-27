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
            player.increase_bet(hand_index, player.bet[hand_index])
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
        
        # Player wins with Blackjack
        if player_blackjack and not dealer_blackjack:
            player.bet[index] *= 1.5
            player.chips += round(player.bet[index])

            print(f'Player {player.id} wins with Blackjack!')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips} (+{player.bet[index]})')
        
        # Player busts. Dealer wins 
        if player.bust:
            player.chips -= player.bet[index]
            player.bust = False

            print(f'Player {player.id} busts. Dealer wins!')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips} (-{player.bet[index]})')
        
        # Dealer busts. Player wins
        if dealer.bust:
            player.chips += player.bet[index]

            print(f'Dealer busts. Player {player.id} wins!')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips} (+{player.bet[index]})')
        
        # Nobody wins. The bet is returned
        if player_hand == dealer_hand:
            print(f'It\'s a push! Player {player.id}\'s bet is returned.')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips}')
        
        # Player wins
        if player_hand > dealer_hand:
            player.chips += player.bet[index]
            
            print(f'Player {player.id} wins!')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips} (+{player.bet[index]})')

        # Dealer wins
        else:
            player.chips -= player.bet[index]
            
            print(f'Dealer wins! Player {player.id} loses')
            print(player.show_hand(index))
            print(f'Chips left: {player.chips} (-{player.bet[index]})')

    def __repr__(self):
        parts = []
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)
