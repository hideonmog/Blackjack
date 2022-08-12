from deck import Deck

class Player:
    def __init__(self, dealer, deck):
        self.cards = []
        self.dealer = dealer
        self.deck = deck
        self.score = 0

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        if self.score > 21:
            return 1
        else:
            return 0

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.check_score()
        if self.score == 21:
            return 1
        else:
            return 0

    def check_score(self):
        aces = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                aces += 1
            self.score += card.price()

        while aces != 0 and self.score > 21:
            aces -= 1
            self.score -= 10
        return self.score

    def show(self, deal = False):
        if deal:
            if self.dealer:
                print('Dealer\'s hand')
                self.cards[1].show()
                print('Score: ' + str(self.cards[1].price()))
        else:
            if self.dealer:
                print('Dealer\'s hand')
            else:
                print('Player\'s hand')

            for card in self.cards:
                card.show()

            print('Score: ' + str(self.score))