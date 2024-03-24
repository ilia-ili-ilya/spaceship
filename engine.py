from constants import *
from direction import Directon
class Engine:
    def __init__(self, type, dir=Directon(base_dir)):
        self.type = type
        self.dir = dir

    def turn(self, dir):
        self.dir += dir

    def draw(self, vec, artist, on_off=False):
        artist.draw_engine(vec, self.dir, self.type, on_off)

    def turn_a_little(self, clockwise):
        if clockwise:
            self.turn(Directon(small_angle))
        else:
            self.turn(Directon(small_anti_angle))

    def give_power(self):
        return self.dir * engine_power
