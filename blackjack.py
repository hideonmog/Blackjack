from deck import Deck
from players import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate_deck()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()
        self.player.show()
        self.dealer.show(True)

        if player_status == 1:
            print('You got Blackjack! Player wins!')
            if dealer_status == 1:
                print('Dealer also got Blackjack! It\'s a push.')
                return 1

        cmd = ''
        while cmd.lower() != 'stand':
            bust = 0
            cmd = input('Hit or Stand? \n')
            if cmd.lower() == 'hit':
                bust = self.player.hit()
                self.player.show()
                self.dealer.show(True)
            if bust == 1:
                print("You went bust. Player loses, good game!")
                return 1
            print('\n')
            if dealer_status == 1:
                self.dealer.show()
                print("Dealer got Blackjack! Better luck next time!")
                return 1

        while self.dealer.check_score() < 17:
            self.dealer.hit()
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer went bust. Congrats!")
            else:
                return 1

        if self.dealer.check_score() == self.player.check_score():
            print("It\'s a push. Better luck next time!")
        elif self.player.check_score() < self.dealer.check_score() <= 21 :
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")

        self.player.show()
        self.dealer.show()
        
blackjack = Blackjack()
blackjack.play()