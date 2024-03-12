class Character:
    def __init__(self) -> None:
        self.room = None
        self.is_alive = True
        self.char_type = None
        self.player: int = None

    def set_player(self, player: int) -> None:
        self.player = player

    def is_player(self) -> bool:
        return self.player is not None