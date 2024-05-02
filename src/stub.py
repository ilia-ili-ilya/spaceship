from src.constants import *
from src.direction import Directon
from src.vector import Vector

class Stub:
    def __init__(self):
        self.type = 0
        self.dir = Directon(BASE_DIR)

    def draw(self, vec, artist, on_off=False):
        artist.draw_stub(vec)

    def give_pover(self):
        return Vector((0, 0))

    def turn(self, dir):
        return
