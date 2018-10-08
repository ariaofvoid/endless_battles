import sys
import rpg


def check_death(characters):
    # return true if every character in the list is dead
    for char in characters:
        if char.hp != 0:
            return False
    return True


# print python version & welcome message
print sys.version
print "-" * 20 + "\n\n\n"
print "Welcome to Endless Battles!"

# Game setup
player = rpg.Character("Link", 100)
foes = [rpg.Character("Undead Knight", 50), rpg.Character("Medusa", 35)]


# Game main loop
#while check_death(foes):
