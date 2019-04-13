import pygame
import pygame.locals
import sys
import os
import config

# Создание окна игры
screen = pygame.display.set_mode(config.window_size)
def create_window():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"
    pygame.display.set_caption("Game")
