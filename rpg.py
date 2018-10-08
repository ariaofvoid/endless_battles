class Character():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        print "A '{0}' has been born, with {1}hp!".format(name,health)
