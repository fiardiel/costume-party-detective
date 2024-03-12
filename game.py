from characters import Character
from card import Card
from room import Room

class Game:
    def __init__(self, n_players: int = 0) -> None:
        self.players: list[int] = [i+1 for i in range(n_players)]
        self.characters: dict[str, Character] = {
            # make 16 general characters
            'Alien': Character('Alien'),
            'Astronaut': Character('Astronaut'),
            'Biologist': Character('Biologist'),
            'Captain': Character('Captain'),
            'Detective': Character('Detective'),
            'Doctor': Character('Doctor'),
            'Engineer': Character('Engineer'),
            'Soldier': Character('Soldier'),
            'Ninja': Character('Ninja'),
            'Pirate': Character('Pirate'),
            'Robot': Character('Robot'),
            'Spy': Character('Spy'),
            'Thief': Character('Thief'),
            'Vampire': Character('Vampire'),
            'Werewolf': Character('Werewolf'),
            'Zombie': Character('Zombie'),
        }
        self.cards: dict[str, Card] = {char: self.characters[char] for char in self.characters}
        self.rooms: dict[Room, set[Character]] = {}