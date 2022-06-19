import random

class Deck():

    CARD_NUM = 13

    def __init__(self) -> None:
        """
        Create deck.
        """
        self.initial_deck = self.create_initial_deck()

    def create_initial_deck(self) -> list:
        """
        Create list object with 53 cards.
        The Card X means Joker.
        """
        initial_deck = []

        for n in range(1, self.CARD_NUM + 1):
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

    def deal_cards(self, players: list)-> list: 
        """
        Deal cards to players automatically.
        """
        random.shuffle(self.initial_deck)
        q, mod = divmod(len(self.initial_deck), len(players))
        for i in range(len(players)):
            player = players[i]
            slice_position = q
            if i < mod:
                slice_position = q + 1
            player.cards = self.initial_deck[:slice_position]
            del self.initial_deck[:slice_position]
        return players
