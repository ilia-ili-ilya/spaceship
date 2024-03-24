from constants import *
from direction import Directon
from vector import Vector
class Stub:
    def __init__(self):
        self.type = 0
        self.dir = Directon(base_dir)

    def draw(self, vec, artist, on_off=False):
        artist.draw_stub(vec)

    def give_pover(self):
        return Vector((0, 0))

    def turn(self, dir):
        return