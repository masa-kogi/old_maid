from deck import Deck
from player import Player
from old_maid import OldMaid

def set_player_num():
    while True:
        try:
            input_value = input('Please input players number(2 or 3 or 4)')
            player_num = int(input_value)
            if not 1 < player_num <= 4:
                raise IndexError()
            return player_num
        except ValueError:
            print('\t*please input intger!!!')
        except IndexError:
            print('\t*please input right number!!!')

def main():
    player_num = set_player_num()
    
    deck = Deck()

    you = Player('you', is_auto=False)
    players = [you]
    for i in range(player_num-1):
        players.append(Player(f'player{i+1}'))

    # Deal cards to each player
    deck.deal_cards(players)

    # remove duplicate cards from each player's cards
    for player in players:
        player.initial_putdown()

    old_maid = OldMaid(players)
    old_maid.run()

    
main()