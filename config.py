import os
import sys
import pygame

FPS = 120

# define display surface
window_width = 1120
window_high = 800
window_size = (window_width, window_high)
area = window_high*window_width


#Hero parametrs
hero_start_HP = 100
hero_start_x = 500
hero_start_y = 400
hero_speed = 5
hero_bullet_damage = 50
hero_taran_damage = 50
hero_frames_per_bullet = 20


#Enemy parametrs
enemy_frames_per_bullet = 40
enemy_speed = 0.5
enemy_random_y = 100 #Размер отступа от краёв экрана, где не сможетпоявляться враг
enemy_delt_coord = 100 #Расстояние между врагами при их создании
enemy_bullet_indent = 6 #Расстояние от координаты врага до координаты создания его патрона
enemy_trajectory_amplitude = 0 #характеристики траетрории врагов, 0 - если нужно случайное поведение
enemy_trajectory_phase = 0
enemy_trajectory_frequency = 0
enemy_taran_damage = 50
enemy_bullet_damage = 25
enemy_start_HP = 100

#Common parametrs
frames_update = 5
image_size = 15 #размер спрайта персонажей
move_right = 1
move_left = -1
impact_parameter = 5 #прицельный параметр - дельта на которой происходит столкновение
bullet_speed = 8



#background speed
level = 2

#paths
resource_path = os.path.abspath("resources") # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

#upload images and sprites
bullet_sprites = [pygame.image.load(os.path.join(image_path, 'bullet.png'))]

#спрайты взрыва участников
sprites_death = [pygame.image.load(os.path.join(image_path, 'boom0.png')), pygame.image.load(os.path.join(image_path, 'boom1.png')),
                pygame.image.load(os.path.join(image_path, 'boom2.png')), pygame.image.load(os.path.join(image_path, 'boom3.png')),
                pygame.image.load(os.path.join(image_path, 'boom4.png'))]

#главный герой
player_sprites = [pygame.image.load(os.path.join(image_path, 'spacecraft0.png')), pygame.image.load(os.path.join(image_path, 'spacecraft1.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft2.png')), pygame.image.load(os.path.join(image_path, 'spacecraft3.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft4.png')), pygame.image.load(os.path.join(image_path, 'spacecraft5.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft6.png')), pygame.image.load(os.path.join(image_path, 'spacecraft7.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft8.png')), pygame.image.load(os.path.join(image_path, 'spacecraft9.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft10.png')), pygame.image.load(os.path.join(image_path, 'spacecraft11.png')),
                pygame.image.load(os.path.join(image_path, 'spacecraft12.png')), pygame.image.load(os.path.join(image_path, 'spacecraft13.png'))]

#спрайты врагов быстрого типа
fast_ship_sprites = [pygame.image.load(os.path.join(image_path, 'enemy/fast_ship0.png')),
                    pygame.image.load(os.path.join(image_path, 'enemy/fast_ship1.png')),
                    pygame.image.load(os.path.join(image_path, 'enemy/fast_ship2.png'))]

#спрайты фона(красное небо, город, туман)
city = pygame.image.load(os.path.join(image_path, "CityBackground.png"))
sky = pygame.image.load(os.path.join(image_path, "red.png"))
mist = pygame.image.load(os.path.join(image_path, "fullfog.png"))
