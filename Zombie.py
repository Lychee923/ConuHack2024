import random


class Zombie:
    face1 = "_&"
    face11 = " &"
    # face2 = "_$"
    # face22 = " $"
    face2 = "[´ཀ`]"
    face22 = "[`ཀ´]"
    leg_walk1 = " <\\"
    leg_walk2 = " /<"
    leg_limp1 = " <"
    leg_limp2 = " /"
    alive = True
    dead1 = "+"
    dead2 = "<>"
    dead3 = "| |"

    def __init__(self, x, y, hp=3, speed=1):
        self.max_hp = hp
        self.hp = hp
        self.speed = speed
        self.x = x
        self.y = y
        self.alive = True
        self.leg_stance = 0
        self.leg = "/\\"
        self.counter = 0
        self.tick = 0
        if random.getrandbits(1):
            self.face = Zombie.face1
        else:
            self.face = Zombie.face2

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
        else:
            self.speed = 1

    def update_body(self):
        if self.hp <= 2:
            if self.face == Zombie.face1:
                self.face = Zombie.face11
            elif self.face == Zombie.face2:
                self.face = Zombie.face22

        if self.tick % 4 == 0:
            if self.leg_stance % 2 == 0:
                if self.hp == 1:
                    self.leg = Zombie.leg_limp1
                else:
                    self.leg = Zombie.leg_walk1
            else:
                if self.hp == 1:
                    self.leg = Zombie.leg_limp2
                else:
                    self.leg = Zombie.leg_walk2
            self.leg_stance += 1
        self.tick += 1
