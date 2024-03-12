class Character:
    def __init__(self, char: str) -> None:
        self.char: str = char
        self.room = None
        self.is_alive = True
        self.player: int = None

    def set_player(self, player: int) -> None:
        self.player = player

    def is_player(self) -> bool:
        return self.player is not None