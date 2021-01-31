import pygame
import random
import heroes
# размер окна
W, H = 1000, 500

# рамки
rx = 10
ry = 5

# выбор персонажа: определяется у двух игроков
heroes_all = {
    0: heroes.Reptile(),
    1: heroes.Scorpion(),
    2: heroes.Sub_Zero(),
    3: heroes.Smoke(),
    4: heroes.Kung_Lao()
    # остальные
}
gamer_1 = heroes_all[1]
gamer_2 = heroes_all[4]

# print(heroes_all)
# gamer_1 = heroes_all[int(input('игрок справа:  '))]
# gamer_2 = heroes_all[int(input('игрок слева:   '))]
# gamer_1 = heroes_all[1]  # как-то по-другому обыграем
# gamer_2 = heroes_all[2]
num_iteration = 0
# окна
window_num = 0 # 0 - выбор персонажа
               # 1 - игра

# выбор персонажа
#счётчик анимации фона
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




# игра
# Игрок 1: размер персонажа/скорость и тп (надо додумать)
g1_w = gamer_1.width
g1_h = gamer_1.height

g1_speed = gamer_1.speed # скорость

g1_jump_speed = 10 # прыжок
g1_jump_coeff = g1_jump_speed
g1_in_jump = False

g1_stay_side = False         # если игрок повёрнут влево ==> стоит False
                             #                     вправо ==> стоит True
g1_move = False
# начальное положение в пространтсве
g1_x = W - 50 - g1_w - rx - g1_w
g1_y = H - g1_h - ry
# удары
g1_in_hit = False

g1_go = False


# Игрок 2: размер персонажа/скорость/движение и тп (надо додумать)
g2_w = gamer_2.width
g2_h = gamer_2.height

g2_speed = gamer_2.speed # скорость

g2_jump_speed = 10 # прыжок
g2_jump_coeff = g2_jump_speed
g2_in_jump = False

g2_stay_side = True          # если игрок повёрнут влево ==> стоит False
                             #                     вправо ==> стоит True
g2_move = False
# начальное положение в пространтсве
g2_x = 50 + g2_w + rx
g2_y = H - g2_h - ry
# удары
g2_in_hit = False

g2_go = False

# время
clock_ = 60
# условие работы основного цикла
run = True

# движение
aC = 0
aC1 = 0
g1_k_jump = gamer_1.k_jump
g2_k_jump = gamer_2.k_jump

# персонаж
g1_stand = True
g2_stand = True

all_sprites = pygame.sprite.Group()
all_sprites.add(gamer_1)
all_sprites.add(gamer_2)

# фон
fon1 = [pygame.image.load('fons/pygame_bg.jpg'),
    pygame.image.load('fons/pygame_bg_1.jpg'),
    pygame.image.load('fons/pygame_bg_2.jpg')]
fon = pygame.transform.scale(random.choice(fon1), (W, H))
fon_ = fon
# окно
pygame.init()
win = pygame.display.set_mode((W, H), pygame.RESIZABLE, pygame.SCALED)
pygame.display.set_caption('mk12')

# анимация
g1_kAn_x = 0
g1_kAn_y = 0
g1_anim = gamer_1.stand
g1_meter_jump = 0

g2_kAn_x = 0
g2_kAn_y = 0
g2_anim = gamer_2.stand
g2_meter_jump = 0



gamer_position = True # True - игрок 1 справа , игрок 2 слева
                      # False - игрок 2 справа , игрок 1 слева

g1_pause = False
g2_pause = False





