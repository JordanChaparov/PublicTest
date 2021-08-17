import pygame as pg
from os import path
import random
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QWidget
import csv
import pandas as pd

pg.font.init()
pg.mixer.init()
font_name = pg.font.match_font("comicsansms")
pg.display.set_caption("Sharingan Mahjong")
FPS = 40
TILE_HEIGHT = int(82)
TILE_WIDTH = int(67)
WIDTH = 22 * TILE_WIDTH
HEIGHT = 10 * TILE_HEIGHT
screen = pg.display.set_mode((WIDTH, HEIGHT))


class SpriteSheet:
    """Class for the tile pictures."""
    def __init__(self, filename):
        """Loading the sheet from an image file and convert it so the image pixes match the screen pixels."""
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        """Gets an image from the sheet and cuts it into pygame surface to load as a tile picture."""
        sprite = pg.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite


my_sprite_sheet = SpriteSheet(path.join(path.dirname(__file__), "images/sheet2.png"))
DEMON = my_sprite_sheet.get_sprite(374, 1234, 182, 235)
DEMON = pg.transform.scale(DEMON, (TILE_WIDTH, TILE_HEIGHT))
NOVA = my_sprite_sheet.get_sprite(0, 1234, 182, 235)
NOVA = pg.transform.scale(NOVA, (TILE_WIDTH, TILE_HEIGHT))
TRIRISE = my_sprite_sheet.get_sprite(1512, 988, 182, 235)
TRIRISE = pg.transform.scale(TRIRISE, (TILE_WIDTH, TILE_HEIGHT))
ENLIGHTENED = my_sprite_sheet.get_sprite(1130, 988, 182, 235)
ENLIGHTENED = pg.transform.scale(ENLIGHTENED, (TILE_WIDTH, TILE_HEIGHT))
NOEL = my_sprite_sheet.get_sprite(749, 988, 182, 235)
NOEL = pg.transform.scale(NOEL, (TILE_WIDTH, TILE_HEIGHT))
MIKOTO = my_sprite_sheet.get_sprite(375, 988, 182, 235)
MIKOTO = pg.transform.scale(MIKOTO, (TILE_WIDTH, TILE_HEIGHT))
SARADA = my_sprite_sheet.get_sprite(0, 988, 182, 235)
SARADA = pg.transform.scale(SARADA, (TILE_WIDTH, TILE_HEIGHT))
DOUBLE_TOMOE = my_sprite_sheet.get_sprite(1512, 739, 182, 236)
DOUBLE_TOMOE = pg.transform.scale(DOUBLE_TOMOE, (TILE_WIDTH, TILE_HEIGHT))
SHARINGAN = my_sprite_sheet.get_sprite(1132, 739, 182, 236)
SHARINGAN = pg.transform.scale(SHARINGAN, (TILE_WIDTH, TILE_HEIGHT))
SENNIN_KYUUBI = my_sprite_sheet.get_sprite(750, 739, 182, 236)
SENNIN_KYUUBI = pg.transform.scale(SENNIN_KYUUBI, (TILE_WIDTH, TILE_HEIGHT))
TENSEIGAN = my_sprite_sheet.get_sprite(374, 739, 182, 236)
TENSEIGAN = pg.transform.scale(TENSEIGAN, (TILE_WIDTH, TILE_HEIGHT))
BYAKUGAN = my_sprite_sheet.get_sprite(0, 739, 182, 236)
BYAKUGAN = pg.transform.scale(BYAKUGAN, (TILE_WIDTH, TILE_HEIGHT))
RINNEGAN = my_sprite_sheet.get_sprite(1514, 491, 182, 236)
RINNEGAN = pg.transform.scale(RINNEGAN, (TILE_WIDTH, TILE_HEIGHT))
SASUKE_RINNEGAN = my_sprite_sheet.get_sprite(1131, 491, 182, 236)
SASUKE_RINNEGAN = pg.transform.scale(SASUKE_RINNEGAN, (TILE_WIDTH, TILE_HEIGHT))
FUGAKU = my_sprite_sheet.get_sprite(749, 492, 182, 236)
FUGAKU = pg.transform.scale(FUGAKU, (TILE_WIDTH, TILE_HEIGHT))
SHISUI = my_sprite_sheet.get_sprite(374, 492, 182, 236)
SHISUI = pg.transform.scale(SHISUI, (TILE_WIDTH, TILE_HEIGHT))
SHIN = my_sprite_sheet.get_sprite(0, 492, 182, 236)
SHIN = pg.transform.scale(SHIN, (TILE_WIDTH, TILE_HEIGHT))
SASUKE = my_sprite_sheet.get_sprite(1512, 246, 182, 236)
SASUKE = pg.transform.scale(SASUKE, (TILE_WIDTH, TILE_HEIGHT))
RAI = my_sprite_sheet.get_sprite(1132, 246, 182, 236)
RAI = pg.transform.scale(RAI, (TILE_WIDTH, TILE_HEIGHT))
OBITO = my_sprite_sheet.get_sprite(750, 244, 182, 236)
OBITO = pg.transform.scale(OBITO, (TILE_WIDTH, TILE_HEIGHT))
NAORI = my_sprite_sheet.get_sprite(373, 245, 182, 236)
NAORI = pg.transform.scale(NAORI, (TILE_WIDTH, TILE_HEIGHT))
NAKA = my_sprite_sheet.get_sprite(0, 246, 182, 236)
NAKA = pg.transform.scale(NAKA, (TILE_WIDTH, TILE_HEIGHT))
MADARA = my_sprite_sheet.get_sprite(1512, 0, 182, 236)
MADARA = pg.transform.scale(MADARA, (TILE_WIDTH, TILE_HEIGHT))
IZUNA = my_sprite_sheet.get_sprite(1131, 1, 182, 237)
IZUNA = pg.transform.scale(IZUNA, (TILE_WIDTH, TILE_HEIGHT))
ITACHI = my_sprite_sheet.get_sprite(749, 0, 182, 236)
ITACHI = pg.transform.scale(ITACHI, (TILE_WIDTH, TILE_HEIGHT))
INDRA = my_sprite_sheet.get_sprite(372, 2, 182, 236)
INDRA = pg.transform.scale(INDRA, (TILE_WIDTH, TILE_HEIGHT))
BARU = my_sprite_sheet.get_sprite(0, 1, 182, 237)
BARU = pg.transform.scale(BARU, (TILE_WIDTH, TILE_HEIGHT))
DEMON2 = my_sprite_sheet.get_sprite(562, 1234, 182, 235)
DEMON2 = pg.transform.scale(DEMON2, (TILE_WIDTH, TILE_HEIGHT))
NOVA2 = my_sprite_sheet.get_sprite(186, 1234, 182, 235)
NOVA2 = pg.transform.scale(NOVA2, (TILE_WIDTH, TILE_HEIGHT))
TRIRISE2 = my_sprite_sheet.get_sprite(1700, 988, 182, 235)
TRIRISE2 = pg.transform.scale(TRIRISE2, (TILE_WIDTH, TILE_HEIGHT))
ENLIGHTENED2 = my_sprite_sheet.get_sprite(1321, 988, 182, 235)
ENLIGHTENED2 = pg.transform.scale(ENLIGHTENED2, (TILE_WIDTH, TILE_HEIGHT))
NOEL2 = my_sprite_sheet.get_sprite(938, 988, 182, 235)
NOEL2 = pg.transform.scale(NOEL2, (TILE_WIDTH, TILE_HEIGHT))
MIKOTO2 = my_sprite_sheet.get_sprite(560, 988, 182, 235)
MIKOTO2 = pg.transform.scale(MIKOTO2, (TILE_WIDTH, TILE_HEIGHT))
SARADA2 = my_sprite_sheet.get_sprite(186, 988, 182, 235)
SARADA2 = pg.transform.scale(SARADA2, (TILE_WIDTH, TILE_HEIGHT))
DOUBLE_TOMOE2 = my_sprite_sheet.get_sprite(1701, 739, 182, 236)
DOUBLE_TOMOE2 = pg.transform.scale(DOUBLE_TOMOE2, (TILE_WIDTH, TILE_HEIGHT))
SHARINGAN2 = my_sprite_sheet.get_sprite(1324, 739, 182, 236)
SHARINGAN2 = pg.transform.scale(SHARINGAN2, (TILE_WIDTH, TILE_HEIGHT))
SENNIN_KYUUBI2 = my_sprite_sheet.get_sprite(940, 739, 182, 236)
SENNIN_KYUUBI2 = pg.transform.scale(SENNIN_KYUUBI2, (TILE_WIDTH, TILE_HEIGHT))
TENSEIGAN2 = my_sprite_sheet.get_sprite(560, 739, 182, 236)
TENSEIGAN2 = pg.transform.scale(TENSEIGAN2, (TILE_WIDTH, TILE_HEIGHT))
BYAKUGAN2 = my_sprite_sheet.get_sprite(186, 739, 182, 236)
BYAKUGAN2 = pg.transform.scale(BYAKUGAN2, (TILE_WIDTH, TILE_HEIGHT))
RINNEGAN2 = my_sprite_sheet.get_sprite(1701, 491, 182, 236)
RINNEGAN2 = pg.transform.scale(RINNEGAN2, (TILE_WIDTH, TILE_HEIGHT))
SASUKE_RINNEGAN2 = my_sprite_sheet.get_sprite(1323, 491, 182, 236)
SASUKE_RINNEGAN2 = pg.transform.scale(SASUKE_RINNEGAN2, (TILE_WIDTH, TILE_HEIGHT))
FUGAKU2 = my_sprite_sheet.get_sprite(940, 492, 182, 236)
FUGAKU2 = pg.transform.scale(FUGAKU2, (TILE_WIDTH, TILE_HEIGHT))
SHISUI2 = my_sprite_sheet.get_sprite(560, 492, 182, 236)
SHISUI2 = pg.transform.scale(SHISUI2, (TILE_WIDTH, TILE_HEIGHT))
SHIN2 = my_sprite_sheet.get_sprite(186, 492, 182, 236)
SHIN2 = pg.transform.scale(SHIN2, (TILE_WIDTH, TILE_HEIGHT))
SASUKE2 = my_sprite_sheet.get_sprite(1701, 246, 182, 236)
SASUKE2 = pg.transform.scale(SASUKE2, (TILE_WIDTH, TILE_HEIGHT))
RAI2 = my_sprite_sheet.get_sprite(1323, 246, 182, 236)
RAI2 = pg.transform.scale(RAI2, (TILE_WIDTH, TILE_HEIGHT))
OBITO2 = my_sprite_sheet.get_sprite(940, 244, 182, 236)
OBITO2 = pg.transform.scale(OBITO2, (TILE_WIDTH, TILE_HEIGHT))
NAORI2 = my_sprite_sheet.get_sprite(560, 245, 182, 236)
NAORI2 = pg.transform.scale(NAORI2, (TILE_WIDTH, TILE_HEIGHT))
NAKA2 = my_sprite_sheet.get_sprite(187, 246, 182, 236)
NAKA2 = pg.transform.scale(NAKA2, (TILE_WIDTH, TILE_HEIGHT))
MADARA2 = my_sprite_sheet.get_sprite(1702, 0, 182, 236)
MADARA2 = pg.transform.scale(MADARA2, (TILE_WIDTH, TILE_HEIGHT))
IZUNA2 = my_sprite_sheet.get_sprite(1323, 1, 182, 237)
IZUNA2 = pg.transform.scale(IZUNA2, (TILE_WIDTH, TILE_HEIGHT))
ITACHI2 = my_sprite_sheet.get_sprite(939, 0, 182, 236)
ITACHI2 = pg.transform.scale(ITACHI2, (TILE_WIDTH, TILE_HEIGHT))
INDRA2 = my_sprite_sheet.get_sprite(561, 2, 182, 236)
INDRA2 = pg.transform.scale(INDRA2, (TILE_WIDTH, TILE_HEIGHT))
BARU2 = my_sprite_sheet.get_sprite(187, 0, 182, 236)
BARU2 = pg.transform.scale(BARU2, (TILE_WIDTH, TILE_HEIGHT))

BG_IMAGE = pg.image.load(path.join(path.dirname(__file__), "images/Background2.jpg"))
BG_IMAGE = pg.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))
PAUSE_IMAGE = pg.image.load(path.join(path.dirname(__file__), "images/pause.jpg"))
PAUSE_IMAGE = pg.transform.scale(PAUSE_IMAGE, (WIDTH, HEIGHT))
BORDER_IMAGE = pg.image.load(path.join(path.dirname(__file__), "images/border.png")).convert_alpha()
BORDER_IMAGE = pg.transform.scale(BORDER_IMAGE, (TILE_WIDTH-1, TILE_HEIGHT-1))

tiles_dict = {1: BARU, 2: INDRA, 3: ITACHI, 4: IZUNA, 5: MADARA, 6: NAKA, 7: NAORI, 8: OBITO, 9: RAI, 10: SASUKE,
              11: SHIN, 12: SHISUI, 13: FUGAKU, 14: SASUKE_RINNEGAN, 15: RINNEGAN, 16: BYAKUGAN, 17: TENSEIGAN,
              18: SENNIN_KYUUBI, 19: SHARINGAN, 20: DOUBLE_TOMOE, 21: SARADA, 22: MIKOTO, 23: NOEL, 24: ENLIGHTENED,
              25: TRIRISE, 26: NOVA, 27: DEMON}


def draw_text(surface, text, size, x, y):
    """Function to draw text on the screen in pygame."""
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, 1, (0, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    surface.blit(text_surface, text_rect)


class Tile(pg.sprite.Sprite):
    """Class for the tiles."""
    def __init__(self, game, x, y, z, tile_id, tile_type, selected):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        for _ in tiles_dict.items():
            self.image = pg.Surface((TILE_WIDTH, TILE_HEIGHT))
            self.tile_id = tile_id
            self.tile_type = tile_type
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.z = z
            self.selected = selected

    def update(self):
        self.rect.x = self.x * TILE_WIDTH
        self.rect.y = self.y * TILE_HEIGHT


class Game:
    """The main class of the game, that does the heavy lifting."""
    def __init__(self):
        pg.init()
        self.time_event, t = pg.USEREVENT+2, 5000
        pg.time.set_timer(self.time_event, t)
        self.movement_controller = True
        self.pause = False
        self.info = False
        self.music = True
        self.running = True
        self.bonus_points = 2250
        self.score = 0
        self.free_pairs = 0
        self.tile_xy_list = []
        self.tile_id_list = []
        self.tiles_compare_list = []
        self.tile_coordinates = []
        self.tile_type_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                                16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27] * 8
        self.mouse_collide = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.clock = pg.time.Clock()

    def new(self):
        """Loads the background music and plays it.
           If the file with highscores does not exist, creates it and sets header.
           Draws all the tiles on their coordinates."""
        pg.mixer.music.load("bg_music.mp3")
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(-1, 0.1)

        if not path.exists("highscores.csv"):
            with open("highscores.csv", "w", newline="", encoding="utf-8") as f:
                header = ["name", "score"]
                hs_row = [window.get_nickname(), self.score]
                writer = csv.writer(f, delimiter=",")
                writer.writerow(header)
                writer.writerow(hs_row)

        for i in range(0, 266):
            if i < 7:
                self.tile = Tile(self, i+5, 1, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(7, 13):
                self.tile = Tile(self, i+7, 1, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(13, 17):
                self.tile = Tile(self, i+2, 2, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(17, 28):
                self.tile = Tile(self, i-16, 2, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(28, 39, 2):
                self.tile = Tile(self, i-27, 3, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(39, 49, 2):
                self.tile = Tile(self, i-37, 4, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(49, 56):
                self.tile = Tile(self, i-46, 5, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(56, 66):
                self.tile = Tile(self, i-55, 6, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(66, 76, 2):
                self.tile = Tile(self, i-65, 7, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(76, 85, 2):
                self.tile = Tile(self, i-74, 8, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(85, 93):
                self.tile = Tile(self, i-72, 3, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(93, 101):
                self.tile = Tile(self, i-80, 4, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(101, 109):
                self.tile = Tile(self, i-88, 5, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(109, 117):
                self.tile = Tile(self, i-96, 6, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(117, 125):
                self.tile = Tile(self, i-104, 7, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(125, 133):
                self.tile = Tile(self, i-112, 8, 1, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((int(self.tile.x), self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(133, 139):
                self.tile = Tile(self, i-119, 8, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(139, 145):
                self.tile = Tile(self, i-125, 7, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(145, 151):
                self.tile = Tile(self, i-131, 6, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(151, 157):
                self.tile = Tile(self, i-137, 5, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(157, 163):
                self.tile = Tile(self, i-143, 4, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(163, 169):
                self.tile = Tile(self, i-149, 3, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(169, 173):
                self.tile = Tile(self, i-154, 2, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(173, 179):
                self.tile = Tile(self, i-159, 1, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(179, 186):
                self.tile = Tile(self, i-174, 1, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(186, 197):
                self.tile = Tile(self, i-185, 2, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(197, 208, 2):
                self.tile = Tile(self, i-196, 3, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(208, 218, 2):
                self.tile = Tile(self, i-206, 4, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(218, 225):
                self.tile = Tile(self, i-215, 5, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(225, 235):
                self.tile = Tile(self, i-224, 6, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(235, 245, 2):
                self.tile = Tile(self, i-234, 7, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()
            elif i in range(245, 255, 2):
                self.tile = Tile(self, i-243, 8, 2, i, random.choice(self.tile_type_count), False)
                self.tile_coordinates.append((self.tile.x, self.tile.y, self.tile.z))
                self.load_images()

    def load_images(self):
        """Loads an image from the sheet for every drawn tile according to the tile type."""
        if self.tile.tile_type == 1 and self.tile.z == 2:
            self.tile.image.blit(BARU, (-1, -1, -2, -1))
            self.tile_type_count.remove(1)
        elif self.tile.tile_type == 1 and self.tile.z == 1:
            self.tile.image.blit(BARU2, (-1, -1, -2, -1))
            self.tile_type_count.remove(1)
        elif self.tile.tile_type == 2 and self.tile.z == 2:
            self.tile.image.blit(INDRA, (-1, -1, -2, -1))
            self.tile_type_count.remove(2)
        elif self.tile.tile_type == 2 and self.tile.z == 1:
            self.tile.image.blit(INDRA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(2)
        elif self.tile.tile_type == 3 and self.tile.z == 2:
            self.tile.image.blit(ITACHI, (-1, -1, -2, -1))
            self.tile_type_count.remove(3)
        elif self.tile.tile_type == 3 and self.tile.z == 1:
            self.tile.image.blit(ITACHI2, (-1, -1, -2, -1))
            self.tile_type_count.remove(3)
        elif self.tile.tile_type == 4 and self.tile.z == 2:
            self.tile.image.blit(IZUNA, (-1, -1, -2, -1))
            self.tile_type_count.remove(4)
        elif self.tile.tile_type == 4 and self.tile.z == 1:
            self.tile.image.blit(IZUNA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(4)
        elif self.tile.tile_type == 5 and self.tile.z == 2:
            self.tile.image.blit(MADARA, (-1, -1, -2, -1))
            self.tile_type_count.remove(5)
        elif self.tile.tile_type == 5 and self.tile.z == 1:
            self.tile.image.blit(MADARA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(5)
        elif self.tile.tile_type == 6 and self.tile.z == 2:
            self.tile.image.blit(NAKA, (-1, -1, -2, -1))
            self.tile_type_count.remove(6)
        elif self.tile.tile_type == 6 and self.tile.z == 1:
            self.tile.image.blit(NAKA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(6)
        elif self.tile.tile_type == 7 and self.tile.z == 2:
            self.tile.image.blit(NAORI, (-1, -1, -2, -1))
            self.tile_type_count.remove(7)
        elif self.tile.tile_type == 7 and self.tile.z == 1:
            self.tile.image.blit(NAORI2, (-1, -1, -2, -1))
            self.tile_type_count.remove(7)
        elif self.tile.tile_type == 8 and self.tile.z == 2:
            self.tile.image.blit(OBITO, (-1, -1, -2, -1))
            self.tile_type_count.remove(8)
        elif self.tile.tile_type == 8 and self.tile.z == 1:
            self.tile.image.blit(OBITO2, (-1, -1, -2, -1))
            self.tile_type_count.remove(8)
        elif self.tile.tile_type == 9 and self.tile.z == 2:
            self.tile.image.blit(RAI, (-1, -1, -2, -1))
            self.tile_type_count.remove(9)
        elif self.tile.tile_type == 9 and self.tile.z == 1:
            self.tile.image.blit(RAI2, (-1, -1, -2, -1))
            self.tile_type_count.remove(9)
        elif self.tile.tile_type == 10 and self.tile.z == 2:
            self.tile.image.blit(SASUKE, (-1, -1, -2, -1))
            self.tile_type_count.remove(10)
        elif self.tile.tile_type == 10 and self.tile.z == 1:
            self.tile.image.blit(SASUKE2, (-1, -1, -2, -1))
            self.tile_type_count.remove(10)
        elif self.tile.tile_type == 11 and self.tile.z == 2:
            self.tile.image.blit(SHIN, (-1, -1, -2, -1))
            self.tile_type_count.remove(11)
        elif self.tile.tile_type == 11 and self.tile.z == 1:
            self.tile.image.blit(SHIN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(11)
        elif self.tile.tile_type == 12 and self.tile.z == 2:
            self.tile.image.blit(SHISUI, (-1, -1, -2, -1))
            self.tile_type_count.remove(12)
        elif self.tile.tile_type == 12 and self.tile.z == 1:
            self.tile.image.blit(SHISUI2, (-1, -1, -2, -1))
            self.tile_type_count.remove(12)
        elif self.tile.tile_type == 13 and self.tile.z == 2:
            self.tile.image.blit(FUGAKU, (-1, -1, -2, -1))
            self.tile_type_count.remove(13)
        elif self.tile.tile_type == 13 and self.tile.z == 1:
            self.tile.image.blit(FUGAKU2, (-1, -1, -2, -1))
            self.tile_type_count.remove(13)
        elif self.tile.tile_type == 14 and self.tile.z == 2:
            self.tile.image.blit(SASUKE_RINNEGAN, (-1, -1, -2, -1))
            self.tile_type_count.remove(14)
        elif self.tile.tile_type == 14 and self.tile.z == 1:
            self.tile.image.blit(SASUKE_RINNEGAN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(14)
        elif self.tile.tile_type == 15 and self.tile.z == 2:
            self.tile.image.blit(RINNEGAN, (-1, -1, -2, -1))
            self.tile_type_count.remove(15)
        elif self.tile.tile_type == 15 and self.tile.z == 1:
            self.tile.image.blit(RINNEGAN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(15)
        elif self.tile.tile_type == 16 and self.tile.z == 2:
            self.tile.image.blit(BYAKUGAN, (-1, -1, -2, -1))
            self.tile_type_count.remove(16)
        elif self.tile.tile_type == 16 and self.tile.z == 1:
            self.tile.image.blit(BYAKUGAN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(16)
        elif self.tile.tile_type == 17 and self.tile.z == 2:
            self.tile.image.blit(TENSEIGAN, (-1, -1, -2, -1))
            self.tile_type_count.remove(17)
        elif self.tile.tile_type == 17 and self.tile.z == 1:
            self.tile.image.blit(TENSEIGAN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(17)
        elif self.tile.tile_type == 18 and self.tile.z == 2:
            self.tile.image.blit(SENNIN_KYUUBI, (-1, -1, -2, -1))
            self.tile_type_count.remove(18)
        elif self.tile.tile_type == 18 and self.tile.z == 1:
            self.tile.image.blit(SENNIN_KYUUBI2, (-1, -1, -2, -1))
            self.tile_type_count.remove(18)
        elif self.tile.tile_type == 19 and self.tile.z == 2:
            self.tile.image.blit(SHARINGAN, (-1, -1, -2, -1))
            self.tile_type_count.remove(19)
        elif self.tile.tile_type == 19 and self.tile.z == 1:
            self.tile.image.blit(SHARINGAN2, (-1, -1, -2, -1))
            self.tile_type_count.remove(19)
        elif self.tile.tile_type == 20 and self.tile.z == 2:
            self.tile.image.blit(DOUBLE_TOMOE, (-1, -1, -2, -1))
            self.tile_type_count.remove(20)
        elif self.tile.tile_type == 20 and self.tile.z == 1:
            self.tile.image.blit(DOUBLE_TOMOE2, (-1, -1, -2, -1))
            self.tile_type_count.remove(20)
        elif self.tile.tile_type == 21 and self.tile.z == 2:
            self.tile.image.blit(SARADA, (-1, -1, -2, -1))
            self.tile_type_count.remove(21)
        elif self.tile.tile_type == 21 and self.tile.z == 1:
            self.tile.image.blit(SARADA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(21)
        elif self.tile.tile_type == 22 and self.tile.z == 2:
            self.tile.image.blit(MIKOTO, (-1, -1, -2, -1))
            self.tile_type_count.remove(22)
        elif self.tile.tile_type == 22 and self.tile.z == 1:
            self.tile.image.blit(MIKOTO2, (-1, -1, -2, -1))
            self.tile_type_count.remove(22)
        elif self.tile.tile_type == 23 and self.tile.z == 2:
            self.tile.image.blit(NOEL, (-1, -1, -2, -1))
            self.tile_type_count.remove(23)
        elif self.tile.tile_type == 23 and self.tile.z == 1:
            self.tile.image.blit(NOEL2, (-1, -1, -2, -1))
            self.tile_type_count.remove(23)
        elif self.tile.tile_type == 24 and self.tile.z == 2:
            self.tile.image.blit(ENLIGHTENED, (-1, -1, -2, -1))
            self.tile_type_count.remove(24)
        elif self.tile.tile_type == 24 and self.tile.z == 1:
            self.tile.image.blit(ENLIGHTENED2, (-1, -1, -2, -1))
            self.tile_type_count.remove(24)
        elif self.tile.tile_type == 25 and self.tile.z == 2:
            self.tile.image.blit(TRIRISE, (-1, -1, -2, -1))
            self.tile_type_count.remove(25)
        elif self.tile.tile_type == 25 and self.tile.z == 1:
            self.tile.image.blit(TRIRISE2, (-1, -1, -2, -1))
            self.tile_type_count.remove(25)
        elif self.tile.tile_type == 26 and self.tile.z == 2:
            self.tile.image.blit(NOVA, (-1, -1, -2, -1))
            self.tile_type_count.remove(26)
        elif self.tile.tile_type == 26 and self.tile.z == 1:
            self.tile.image.blit(NOVA2, (-1, -1, -2, -1))
            self.tile_type_count.remove(26)
        elif self.tile.tile_type == 27 and self.tile.z == 2:
            self.tile.image.blit(DEMON, (-1, -1, -2, -1))
            self.tile_type_count.remove(27)
        elif self.tile.tile_type == 27 and self.tile.z == 1:
            self.tile.image.blit(DEMON2, (-1, -1, -2, -1))
            self.tile_type_count.remove(27)

    def run(self):
        """The main loop tha runs the game, while conditions are met, otherwise exits the game."""
        while self.running:
            self.free_pairs_func()
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Checks and waits for an event in the game to happen."""
        for event in pg.event.get():
            # Checks if the player exits the game.
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.quit()

            # If you press the left mouse button and the game is not paused, if it collides with tile coordinates checks
            # if the tile is free. If its free adds it to a group of sprites. When there are 2 sprites in that group
            # it compares their type and if they are the same - removes them from the game and adds points to the score.
            # Otherwise draws a red rectangle and deselects the tile, clears the sprite group and the other lists, and
            # finally it waits for a new tile to collide with the mouse coordinates and repeats the whole process again.

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not self.pause:
                for self.tile in self.all_sprites:
                    if self.tile.rect.collidepoint(event.pos):
                        if self.tile.tile_id not in self.tile_id_list:
                            if (self.tile.x-1, self.tile.y, self.tile.z) in self.tile_coordinates and \
                                    (self.tile.x+1, self.tile.y, self.tile.z) in self.tile_coordinates:
                                print("tile is blocked")
                                pg.draw.rect(screen, (255, 0, 0), self.tile.rect)
                                self.mouse_collide.remove(self.tile)
                            else:
                                if (self.tile.x, self.tile.y, self.tile.z) in self.tile_coordinates and \
                                        (self.tile.x, self.tile.y, self.tile.z+1) not in self.tile_coordinates:

                                    self.tile_xy_list.append((self.tile.x, self.tile.y, self.tile.z))
                                    self.mouse_collide.add(self.tile)
                                    self.tile_id_list.append(self.tile.tile_id)
                                    self.tiles_compare_list.append(self.tile)
                                    print("appending from layer ", self.tile.z)
                                    self.tile.selected = True
                                else:
                                    self.mouse_collide.remove(self.tile)
                                if len(self.tiles_compare_list) < 2:
                                    pass
                                else:
                                    if self.tiles_compare_list[0].tile_type == self.tiles_compare_list[1].tile_type:
                                        for sprite in self.mouse_collide:
                                            sprite.kill()
                                        for i in self.tile_xy_list:
                                            if i in self.tile_coordinates:
                                                self.tile_coordinates.remove(i)
                                        self.tile.selected = False
                                        self.free_pairs_func()
                                        self.tile_xy_list.clear()
                                        self.mouse_collide.remove(self.tile)
                                        self.tile_id_list.clear()
                                        self.tiles_compare_list.clear()
                                        self.score += 1000 + self.bonus_points
                                        self.bonus_points = 2250
                                        print("tiles matched and deleted")
                                    else:
                                        for sprite in self.mouse_collide:
                                            pg.draw.rect(screen, (255, 0, 0), self.tile.rect)
                                            self.mouse_collide.remove(sprite)
                                        self.tile_id_list.clear()
                                        self.tiles_compare_list.clear()
                                        self.tile_xy_list.clear()
                                        print("tiles didn't match. pick another two.")

            # Every 5 seconds it triggers a time event that moves specific tiles on the screen back and forth (if the
            # tiles still exist), adding some dynamics and complexity to the game.
            elif event.type == self.time_event and not self.pause:
                if self.movement_controller:
                    for self.tile in self.all_sprites:
                        if self.tile.tile_id == 28:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 30:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 34:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 36:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 38:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 3
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 39:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 41:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 45:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 47:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 66:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 68:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 72:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 74:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 76:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 78:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 82:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 84:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 197:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 199:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 203:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 205:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 207:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 3
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 208:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 210:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 214:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 216:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 235:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 237:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 241:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 243:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 245:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 247:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 251:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 253:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))

                    for self.tile in self.mouse_collide:
                        if self.tile.selected:
                            if (self.tile.x-1, self.tile.y, self.tile.z) in self.tile_coordinates and \
                                    (self.tile.x+1, self.tile.y, self.tile.z) in self.tile_coordinates:
                                self.tile.selected = False
                                self.mouse_collide.remove(self.tile)
                                self.tile_xy_list.clear()
                                self.tile_id_list.clear()
                                self.tiles_compare_list.clear()
                    self.movement_controller = False
                else:
                    for self.tile in self.all_sprites:
                        if self.tile.tile_id == 28:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 30:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 34:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 36:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 38:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 3
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 39:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 41:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 45:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 47:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 66:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 68:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 72:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 74:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 76:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 78:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 82:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 84:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 197:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 199:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 203:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 205:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 207:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 3
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 208:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 210:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 214:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 216:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 235:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 237:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 241:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 243:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 245:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 247:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x -= 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 251:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 1
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                        if self.tile.tile_id == 253:
                            if self.tile.alive():
                                self.tile_coordinates.remove((self.tile.x, self.tile.y, self.tile.z))
                                self.tile.x += 2
                                self.tile_coordinates.insert(0, (self.tile.x, self.tile.y, self.tile.z))
                    self.movement_controller = True

            # Checks if the player pauses the game. If so loads the pause image and pauses the game until resumed or
            # the player exits the game.
            elif event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.pause = not self.pause
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN and event.key == pg.K_p:
                        self.pause = False
                    elif event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        self.quit()

            # Checks if the player presses the info button. If so displays info about the game and pauses the game
            # until resumed or the player exits the game.
            elif event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.pause = not self.pause
                self.info = not self.info
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN and event.key == pg.K_i:
                        self.info = False
                        self.pause = False
                    elif event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                        self.quit()

            # Checks if the player mutes the music. If the music stops playing and unloads the file to save resources.
            # The music can be played again if the player presses the button again.
            elif event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.music = not self.music
                if self.music:
                    pg.mixer.music.load("bg_music.mp3")
                    pg.mixer.music.set_volume(0.4)
                    pg.mixer.music.play(-1, 0.1, 2)
                else:
                    pg.mixer.music.stop()
                    pg.mixer.music.unload()

            # Checks if there are free pairs left in the game. Game ends when there are no more free pairs.
            # Score is then calculated and written in a highscores file.
            elif self.free_pairs == 0 and len(self.all_sprites) > 0 or len(self.all_sprites) == 0:
                self.calc_highscore()

    def update(self):
        """Constantly updates the game with 40 FPS until the main loop ends."""
        pg.display.update()
        self.all_sprites.update()

    def draw(self):
        """Draws various texts(like score, free pairs, bonus points), background image and the tiles on the screen."""
        screen.blit(BG_IMAGE, (0, 0))
        self.all_sprites.draw(screen)
        draw_text(screen, "Free Pairs: "+str(self.free_pairs), 32, 120, 20)
        draw_text(screen, "Score: " + str(self.score), 32, WIDTH-210, 20)

        # Calculates the bonus points and draws the number on the screen. For every tick
        # the bonus points are reduced by 5 until they reach 0. Then you get no bonus points to the score.
        if pg.time.get_ticks() and not self.pause:
            self.bonus_points -= 5
            if self.bonus_points <= 0:
                self.bonus_points = 0
        draw_text(screen, "Bonus Points: " + str(self.bonus_points), 32, WIDTH/2, 20)

        # If the game is paused - draws the pause image and text, that shows the player the game is paused.
        if self.pause and not self.info:
            screen.blit(PAUSE_IMAGE, (0, 0))
            draw_text(screen, "GAME IS PAUSED", 32, WIDTH/2, 20)

        # Draws information about the game if the player presses the information button.
        if self.info:
            screen.fill((0, 0, 0))
            draw_text(screen, "Press I for information.", 32, 245, 50)
            draw_text(screen, "Press P for pause.", 32, 200, 100)
            draw_text(screen, "Press Escape to quit the game.", 32, 295, 150)
            draw_text(screen, "Press M to mute/unmute the music.", 32, 332, 200)
            draw_text(screen, "There are 2 layers of tiles - white and green.", 32, 400, 300)
            draw_text(screen, "Match two equal tiles that are free to score points.", 32, 450, 350)
            draw_text(screen, "Free tiles are those, which don't have tile on the left,"
                      " right or above.", 32, 583, 400)
            draw_text(screen, "The colors are only to help you better see the layers.", 32, 463, 450)
            draw_text(screen, "You can match tiles of different color if the images are the same.", 32, 560, 500)
            draw_text(screen, "You get bonus points for matching the tiles faster.", 32, 450, 550)
            draw_text(screen, "GL & HF!", 32, screen.get_width() / 2, screen.get_height() - 150)
            draw_text(screen, "Created by: BateDa4ko", 32, screen.get_width() / 2,
                      screen.get_height() - 100)

        # If there are no free pairs left - draws the player name and score to the screen. Reads the highscores file
        # and draws top 15 player names and scores and the current player position.
        if len(self.all_sprites) == 0:
            screen.fill((0, 0, 0))
            draw_text(screen, "You won!", 32, window.desktop.width()/ 2 + 90, window.desktop.height() / 4)
            draw_text(screen, window.get_nickname(), 32, window.desktop.width() / 2 + 90,
                      window.desktop.height() / 4 + 40)
            draw_text(screen, str(self.score), 32, window.desktop.width() / 2 + 90,
                      window.desktop.height() / 4 + 80)
            self.read_highscore()

        if self.free_pairs == 0 and len(self.all_sprites) > 0:
            screen.fill((0, 0, 0))
            draw_text(screen, "No free pairs left!", 32, window.desktop.width() / 2 + 90,
                      window.desktop.height() / 4)
            draw_text(screen, window.get_nickname(), 32, window.desktop.width() / 2 + 90,
                      window.desktop.height() / 4 + 40)
            draw_text(screen, str(self.score), 32, window.desktop.width() / 2 + 90,
                      window.desktop.height() / 4 + 80)
            self.read_highscore()

        # If a tile is selected - draws a green rectangle around it, so the player visualize that the tile is selected.
        for self.tile in self.mouse_collide:
            if self.tile.selected and not self.pause:
                screen.blit(BORDER_IMAGE, self.tile.rect)
        pg.display.flip()

    def free_pairs_func(self):
        """ Calculates the free pairs that are left in the game.
        Draws the number at the top left corner, so the player see exactly how much free pairs are left."""
        self.temp_tiles = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                           15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0}
        self.free_pairs = 0
        for self.tile in self.all_sprites:
            if (self.tile.x-1, self.tile.y, self.tile.z) not in self.tile_coordinates or \
               (self.tile.x+1, self.tile.y, self.tile.z) not in self.tile_coordinates:
                if (self.tile.x, self.tile.y, self.tile.z) in self.tile_coordinates and \
                        (self.tile.x, self.tile.y, self.tile.z+1) not in self.tile_coordinates:
                    self.temp_tiles[self.tile.tile_type] += 1

        for v in self.temp_tiles.values():
            self.free_pairs = self.free_pairs + int(v/2)
        return self.free_pairs

    def calc_highscore(self):
        """Reads a csv file with the players highscores. If the players current score is lower it displays his previous
        best score. If the score is higher than the score in the csv file it overwrites it and sets a new highscore.
        If the player name is not in the file it appends it with his first score. Then sorts all the highscores in
        descending(highest score is on top) order and writes the new highscores file."""
        rows = []
        hs_row = [window.get_nickname(), self.score]
        with open("highscores.csv", "r", newline="", encoding="utf-8") as g:
            reader = csv.reader(g)
            for row in reader:
                rows.append(row)
                if row[0] == "name" and row[1] == "score":
                    pass
                else:
                    if row[0] == window.get_nickname() and int(row[1]) < self.score:
                        if row[0] == "name" and row[1] == "score":
                            rows.remove(row)
                        rows.remove(row)
                        rows.append(hs_row)
                        with open("highscores.csv", "w", newline="", encoding="utf-8") as f:
                            writer = csv.writer(f, delimiter=",")
                            writer.writerows(rows)

                    elif row[0] == window.get_nickname() and int(row[1]) > self.score:
                        break
                        if row[0] == "name" and row[1] == "score":
                            rows.remove(row)
                        rows.remove(hs_row)
                        with open("highscores.csv", "w", newline="", encoding="utf-8") as f2:
                            writer = csv.writer(f2, delimiter=",")
                            writer.writerow(rows)

                    elif row[0] != window.get_nickname():
                        with open("highscores.csv", "a", newline="", encoding="utf-8") as f3:
                            writer = csv.writer(f3, delimiter=",")
                            writer.writerow(hs_row)

        df = pd.read_csv("highscores.csv", sep=",")
        df.drop_duplicates(subset=None, inplace=True)
        df.sort_values(by=["score"], inplace=True, ascending=False)
        df.to_csv("highscores.csv", index=False)

    def read_highscore(self):
        """Reads the highscores csv file and draws the player names and scores on the screen. If the current player
        position is higher than 15 (16+ position) it draws it on the bottom."""
        with open("highscores.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    draw_text(screen, "Top 15 Scores", 32,
                              window.desktop.width()//4-180, window.desktop.height()//16-40)
                else:
                    if i < 16:
                        draw_text(screen, str(i), 32,
                                  window.desktop.width()//4-400, window.desktop.height()//16+i*40)
                        draw_text(screen, row[0], 32,
                                  window.desktop.width()//4-200, window.desktop.height()//16+i*40)
                        draw_text(screen, str(row[1]), 32,
                                  window.desktop.width()//4+120, window.desktop.height()//16+i*40)
                        if window.get_nickname() == row[0]:
                            draw_text(screen, "<=", 32,
                                      window.desktop.width()//2-150, window.desktop.height()//16+i*40)
                    elif i >= 16 and window.get_nickname() == row[0]:
                        draw_text(screen, str(i), 32,
                                  window.desktop.width()//4-400, window.desktop.height()//16+17*40)
                        draw_text(screen, row[0], 32,
                                  window.desktop.width()//4-200, window.desktop.height()//16+17*40)
                        draw_text(screen, str(row[1]), 32,
                                  window.desktop.width()//4+120, window.desktop.height()//16+17*40)

    def quit(self):
        """Exits the game."""
        pg.quit()
        sys.exit()


class HighScores(QWidget):
    """Utility class that displays the pre-game screen, where you see the game rules and enter a nickname."""
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(QSize(self.desktop.width()//2, self.desktop.height()//2))
        self.setWindowTitle("Game Instructions")
        self.display_widgets()
        self.show()

    def display_widgets(self):
        """Displays the game rules, prompts the player to enter a nickname."""
        self.info_label = QLabel(self)
        self.info_label.move(self.desktop.width()//18, self.desktop.height()//16)
        self.info_label.setFont(QFont("Arial", 15))
        self.info_label.setText("Press I for information.\nPress P for pause.\nPress Escape to quit the game.\nPress M"
                                " to mute/unmute the music.\n\n"
                                "There are 2 layers of tiles, white and green. Match two equal tiles that are free to\n"
                                "score points. Free tiles are those, which don't have tile on the left, right or "
                                "above.\nThe colors are only to help you better see the layers(you can match tiles of "
                                "different\ncolor if the images are the same). You get bonus points for matching "
                                "the tiles faster.\n\nEnter a nickname and press the Play to start. GL & HF!")
        self.info_label.show()

        self.nickname = QLineEdit(self)
        self.nickname.move(self.desktop.width()//4-100, self.desktop.height()//2-100)
        self.nickname.resize(200, 30)
        self.nickname.setFont(QFont("Arial", 14))
        self.nickname.show()

        self.play_button = QPushButton("Play", self)
        self.play_button.move(self.desktop.width()//4-70, self.desktop.height()//2-50)
        self.play_button.resize(140, 30)
        self.play_button.setFont(QFont("Arial", 14))
        self.play_button.clicked.connect(self.click_play)

    def click_play(self):
        """Starts the game loop if the Play button is pressed."""
        self.close()
        g = Game()
        while True:
            g.new()
            g.run()

    def get_nickname(self):
        """Gets the player's nickname for later purposes."""
        self.player_nickname = self.nickname.text()
        if self.player_nickname == "":
            self.player_nickname = "Guest"
            return self.player_nickname
        else:
            return self.player_nickname.title().strip()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HighScores()
    sys.exit(app.exec_())

