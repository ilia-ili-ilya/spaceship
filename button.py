from vector import Vector
class Button:
    def __init__(self, left_up, right_down, text):
        self.left_up = Vector(left_up)
        self.right_down = Vector(right_down)
        self.text = text

    def draw(self, artist):
        artist.draw_button(self.left_up, self.right_down, self.text)

    def is_pressed(self, vec):
        return (self.left_up.x < vec.x < self.right_down.x) and (self.left_up.y < vec.y < self.right_down.y)
