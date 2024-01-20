
class Player:

    def __init__(self, y, hp):
        self.y = y
        self.width = 4
        self.height = 3
        self.hp = hp
        self.walk_stance = 0

    #Moving up and down
    def move(self, direction):
        self.y += direction

    #Walking stance
    def __str__(self):
        if self.walk_stance % 2 == 0:
            stance = " o  \nn+--\n />  "
        else:
            stance = " o  \nn+--\n >\\  "

        self.walk_stance += 1    
        return stance



'''
Player animations
Walking:
" o  \nn+--\n />  "
" o  \nn+--\n >\\  "
'''