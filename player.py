from unicodedata import name


class Player():

    def __init__(self, name: str, is_auto: bool = True) -> None:
        """
        Create a player.
        """
        self.name = name
        self.deck = []
        self.is_win = False
        self.is_auto = is_auto

    def __repr__(self) -> str:
        return self.name