
class Zombie:
    face1 = "_&"
    face2 = " &"
    big_face = "[´ཀ`]"
    leg_walk1 = " <\\"
    leg_walk2 = " /<"
    leg_limp1 = " <"
    leg_limp2 = " /"
    alive = True
    tick = 0
    dead1 = " + "
    dead2 = "- -"
    dead3 = "<   >"

    def __init__(self, x, y, face = face1, hp=3, speed=1):
        self.max_hp = hp
        self.hp = hp
        self.speed = speed
        self.x = x
        self.y = y
        self.alive = True
        self.leg_stance = 0
        self.counter = 0
        self.face = face
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
            self.face = self.face2

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

    #def health_bar(self):
        #return str(self.hp) + f"/{self.max_hp}"
    

    def zombiw_dead():
        pass