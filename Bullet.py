class Bullet:
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.damage = damage
    
    def move(self):
        self.x += 1
        
        
        
