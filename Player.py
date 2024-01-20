
class Player:

    def __init__(self, y, hp):
        self.y = y
        self.width = 4
        self.height = 3
        self.hp = hp
        self.sprite = " o  \nn+--\n /\\  "

    def move(self, direction):
        self.y += direction

'''
Player animations
Walking:
" o  \nn+--\n />  "
" o  \nn+--\n >\\  "
'''