from constants import *
from vector import Vector
from direction import Directon
class Ship:

    def __init__(self):
        self.center = Vector(ship_start_pos)
        self.angle = Directon(base_dir)
        self.cells = []
        self.speed = Vector((0, 0))
        self.spin = Directon(base_dir)

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
            if (self.cells[i].say_pos(self.center) - point).lenght() <= real_rad_cell:
                return i
        return -1

    def make_a_step(self, actual_types):
        self.speed += Vector(attraction)
        self.angle -= self.spin
        for cell in self.cells:
            cell.turn(self.spin)

        for cell in self.cells:
            if actual_types[cell.say_type()]:
                pulse = cell.give_power()
                pulse *= ((1 / pulse.lenght()) * power_of_engine)
                pr = (cell.dir * ((cell.dist + ship_size) / 2)).find_projection(pulse)
                self.speed += pulse * engine_power
                sp = (cell.dir * ((cell.dist + ship_size) / 2)) + (pulse - pr) * engine_power
                sp *= 1 / sp.lenght()
                self.spin += (Directon(sp.make_point()) - cell.dir)
        self.center += self.speed

    def does_touch_haters(self, haters):
        for hater in haters:
            if (self.center - hater.say_center()).lenght() < ship_size + hater.say_size():
                return True
        return False

    def is_in_screen(self):
        return (0 + ship_size <= self.center.x <= SCREEN_WIDTH - ship_size) and (
                0 + ship_size <= self.center.y <= SCREEN_HEIGHT - ship_size)

    def to_factory_settings(self):
        for cell in self.cells:
            cell.turn(self.angle)
        self.center = Vector(ship_start_pos)
        self.angle = Directon(base_dir)
        self.speed = Vector((0, 0))
        self.spin = Directon(base_dir)

    def in_ship(self, ind):
        return (self.center - ind).lenght() <= ship_size