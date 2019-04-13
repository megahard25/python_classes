import pygame
import pygame.locals
import sys
import os

# Принимает нажатия любых клавиш
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
