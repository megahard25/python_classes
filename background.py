import pygame
import pygame.locals
import sys
import os

import config

# import window
class Background(object):
    def __init__(self, background, DSS, speed = 0):
        self.background = background
        self.x_coordinate = 0
        self.speed = speed
        self.DSS = DSS

    def draw_static_background(self):
        slef.speed = 0
        pass

    def draw_dynamic_background(self):
        rel_x = self.x_coordinate % (self.background).get_rect().width
        (self.DSS).blit((self.background), (rel_x - (self.background).get_rect().width, 0))
        if rel_x < config.window_width:
            (self.DSS).blit((self.background), (rel_x, 0))
        self.x_coordinate -= self.speed
