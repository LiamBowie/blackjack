from deck import Deck
from agent import Dealer, Player

class Game():
    def __init__(self, deck:Deck, dealer:Dealer, players:list):
        self.deck = deck
        self.dealer = dealer
        self.players = players
    
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.hand.append(self.deck.draw())
            self.dealer.hand.append(self.deck.draw())
    
    def twist(self, player):
        player.add_card(self.deck.draw())
        print(player.hand)
        
    def __repr__(self):
        parts = []
        parts.append(f'Dealer\'s {self.dealer}')
        for i, player in enumerate(self.players):
            parts.append(f'Player {i+1}\'s {player}')
        return '\n'.join(parts)