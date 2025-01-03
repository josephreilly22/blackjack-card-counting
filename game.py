from cards import Shoe
from player import Player 

class Game:
    def __init__(self, numOfDecks, deckPenetration, H17, DAS, payout):
        self.numOfDecks = numOfDecks
        self.deckPenetration = deckPenetration * (52*numOfDecks)
        self.H17 = H17
        self.DAS = DAS
        self.handsComplete = 0
        self.deck = Shoe(numOfDecks).get_cards()
        self.player = Player(15)
        self.count = 0
        self.dealer = []
        self.current_index = 0
        self.payout = payout
        
    def deal_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card
    
    def deal_player_start(self):
        card1 = self.deal_card()
        card2 = self.deal_card()
        self.count_card(card1)
        self.count_card(card2)
        self.player.cards = [[card1, card2]]

    def hit(self, index=None):
        card = self.deal_card()
        self.count_card(card)
        if index:
            self.player.cards[index].append(card)
        else:
            self.player.cards[self.current_index].append(card)

    def split(self):
        self.player.cards.append([self.player.cards[self.current_index][1]])
        self.player.cards[self.current_index].pop(1)
        self.hit()
        self.hit(len(self.player.cards)-1)

    def double(self):
        pass

    def deal_dealer_start(self):
        card1 = self.deal_card()
        card2 = self.deal_card()
        self.count_card(card1)
        self.dealer = [card1, card2]

    def check_player(self, index=None):
        total = 0
        ace_count = 0
        if index != None:
            for card in self.player.cards[index]:
                total += card
                if card == 1:
                    ace_count += 1
        else:
            for card in self.player.cards[self.current_index]:
                total += card
                if card == 1:
                    ace_count += 1
        if total < 12 and ace_count:
            total += 10
        return total
    
    def check_soft(self):
        total = self.check_player()
        new_total = 0
        for card in self.player.cards[self.current_index]:
            new_total += card
        if new_total != total:
            return True
        return False

    def dealer_deal_out(self):
        # Check if deal out needed
        deal_out = False
        for hand in range(len(self.player.cards)):
            total = self.check_player(hand)
            if total <= 21:
                deal_out = True

        self.count_card(self.dealer[1])

        if deal_out:
            total = 0
            ace_count = 0
            while total < 17:
                total = 0
                ace_count = 0
                for card in self.dealer:
                    total += card
                    if card == 1:
                        ace_count += 1
                if total < 12 and ace_count:
                    total += 10

                # Append card if needed
                if total < 17:
                    self.dealer.append(self.deal_card())

                # Check for hit or stand on soft 17
                # elif total == 17 and self.H17 and ace_count:
                #     new_total = 0
                #     for card in self.dealer:
                #         new_total += card
                #     if new_total != total:
                #         total = 0
                # Break if over 17
                else:
                    break

            for card in range(len(self.dealer)):
                if card > 1:
                    self.count_card(self.dealer[card])

            if total > 21:
                return 0
            else:
                return total
        
    def check_blackjack(self):
        # Player Blackjack
        if self.player.cards[0][0] == 1:
            if self.player.cards[0][1] == 10:
                return 'P'
        if self.player.cards[0][0] == 10:
            if self.player.cards[0][1] == 1:
                return 'P'

        # Dealer Blackjack
        if self.dealer[0] == 1:
            if self.dealer[1] == 10:
                return 'D'
        if self.dealer[0] == 10:
            if self.dealer[1] == 1:
                return 'D'
        
        return False

    def end_hand(self):
        self.current_index = 0

    def count_card(self, value):
        if value == 1 or value == 10:
            self.count -= 1
        elif value >= 2 and value <= 6:
            self.count += 1

    def check_winner(self):
        hands = []
        dealer_total = self.dealer_deal_out()
        for hand in range(len(self.player.cards)):
            total = self.check_player(hand)
            if total > 21:
                hands.append('L')
            elif dealer_total == 0:
                hands.append('W')
            elif dealer_total > total:
                hands.append('L')
            elif dealer_total < total:
                hands.append('W')
            else:
                hands.append('P')
        return hands
