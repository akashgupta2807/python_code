#! /usr/bin/env python3

class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

player1 = GameCharacter('roger',10)
player2 = GameCharacter('alex',10)
player3 = GameCharacter('bob',10)


print(player1.name)
print(player2.name)
