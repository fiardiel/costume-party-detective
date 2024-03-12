from characters import Character

class Room:
    def __init__(self, room: str, right, left, front) -> None:
        self.room = room
        self.right: Room = right
        self.left: Room = left
        self.front: Room = front
        self.characters: set[Character] = set()

