import pygame
from pygame.locals import *
import sys
import os

#принимает нажатия любых клавиш
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
