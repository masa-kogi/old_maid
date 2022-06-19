import random

class Player():

    def __init__(self, name: str, is_auto: bool = True) -> None:
        """
        Create a player.
        """   
        self.name = name
        self.is_out = False
        self.is_auto = is_auto


    def draw_card(self, passer: object) ->str:
        """
        Draw card.
        *(passer.cards Return is not required for destructive methods(pop).
        """

        def choose_card_number() -> int:
            while True:
                text = ''
                for n in range(len(passer.cards)):
                    text += f'[{n+1}] '
                input_value = input(
                    f'\n\n\tSelect card of {passer.name} from {text}: ')
                try:
                    selected_index = int(input_value) - 1
                    if selected_index < 0 or selected_index >= len(passer.cards):
                        raise IndexError()
                    return selected_index
                except ValueError:
                    print('\t*please input intger!!!')
                except IndexError:
                    print('\t*please input right number!!!')

        if self.is_auto:
            selected_index = random.randrange(len(passer.cards))
        else:
            selected_index = choose_card_number()
        print('\n\t', end='')
        selected_card = passer.cards.pop(selected_index)
        return selected_card

    def putdown_or_add(self, selected_card: str) -> list:
        """
        Put down or add a card.
        *Return is not required for destructive methods.
        """
        if selected_card in self.cards:
            self.cards.remove(selected_card)
        else:
            self.cards.append(selected_card)
        return self.cards

    def initial_putdown(self) -> list:
        """
        Play(put down) matching cards.
        """
        while len(set(self.cards))!= len(self.cards):
            selected_card = self.cards.pop(0)
            self.putdown_or_add(selected_card)
        return self.cards

    def is_win(self) -> bool:
        """
        Judge if the player wins.
        """
        return len(self.cards) ==0

    def __repr__(self) -> str:
        return self.name