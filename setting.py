import pygame
import heroes
from walls_fons import Fons
from platform import PlatformX, PlatformY

# размер окна
size = W, H = 1000, 500

# рамки
rx = 10
ry = 5

# выбор персонажа: определяется у двух игроков
heroes_all = [heroes.Reptile, heroes.Scorpion, heroes.SubZero, heroes.Smoke,
              heroes.KungLao]

gamer_1 = heroes.MainHero()
gamer_2 = heroes.MainHero(2)

# окна
window_num = 0  # 0 - выбор персонажа
# 1 - игра

# выбор персонажа
# счётчик анимации фона
choose_heroes_fons_aC = 0
choose_heroes_fons_anim = [pygame.image.load('choose_heroes/fon/0.png'),
                           pygame.image.load('choose_heroes/fon/1.png'),
                           pygame.image.load('choose_heroes/fon/2.png'),
                           pygame.image.load('choose_heroes/fon/3.png'),
                           pygame.image.load('choose_heroes/fon/4.png'),
                           pygame.image.load('choose_heroes/fon/5.png'),
                           pygame.image.load('choose_heroes/fon/6.png'),
                           pygame.image.load('choose_heroes/fon/7.png')]
choose_heroes_fons_anim = [pygame.transform.scale(i, (W, H)) for i in choose_heroes_fons_anim]

choose_heroes_right_heroes = [pygame.image.load('heroes/Scorpion/scorpion.png'),
                              pygame.image.load('heroes/Sub_Zero/subzero.png'),
                              pygame.image.load('heroes/Reptile/reptile.png'),
                              pygame.image.load('heroes/Smoke/smoke.png'),
                              pygame.image.load('heroes/Kung_Lao/kunglao.png')]
choose_heroes_right_heroes_x = 5
choose_heroes_right_heroes_y = 5

# время
fps = 90

# ПЛАТФОРМЫ
platforms = pygame.sprite.Group()
platforms.add(PlatformX(-100, 495), PlatformY(0, -50), PlatformY(995, -50))

# ФОНЫ
fon = Fons(size)

# Группа всех спрайтов ВООБЩЕ всех
all_sprites = pygame.sprite.Group()
all_sprites.add(gamer_1)
all_sprites.add(gamer_2)
