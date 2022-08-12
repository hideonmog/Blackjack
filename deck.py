from cards import Card
import random

class Deck:
    def __init__(self):
        self.cards = []

    def generate_deck(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))

    def draw(self, draws):
        cards = []
        for i in range(draws):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)