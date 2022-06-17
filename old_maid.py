import random

class OldMaid():
    def __init__(self, players: list) -> None:
        self.players = players

    def create_turn_index(self, passer_i: int, drawer_i: int) -> tuple:
        """
        Create an index to determin if it is passer or drawer
        """
        passer_i, drawer_i = drawer_i, drawer_i + 1
        if passer_i >= len(self.players):
            passer_i = 0
            drawer_i = 1
        elif drawer_i >= len(self.players):
            drawer_i = 0
        return passer_i, drawer_i

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
        rank = []

        print(f'GAME START')

        while True:
            loop += 1
            print(f'\n --- TURN {loop} ---')

            passer_i, drawer_i = self.create_turn_index(passer_i, drawer_i)

            selected_card = self.select(self.players[passer_i], self.players[drawer_i])

            self.putdown_or_add(selected_card, self.players[drawer_i])

            print(f'\tCurrent card number: ', end='')
            for i in range(len(self.players)):
                print(f'{self.players[i].name}: {len(self.players[i].deck)} ', end='')
                if len(self.players[i].deck) == 0:
                    print('*WIN', end='')
                    rank.append(self.players.pop(i))
                    break

            if len(self.players) < 2:
                break

        rank.append(self.players.pop())

        print('\n\nGAME END\n')
        for i in range(len(rank)):
            print(f'RANK {i+1}: {rank[i].name}')