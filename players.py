import pygame
from pygame.locals import *
import math
import random
import sys

import config
import window

# Класс родитель(наследует участников: главный герой, враги, пули)
class Ship(object):
    def __init__(self, HP, x, y,
                 speed_x, speed_y,
                 sprites, sprites_death, damage):
        self.HP = HP
        self.x = 0
        self.y = 0
        self.set_coord(x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.sprites = sprites
        self.sprites_death = sprites_death
        self.damage = damage
        self.anim_count = 0
        self.anim_count_death = 0

    # Жив ли участник
    def is_alive(self):
        if self.HP >= 0:
            return True
        elif self.anim_count_death // config.frames_update < len(self.sprites_death):
            return True
        else:
            return False

    # Получить спрайты участника
    def get_sprite(self):
        self.anim_count += 1
        return self.sprites[(self.anim_count // config.frames_update) % len(self.sprites)]

    # Получить спрайты уничтожения участника
    def get_sprite_death(self):
        self.anim_count_death += 1
        return self.sprites_death[((self.anim_count_death - 1) // config.frames_update) % len(self.sprites_death)]

    # Геттер координат
    def get_coord(self):
        return self.x, self.y

    # Сеттер координат
    def set_coord(self, x, y):
        if ((x < config.window_width - config.image_size and x > 0) and
           (y < config.window_high - config.image_size and y > 0)):
            self.x = x
            self.y = y
        else:
            print('bad coords!')

    # Обновление координат - движение
    def new_coord(self):
        pass

    # Отрисовка
    def draw(self):
        if self.HP >= 0:
            window.screen.blit(self.get_sprite(), (self.x, self.y))
        else:
            window.screen.blit(self.get_sprite_death(), (self.x, self.y))

    # Получение урона
    def on_damage(self, d):
        if self.HP >= 0:
            self.HP -= d

    def get_damage(self):
        return self.damage

    def fire(self):
        pass

# Ребёнок класса Ship - пули врагов и героя
class Bullet(Ship):
    def __init__(self, x, y, speed_x,
                 sprites, sprites_death,
                 damage, direction):
        HP = 0
        speed_y = 0
        Ship.__init__(self, HP, x, y,
                      speed_x, speed_y,
                      sprites, sprites_death, damage)
        self.direction = direction

    def set_coord(self, x, y):
        if ((x < config.window_width - config.image_size and x > 0) and
           (y < config.window_high - config.image_size and y > config.image_size)):
            self.x = x
            self.y = y
        else:
            self.on_damage(1)

    def new_coord(self):
        new_x = self.x + self.direction*self.speed_x
        new_y = self.y
        self.set_coord(new_x, new_y)

# Ребёнок класса Ship - герой игры
class Hero(Ship):

    def new_coord(self, keys):
        new_x = new_y = 0
        if keys[pygame.K_LEFT]:
            new_x = self.x - self.speed_x*1
        if keys[pygame.K_RIGHT]:
            new_x = self.x + self.speed_x*1
        if keys[pygame.K_UP]:
            new_y = self.y - self.speed_y*1
        if keys[pygame.K_DOWN]:
            new_y = self.y + self.speed_y*1
        if new_x == 0:
            new_x = self.x
        if new_y == 0:
            new_y = self.y
        self.set_coord(new_x, new_y)

    # Реализация выстрелов
    def fire(self, keys):
        if keys[pygame.K_SPACE] and self.anim_count % config.hero_frames_per_bullet == 0:
            return  Bullet(self.x + 6, self.y, config.bullet_speed,
                           config.bullet_sprites, config.sprites_death,
                           config.hero_bullet_damage, config.move_right)

# Ребёнок класса Ship - враги
class Enemy(Ship):
    def __init__(self, HP = config.enemy_start_HP, x = 800, y = 0,
                    speed_x = config.enemy_speed,
                    speed_y = config.enemy_speed,
                    sprites = config.fast_ship_sprites,
                    sprites_death = config.sprites_death,
                    damage = config.enemy_taran_damage,
                    amplitude = config.enemy_trajectory_amplitude,
                    phase = config.enemy_trajectory_phase,
                    frequency = config.enemy_trajectory_frequency):
        if y == 0:
            y = random.randrange(config.enemy_random_y,
                                 config.window_high - config.enemy_random_y,
                                 config.enemy_delt_coord)
        if speed_x == 0:
            speed_x = 0
        if speed_y == 0:
            speed_y = 0
        Ship.__init__(self, HP, x, y,
                      speed_x, speed_y, sprites,
                      sprites_death, damage)
        if amplitude == 0:
            amplitude = min((self.y), (800 - self.y))
        if phase == 0:
            phase = random.randrange(0, 6, 1)
        if frequency == 0:
            frequency = random.random()*0.01
        self.phase = phase
        self.frequency = frequency
        self.amplitude = amplitude
        self.start_x = x
        self.start_y = y

    def set_coord(self, x, y):
        if ((x < config.window_width - config.image_size and x > 0) and
           (y < config.window_high - config.image_size and y > config.image_size)):
            self.x = x
            self.y = y
        else:
            self.on_damage(self.HP+1)

    def new_coord(self):
        new_x = self.x - self.speed_x*1
        new_y = self.amplitude*math.sin((self.frequency*self.x + self.phase)/2)*math.sin(self.frequency*self.x + self.phase) + self.start_y
        self.set_coord(new_x, new_y)

    def fire(self):
        if self.anim_count % config.enemy_frames_per_bullet == 0:
            return Bullet(self.x - config.enemy_bullet_indent,
                          self.y,
                          config.bullet_speed,
                          config.bullet_sprites,
                          config.sprites_death,
                          config.enemy_taran_damage,
                          config.move_left)

# Фабрика участников
class Ships_Factory(object):
    def __init__(self):
        self.list = []

    def add(self, s: Ship):
        if s is not None:
            self.list.append(s)

    def get(self, index):
        return self.list[index]

    def remove(self, index):
        self.list.remove(index)

    def get_list(self):
        return self.list

    def draw(self):
        for each in self.list:
            each.draw()

    def new_coord(self):
        for each in self.list:
            if each.is_alive():
                each.new_coord()
            else:
                self.list.remove(each)

# Игровой класс- создание классов участников, отприсовка, движение
class Game(object):
    def __init__(self):
        self.player = Hero(config.hero_start_HP,
                           config.hero_start_x,
                           config.hero_start_y,
                           config.hero_speed,
                           config.hero_speed,
                           config.player_sprites,
                           config.sprites_death,
                           config.hero_taran_damage)
        self.Enemy_Factory = Ships_Factory()
        self.Enemy_Factory.add(Enemy())
        self.Enemy_Factory.add(Enemy())
        self.Enemy_Factory.add(Enemy())
        self.bullets = Ships_Factory()

    def draw(self):
        self.player.draw()
        self.Enemy_Factory.draw()
        self.bullets.draw()

    def new_coord(self, keys):
        if self.player.is_alive():
            self.player.new_coord(keys)
        else:
            print('End game!!!')
            sys.exit()
        self.Enemy_Factory.new_coord()
        self.bullets.new_coord()

    def tick(self, keys):
        self.draw()
        self.new_coord(keys)
        self.bullets.add(self.player.fire(keys))
        for each in self.Enemy_Factory.get_list():
            self.bullets.add(each.fire())
        for each in self.Enemy_Factory.get_list():
            self.collide(self.player, each)
        for each in self.bullets.get_list():
            self.collide(self.player, each)
        for each1 in self.Enemy_Factory.get_list():
            for each2 in self.bullets.get_list():
                self.collide(each1, each2)

    # Проверка столкновений
    def collide(self, A: Ship, B: Ship):
        x_A, y_A = A.get_coord()
        x_B, y_B = B.get_coord()
        if math.sqrt((x_A - x_B)**2 + (y_A -y_B)**2) < config.impact_parameter:
            A.on_damage(B.get_damage())
            B.on_damage(A.get_damage())
