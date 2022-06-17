import random


def create_initial_deck() -> list:
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

def create_player(name: str, is_auto: bool = True) -> dict:
    """
    Create a player dict.
    """
    return {
        'name': name,
        'deck': [],
        'is_win': False,
        'is_auto': is_auto,
    }



def initial_deal(initial_deck: list, *args: tuple)-> list: 
    """
    Deal cards to players automatically.
    """
    players = list(args)
    random.shuffle(initial_deck)
    q, mod = divmod(len(initial_deck), len(players))
    for i in range(len(players)):
        slice_n = q
        if i < mod:
            slice_n = q + 1
        players[i]["deck"] = initial_deck[:slice_n]
        del initial_deck[:slice_n]
    return players


def initial_putdown(deck: list) -> list:
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


initial_deck = create_initial_deck()

player1 = create_player('A')
player2 = create_player('B')
player3 = create_player('C')

players = initial_deal(initial_deck, player1, player2, player3)

for i in range(len(players)):
    players[i]["deck"] = initial_putdown(players[i]["deck"])

print(players[0]["deck"])
print(players[1]["deck"])
print(players[2]["deck"])

