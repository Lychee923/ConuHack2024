class Player:
    tick = 0
    walk_stance = 0
    stance = " o  \nn+--\n /\\  "
    
    def __init__(self, y, hp):
        self.y = y
        self.width = 4
        self.height = 3
        self.hp = hp
        

    # Moving up and down
    def move(self, direction):
        self.y += direction

    # Get walking stance
    def update_stance(self):
        if self.tick % 4 == 0:
            if self.walk_stance % 2 == 0:
                self.stance = " o  \nn+--\n/>  "
            else:
                self.stance = " o  \nn+--\n>\\  "
            self.walk_stance += 1
        self.tick += 1


'''
Player animations
Walking:
" o  \nn+--\n />  "
" o  \nn+--\n >\\  "
'''
