import pygame
from pygame.locals import *
import sys
import os

def events():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
# define display surface
image_size_x = 1120
image_size_y = 800

W, H = 1120, 800
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")
FPS = 120

current_path = os.path.dirname('/home/antony/python/MyGame/test/') # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path


walk = [pygame.image.load(os.path.join(image_path, 'spacecraft0.png')), pygame.image.load(os.path.join(image_path, 'spacecraft1.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft2.png')), pygame.image.load(os.path.join(image_path, 'spacecraft3.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft4.png')), pygame.image.load(os.path.join(image_path, 'spacecraft5.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft6.png')), pygame.image.load(os.path.join(image_path, 'spacecraft7.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft8.png')), pygame.image.load(os.path.join(image_path, 'spacecraft9.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft10.png')), pygame.image.load(os.path.join(image_path, 'spacecraft11.png')),
        pygame.image.load(os.path.join(image_path, 'spacecraft12.png')), pygame.image.load(os.path.join(image_path, 'spacecraft13.png'))]

city_back = pygame.image.load("resources/images/CityBackground.png").convert()
color_back = pygame.image.load("resources/images/red.png").convert()
mist_back = pygame.image.load("resources/images/fullfog.png").convert_alpha(DS)

x = 15
y = 600
width1 = 100
height = 96
speed = 6

animcount = 0

run= True

city_x = 0
mist_x = 0
# main loop
while run:
	events()
#    city_x = run_bkgd(city_x, DS.screen, background.city, config.window_width)

#	DS.blit(city_back, (city_x, 0))
#	DS.blit(color_back, (color_x, 0))
	city_rel_x = city_x % city_back.get_rect().width
	DS.blit(city_back, (city_rel_x - city_back.get_rect().width, 0))
	if city_rel_x < W:
		DS.blit(city_back, (city_rel_x, 0))
	city_x -= 0.5

	mist_rel_x = mist_x % mist_back.get_rect().width
	DS.blit(mist_back, (mist_rel_x - mist_back.get_rect().width, 0))
	if mist_rel_x < W:
		DS.blit(mist_back, (mist_rel_x, 0))
	mist_x -= 1
#	pygame.draw.line(DS, (255, 0, 0), (rel_x, 0), (rel_x, H), 3)
	if animcount + 1 >= 65: #по 5 кадров на изображение 5*7=35
		animcount = 0

	DS.blit(walk[animcount // 5], (x,y)) #деление на 5 и округление до меньшего
	animcount += 1

#	pygame.draw.rect(DS, (0,0,255), (x,y,width1,height)) #Рисуем игрока
	keys = pygame.key.get_pressed() #Отслеживание всех нажатых кнопок


	if keys[pygame.K_LEFT] and x > 5:
		x -= speed
	if keys[pygame.K_RIGHT] and x < 1080:
		x += speed
	if keys[pygame.K_UP] and y > 5:
		y -= speed
	if keys[pygame.K_DOWN] and y < 772:
		y += speed
#	elif keys[pygame.K_RIGHT] and x < (image_size_x - width1 - 5):
#		runing = True
#		x += speed
#	else:
#		runing = False
#		animcount = 0
#	if not(isJump):
#        if keys[pygame.K_UP] and y > 5:
#            y -= speed
#        if keys[pygame.K_DOWN] and y < 720 - height - 5:
#            y += speed
#		if keys[pygame.K_SPACE]:
#			isJump = True
#	else:
#		if jumpcount >= -10:
#			if jumpcount < 0:
#				y += (jumpcount ** 2) / 2
#			else:
#				y -= (jumpcount ** 2) / 2
#			jumpcount -= 1
#		else:
#			isJump = False
#			jumpcount = 10

	pygame.display.update()
	CLOCK.tick(FPS)
