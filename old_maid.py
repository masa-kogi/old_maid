class OldMaid():
    def __init__(self, players: list) -> None:
        self.players = players
        self.rank = []

    def set_role(self, index: int) -> object:
        """
        Set passer or drawer by index.
        """
        while self.players[index].is_out:
            index = (index + 1) % len(self.players)
        return self.players[index]

    def set_winner_rank(self, winner: object) -> None:
        """
        Add winner's name to the rank order list
        """
        winner.is_out = True
        self.rank.append(winner.name)

    def show_current_status(self) -> None:
        """
        Show player's name and current card numbers.
        """
        print(f'\tCurrent card number: ', end='')
        for i in range(len(self.players)):
            print(f'{self.players[i].name}: {len(self.players[i].cards)} ', end='')

    def get_loser(self) -> object:
        """
        Get loser from players list.
        """
        return [player for player in self.players if not player.is_out][0]        

    def show_final_result(self, rank: list) -> None:
        """
        Show game final result.
        """
        print('\n\nGAME END\n')
        for i in range(len(rank)):
            print(f'RANK {i+1}: {rank[i]}') 

    def run(self) -> None:
        """
        Start game.
        """
        passer_index = 0
        loop = 0

        player_num = len(self.players)
        current_player_num = player_num - len(self.rank)
        print(f'GAME START')

        while current_player_num >  1:
            loop += 1
            print(f'\n --- TURN {loop} ---')

            passer = self.set_role(passer_index % player_num)
            drawer = self.set_role((self.players.index(passer) + 1) % player_num)

            selected_card = drawer.draw_card(passer)

            if passer.is_win():
                passer.is_out = True
                self.set_winner_rank(passer)

            drawer.putdown_or_add(selected_card)
            if drawer.is_win():
                drawer.is_out = True
                self.set_winner_rank(drawer)

            self.show_current_status()

            # set passer_index to current drawer's index
            passer_index = self.players.index(drawer)
            current_player_num = player_num - len(self.rank)

        loser = self.get_loser()
        self.set_winner_rank(loser)

        self.show_final_result(self.rank)

        