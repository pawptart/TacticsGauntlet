import random
from data.objects.character import Character

class Team:
    PLAYER_CHARACTERS = ['marche']
    ENEMY_CHARACTERS = ['thief']

    def __init__(self, size, game, is_enemy=False):
        self.size = size
        self.game = game
        self.is_enemy = is_enemy
        self.characters = self.set_characters()

    def set_characters(self):
        valid_characters = self.ENEMY_CHARACTERS if self.is_enemy else self.PLAYER_CHARACTERS
        characters = []

        for _value in range(0, self.size):
            character = Character(random.choice(valid_characters), self.game, should_walk=True)
            characters.append(character)
        
        return characters

    def __len__(self):
        return len(self.characters)
        
    def __getitem__(self, value):
        return self.characters[value]