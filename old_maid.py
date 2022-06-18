import random

from player import Player

class OldMaid():
    def __init__(self, players: list) -> None:
        self.players = players
        self.rank = []

    def create_turn_index(self, passer_i: int, drawer_i: int) -> tuple:
        """
        Create an index to determin if it is passer or drawer.
        """
        def decide_turn_index(
            turn_i: int, players: list, check_equal: int = None) -> int:
            """
            Decide a turn index.
            """
            while True:
                if turn_i >= len(players):
                    turn_i = 0
                if not players[turn_i].card_exists:
                    turn_i += 1
                    continue
                if turn_i == check_equal:
                    turn_i += 1
                    continue
                break
            return turn_i

        passer_i = drawer_i
        passer_i = decide_turn_index(passer_i, self.players)
        
        drawer_i = passer_i + 1
        drawer_i = decide_turn_index(drawer_i, self.players, check_equal=passer_i)
        return passer_i, drawer_i

    def check_is_zero(self, player: dict, rank: list) -> None:
        """
        Check how many cards player have on hand.
        """
        if len(player.deck) == 0:
            player.card_exists = False
            rank.append(player.name)

    def select(self, passer: object, drawer: object) ->str:
        """
        Select card.
        *(passer["deck]) Return is not required for destructive methods(pop).
        """
        if drawer.is_auto:
            select_index = random.randrange(len(passer.deck))
        else:
            while True:
                text = ''
                for n in range(len(passer.deck)):
                    text += f'[{n+1}]'
                select_index = input(f'Select Card of {passer.name} from {text}: ')
                try:
                    select_index = int(select_index) - 1
                    if select_index < 0 or select_index >= len(passer.deck):
                        raise IndexError()
                except ValueError:
                    print('\t*please input integer!!')
                except IndexError:
                    print('\t*please input right number!!')
                else:
                    break
            print(f'\tYou chose {select_index+1}.')
        selected_card = passer.deck.pop(select_index)
        return selected_card

    def putdown_or_add(self, selected_card: str, taker: object):
        """
        Put down or add a card.
        *Return is not required for destructive methods.
        """
        try:
            taker.deck.remove(selected_card)
        except ValueError:
            taker.deck.append(selected_card)

    def run(self):
        """
        Start the Game
        """
        passer_i = -1
        drawer_i = 0
        loop = 0

        print(f'GAME START')

        while len(self.players) - len(self.rank) > 1:
            loop += 1
            print(f'\n --- TURN {loop} ---')

            passer_i, drawer_i = self.create_turn_index(passer_i, drawer_i)

            selected_card = self.select(self.players[passer_i], self.players[drawer_i])
            self.check_is_zero(self.players[passer_i], self.rank)

            self.putdown_or_add(selected_card, self.players[drawer_i])
            self.check_is_zero(self.players[drawer_i], self.rank)

            print(f'\tCurrent card number: ', end='')
            for i in range(len(self.players)):
                print(f'{self.players[i].name}: {len(self.players[i].deck)} ', end='')

        player_name = [p.name for p in self.players if p.card_exists][0]
        self.rank.append(player_name)

        print('\n\nGAME END\n')
        for i in range(len(self.rank)):
            print(f'RANK {i+1}: {self.rank[i]}')