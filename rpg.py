class Character():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print "A '{0}' has been born, with {1}hp!".format(name,hp)

    def get_hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

