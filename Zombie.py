
class Zombie:
    face1 = "_&"
    face2 = " &"
    big_face1 = "[´ཀ`]"
    big_face2 = "[`ཀ´]"
    leg_walk1 = " <\\"
    leg_walk2 = " /<"
    leg_limp1 = " <"
    leg_limp2 = " /"
    alive = True
    tick = 0
    dead1 = " + "
    dead2 = "- -"
    dead3 = "<   >"

    def __init__(self, x, y, default_face=face1, angry_face=face2, hp=3, speed=1):
        self.max_hp = hp
        self.hp = hp
        self.speed = speed
        self.x = x
        self.y = y
        self.alive = True
        self.leg_stance = 0
        self.counter = 0
        self.face = default_face
        self.angry_face = angry_face
        self.leg = "/\\"
        

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
            self.face = self.angry_face

        if self.tick % 4 == 0:
            if self.leg_stance % 2 == 0:
                if self.hp == 1:
                    self.leg = self.leg_limp1
                else:
                    self.leg = self.leg_walk1
            else:
                if self.hp == 1:
                    self.leg = self.leg_limp2
                else:
                    self.leg = self.leg_walk2
            self.leg_stance += 1
        self.tick += 1


    def zombiw_dead():
        pass