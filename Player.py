
class Player:

    def __init__(self, y, hp):
        self.y = y
        self.hp = hp
        self.sprite = " o  \nn+--\n /\\  "

    def move(self, direction):
        self.y += direction




