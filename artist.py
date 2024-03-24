import pygame

from random import random, randint, choice
from constants import *
from direction import Directon

class Artist:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_sreen(self, color=SCREEN_COLOR):
        self.screen.fill(color)

    def draw_engine(self, vec, dir, type, on_off=False):
        pygame.draw.line(self.screen, ENGINE_TURBINE_COLOR, (vec + dir * engine_size).make_point(),
                         (vec - dir * engine_size).make_point(), 7)
        if type == 1:
            if not on_off:
                pygame.draw.circle(self.screen, GREEN, (vec - dir * engine_size).make_point(), engine_core_size)
            else:
                pygame.draw.circle(self.screen, (randint(0, 255), randint(127, 255), randint(0, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size_on)
                pygame.draw.circle(self.screen, (randint(0, 255), randint(127, 255), randint(0, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size)
        if type == 2:
            if not on_off:
                pygame.draw.circle(self.screen, RED, (vec - dir * engine_size).make_point(), engine_core_size)
            else:
                pygame.draw.circle(self.screen, (randint(127, 255), randint(0, 255), randint(0, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size_on)
                pygame.draw.circle(self.screen, (randint(127, 255), randint(0, 255), randint(0, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size)
        if type == 3:
            if not on_off:
                pygame.draw.circle(self.screen, BLUE, (vec - dir * engine_size).make_point(), engine_core_size)
            else:
                pygame.draw.circle(self.screen, (randint(0, 255), randint(0, 255), randint(127, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size_on)
                pygame.draw.circle(self.screen, (randint(0, 255), randint(0, 255), randint(127, 255)),
                                   (vec - dir * engine_size).make_point(), engine_core_size)

    def draw_ship(self, vec, dir):
        pygame.draw.circle(self.screen, SHIP_COLOR, (vec.make_point()), ship_size)

    def draw_stub(self, vec):
        pygame.draw.circle(self.screen, CELL_COLOR, (vec.make_point()), cell_size)

    def draw_hater(self, vec, size):
        pygame.draw.circle(self.screen, HATER_COLOR, (vec.make_point()), size)

    def update_screen(self):
        pygame.time.wait(fps)
        pygame.display.update()

    def draw_button(self, left_up, right_down, text):
        pygame.draw.rect(self.screen, BUTTON_COLOR2,
                         (left_up.x + 2, left_up.y + 2, right_down.x - left_up.x - 4, right_down.y - left_up.y - 4))
        pygame.draw.rect(self.screen, BUTTON_COLOR,
                         (left_up.x + 2, left_up.y + 2, right_down.x - left_up.x - 4, right_down.y - left_up.y - 4), 8)
        if text in ['1', '2', '3']:
            self.draw_engine((left_up + right_down) * 0.5, Directon(base_dir), int(text), True)  # лучше и False
        else:
            self.draw_text((left_up + right_down) * 0.5, text)

    def draw_text(self, vec, text):
        self.screen.blit(pygame.font.Font(None, 36).render(text, 1, TEXT_COLOR), (
            pygame.font.Font(None, 36).render(text, 1, TEXT_COLOR).get_rect(
                center=(vec).make_point())))

    #def draw_result(self, result):


