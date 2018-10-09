import random
from enum import Enum


class Character:
    def __init__(self, name, stats, hp):
        self.name = name
        self.hp = hp
        self.stats_str = stats[0]
        self.stats_dex = stats[1]
        self.stats_con = stats[2]
        self.stats_int = stats[3]
        self.stats_wis = stats[4]
        self.stats_chm = stats[5]
        print("A '{0}' has been born, with {1}hp!".format(name,hp))

    def get_hit(self, damage):
        self.hp -= damage
        print("{0} has recieved {1} damage!".format(self.name, damage))
        if self.hp <= 0:
            self.hp = 0
            print("{0} has been defeated!")

    def attack(self):
        dice = random.randint(1, 12)
        damage = self.stats_str + dice
        return damage


class Element(Enum):
    PHYSICAL = 1
    FIRE = 2
    COLD = 3
    SHOCK = 3
    ACID = 4


class Skill:
    def __init__(self, name: str, element: Element, damage: int, mp_cost: int):
        self.name = name
        self.element = element
        self.damage = damage
        self.mp_cost = mp_cost
