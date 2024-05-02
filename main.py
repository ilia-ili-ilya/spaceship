import os

import pygame

from src.garage import Garage
from src.constants import *

if not os.path.isfile(RECORDS):
	open(RECORDS, 'w').close()
pygame.init()
g = Garage()
g.menu()
