import random

class Dealer():

    def __init__(self) -> None:
        self.initial_deck = self.create_initial_deck()

    def create_initial_deck(self) -> list:
        """
        Create list object with 53 cards.
        The Card X means Joker.
        """
        initial_deck = []

        for n in range(1, 14):
            if n == 1:
                card_number = 'A'
            elif n == 11:
                card_number = 'J'
            elif n == 12:
                card_number = 'Q'
            elif n == 13:
                card_number = 'K'
            else:
                card_number = str(n)

            initial_deck.append(card_number)

        # 4 suit each card
        initial_deck *= 4

        # add joker
        initial_deck.append('X')

        return initial_deck

    def initial_deal(self, *args: tuple)-> list: 
        """
        Deal cards to players automatically.
        """
        players = list(args)
        random.shuffle(self.initial_deck)
        q, mod = divmod(len(self.initial_deck), len(players))
        for i in range(len(players)):
            slice_n = q
            if i < mod:
                slice_n = q + 1
            players[i].deck = self.initial_deck[:slice_n]
            del self.initial_deck[:slice_n]
        return players

    def initial_putdown(self, deck: list) -> list:
        """
        Play(put down) matching cards.
        """
        while len(set(deck))!= len(deck):
            drawn_card = deck.pop(0)
            if drawn_card in deck:
                deck.remove(drawn_card)
            else:
                deck.append(drawn_card)
        return deck