import pygame
import pygame.locals
import sys
import os
import math
import random
random.seed() # Иначе рандом начальных координат будет один и тот же для всех врагов

import background
import config
import window
import buttons
import players

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()

window.create_window()

# Создаём постоянные фоновых рисунков
city_back = (config.city).convert()
color_back = (config.sky).convert()
mist_back = (config.mist).convert_alpha(window.screen)

# background objects creation
city_background = background.Background(city_back,
                                        window.screen,
                                        config.level/4)
mist_background = background.Background(mist_back,
                                        window.screen,
                                        config.level/2)

game = players.Game()

# main loop
while True:
    # проверка всех нажатий
    buttons.events()

    # создаём динамичныйфон
    city_background.draw_dynamic_background()
    mist_background.draw_dynamic_background()

    # Отслеживание всех нажатых кнопок
    key_press = pygame.key.get_pressed()

    game.tick(key_press)

    pygame.display.update()
    CLOCK.tick(config.FPS)
