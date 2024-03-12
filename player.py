from characters import Character

class Player:
    def __init__(self, char1: Character, char2: Character) -> None:
        self.character_1: Character = char1
        self.character_2: Character = char2
        self.is_out = False

    def update_is_alive(self) -> None:
        self.is_out = True if self.character_1.is_alive or self.character_2.is_alive else False 

    def is_alive(self) -> bool:
        return self.is_alive