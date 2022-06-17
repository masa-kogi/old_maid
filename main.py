from dealer import Dealer
from player import Player
from old_maid import OldMaid

dealer = Dealer()

player1 = Player('A', is_auto=False)
player2 = Player('B')
player3 = Player('C')

players = dealer.initial_deal(player1, player2, player3)


for i in range(len(players)):
    players[i].deck = dealer.initial_putdown(players[i].deck)

old_maid = OldMaid(players)
old_maid.run()