from src.constants import *
from src.direction import Directon

class Engine:
    def __init__(self, type, dir=Directon(BASE_DIR)):
        self.type = type
        self.dir = dir

    def turn(self, dir):
        self.dir += dir

    def draw(self, vec, artist, on_off=False):
        artist.draw_engine(vec, self.dir, self.type, on_off)

    def turn_a_little(self, clockwise):
        if clockwise:
            self.turn(Directon(SMALL_ANGLE))
        else:
            self.turn(Directon(SMALL_ANTI_ANGLE))

    def give_power(self):
        return self.dir * ENGINE_POWER
