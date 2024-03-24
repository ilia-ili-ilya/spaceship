class Cell:
    def __init__(self, dir, dist, body):
        self.type = body.type
        self.dir = dir
        self.dist = dist
        self.body = body

    def say_type(self):
        return self.type

    def say_pos(self, cent):
        return cent + self.dir * self.dist

    def draw(self, vec, artist, on_off=False):
        self.body.draw(vec + self.dir * self.dist, artist, on_off)

    def turn(self, dir):
        self.dir += dir
        self.body.turn(dir)

    def give_power(self):
        return self.body.give_power()
