class Bullet:
    speed = 1

    def __init__(self, x, y, damage, hyper=False):
        self.x = x
        self.y = y
        self.damage = damage
        self.hyper = hyper

    def move(self):
        self.x += self.speed
