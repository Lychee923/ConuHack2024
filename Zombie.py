
class Zombie:
    face = "_&"
    leg1 = " <\\"
    leg2 = " /<"
    alive = True
    tick = 0
    leg_stance =0
    leg = "/\\"
    dead1 = " + "
    dead2 = "- -"
    dead3 = "<   >"

    def __init__(self, x, y, hp=3, speed=1):
        self.hp = hp
        self.speed = speed
        self.x = x
        self.y = y
        

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

    def update_leg(self):
        if self.tick % 6 == 0:
            if self.leg_stance % 2 == 0:
                self.leg = self.leg1
            else:
                self.leg = self.leg2
            self.leg_stance += 1
        self.tick += 1

    def zombiw_dead():
        pass