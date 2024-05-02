from time import sleep
from random import choice

from src.constants import *
from src.vector import Vector
from src.direction import Directon
from src.artist import Artist
from src.looker import Looker
from src.engine import Engine
from src.cell import Cell
from src.ship import Ship
from src.game import Game
from src.button import Button


class Garage:
    def __init__(self):
        self.ship = Ship()
        self.artist = Artist()
        self.looker = Looker()
        self.buttons_engines = [Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, 0),
                                       (SCREEN_WIDTH, SIZE_OF_BUTTON_Y), '1'),
                                Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y),
                                       (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 2), '2'),
                                Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 2),
                                       (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 3), '3'),
                                Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 3),
                                       (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 4), 'START')]
        self.buttons_technical = [Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, 0), (SCREEN_WIDTH, SIZE_OF_BUTTON_Y), '<'),
                                  Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y),
                                         (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 2), '>'),
                                  Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 2),
                                         (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 3), 'OK'),
                                  Button((SCREEN_WIDTH - SIZE_OF_BUTTON_X, SIZE_OF_BUTTON_Y * 3),
                                         (SCREEN_WIDTH, SIZE_OF_BUTTON_Y * 4), 'delete')]

    def one_game(self):
        game = Game(self.ship, self.artist, self.looker)
        while True:
            game.update_types()
            game.one_step()
            if not game.check():
                self.ship.to_factory_settings()
                return game.result
            game.draw()

    def follow_mouse(self, type):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                if self.ship.in_ship(Vector(cursor)):
                    self.ship.add_cell(Cell(Directon(((Vector(cursor) - self.ship.center) * (
                            1 / (Vector(cursor) - self.ship.center).lenght())).make_point()),
                                            (Vector(cursor) - self.ship.center).lenght(),
                                            Engine(int(type), Directon(BASE_DIR))))
                return
            else:
                self.artist.draw_sreen()
                self.ship.draw(self.artist, [False] * COUNT_OF_TYPES)

                self.artist.draw_engine(Vector(cursor), Directon(BASE_DIR), int(type))

                self.artist.update_screen()

    def technical_support_engine(self, ind):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                for button in self.buttons_technical:
                    if button.is_pressed(Vector(cursor)):
                        if button.text == '>':
                            self.ship.cells[ind].body.turn(Directon(SMALL_ANGLE))
                        elif button.text == '<':
                            self.ship.cells[ind].body.turn(Directon(SMALL_ANTI_ANGLE))
                        elif button.text == 'delete':
                            self.ship.del_cell(ind)
                            return
                        elif button.text == 'OK':
                            return
            self.artist.draw_sreen()
            self.ship.draw(self.artist, [False] * COUNT_OF_TYPES)
            for button in self.buttons_technical:
                self.artist.draw_button(button.left_up, button.right_down, button.text)
            self.artist.update_screen()

    def show_results(self, result):
        with open(RECORDS, "r") as f:
            records = [int(line.strip()) for line in f.readlines()]
        records.append(result)
        with open(RECORDS, "w") as f:
            for record in records:
                f.write("{}\n".format(record))
        self.artist.draw_sreen(SCREEN_COLOR)

        with open(CONGRATULATIONS, "r") as con:
            congratulation = choice([(line.strip()) for line in con.readlines()])
        self.artist.draw_text(Vector((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)), str(result))
        self.artist.draw_text(Vector((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)), congratulation)
        self.artist.update_screen()
        sleep(3)

    def menu(self):
        while True:
            click, cursor = self.looker.mouse_pos(True)
            if click:
                ind = self.ship.ind_of_cell(Vector(cursor))
                if ind != -1:
                    self.technical_support_engine(ind)
                else:
                    for button in self.buttons_engines:
                        if button.is_pressed(Vector(cursor)):
                            if button.text != 'START':
                                self.follow_mouse(button.text)
                            else:
                                self.show_results(self.one_game())
            self.artist.draw_sreen()
            self.ship.draw(self.artist, [False] * COUNT_OF_TYPES)
            for button in self.buttons_engines:
                self.artist.draw_button(button.left_up, button.right_down, button.text)
            self.artist.update_screen()
