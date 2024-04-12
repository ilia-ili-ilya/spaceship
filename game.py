from random import random, randint, choice
from constants import *
from hater import Hater

class Game:
    def __init__(self, ship, artist, looker):
        self.ship = ship
        self.haters = []
        self.artist = artist
        self.looker = looker
        self.actual_types = [False] * count_of_types
        self.result = 0

    def update_types(self):
        self.looker.update_keys()
        self.actual_types[1] = self.looker.get_key('1')
        self.actual_types[2] = self.looker.get_key('2')
        self.actual_types[3] = self.looker.get_key('3')

    def check(self):
        if not self.ship.is_in_screen():
            return False
        if self.ship.does_touch_haters(self.haters):
            return False
        return True

    def resalt(self):
        return self.result

    def one_step(self):
        self.ship.make_a_step(self.actual_types)
        new_haters = []
        for i in range(len(self.haters)):
            if self.haters[i].make_a_step():
                new_haters.append(self.haters[i])
        self.haters = new_haters
        self.result += 1
        if self.result % 50 == 0:
            self.add_hater(self.result % 100)

    def draw(self):
        self.artist.draw_sreen()
        self.ship.draw(self.artist, self.actual_types)
        for hater in self.haters:
            hater.draw(self.artist)
        self.artist.update_screen()

    def add_hater(self, ud_or_lr):
        if ud_or_lr:
            self.haters.append(
                Hater((choice([0, SCREEN_WIDTH]), randint(0, SCREEN_HEIGHT)), self.ship.center.make_point()))
        else:
            self.haters.append(
                Hater((randint(0, SCREEN_WIDTH), choice([0, SCREEN_HEIGHT])), self.ship.center.make_point()))