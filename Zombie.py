
class Zombie:
    head = "_<"
    legs1 = "<\\"

    legs2 = "/<"

    def __init__(self, x, y, hp=3, speed=1):
        self.hp = hp
        self.speed = speed
        self.x = x
        self.y = y
        self.alive = True

    def move(self, direction):
        if direction == "LEFT":
            self.x -= self.speed
        if direction == "UP":
            self.y += 1
        if direction == "DOWN":
            self.y -= 1

    def take_damage(self, damage=1):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False
        if self.hp == 2:
            self.speed += 1