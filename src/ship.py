from src.constants import *
from src.vector import Vector
from src.direction import Directon

class Ship:

    def __init__(self):
        self.center = Vector(SHIP_START_POS)
        self.angle = Directon(BASE_DIR)
        self.cells = []
        self.speed = Vector((0, 0))
        self.spin = Directon(BASE_DIR)

    def draw(self, artist, actual_types):
        artist.draw_ship(self.center, self.angle)
        for cell in self.cells:
            cell.draw(self.center, artist, actual_types[cell.say_type()])

    def add_cell(self, new_cell):
        self.cells.append(new_cell)

    def del_cell(self, ind):
        self.cells.pop(ind)

    def ind_of_cell(self, point):
        for i in range(len(self.cells)):
            if (self.cells[i].say_pos(self.center) - point).lenght() <= REAL_RAD_CELL:
                return i
        return -1

    def make_a_step(self, actual_types):
        self.speed += Vector(ATTRACTION)
        self.angle -= self.spin
        for cell in self.cells:
            cell.turn(self.spin)

        for cell in self.cells:
            if actual_types[cell.say_type()]:
                pulse = cell.give_power()
                pulse *= ((1 / pulse.lenght()) * POWER_OF_ENGINE)
                pr = (cell.dir * ((cell.dist + SHIP_SIZE) / 2)).find_projection(pulse)
                self.speed += pulse * ENGINE_POWER
                sp = (cell.dir * ((cell.dist + SHIP_SIZE) / 2)) + (pulse - pr) * ENGINE_POWER
                sp *= 1 / sp.lenght()
                self.spin += (Directon(sp.make_point()) - cell.dir)
        self.center += self.speed

    def does_touch_haters(self, haters):
        for hater in haters:
            if (self.center - hater.say_center()).lenght() < SHIP_SIZE + hater.say_size():
                return True
        return False

    def is_in_screen(self):
        return (0 + SHIP_SIZE <= self.center.x <= SCREEN_WIDTH - SHIP_SIZE) and (
                0 + SHIP_SIZE <= self.center.y <= SCREEN_HEIGHT - SHIP_SIZE)

    def to_factory_settings(self):
        for cell in self.cells:
            cell.turn(self.angle)
        self.center = Vector(SHIP_START_POS)
        self.angle = Directon(BASE_DIR)
        self.speed = Vector((0, 0))
        self.spin = Directon(BASE_DIR)

    def in_ship(self, ind):
        return (self.center - ind).lenght() <= SHIP_SIZE
