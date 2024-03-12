import random

class Dice:
    def __init__(self) -> None: 
        self.sides = ['red', 'yellow', 'green', 'blue', 'white', 'white']

    def roll(self):
        return random.choice(self.sides)