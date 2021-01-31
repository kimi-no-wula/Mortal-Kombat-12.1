import pygame


GRAVITY = 0.2
MOVE_SPEED = 5
JUMP_POWER = 5
jump_coeff = 10
JUMP_BEAUTY_COEFF = 4


class MainHero(pygame.sprite.Sprite):
    def __init__(self, gamer_n=1):
        pygame.sprite.Sprite.__init__(self)
        self.on_ground = False
        self.jump = False

        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
        self.image = pygame.image.load('heroes/Reptile/go/0.png')
        self.go = [pygame.image.load('heroes/Reptile/go/0.png'),
                   pygame.image.load('heroes/Reptile/go/1.png'),
                   pygame.image.load('heroes/Reptile/go/2.png'),
                   pygame.image.load('heroes/Reptile/go/3.png'),
                   pygame.image.load('heroes/Reptile/go/4.png'),
                   pygame.image.load('heroes/Reptile/go/5.png'),
                   pygame.image.load('heroes/Reptile/go/6.png'),
                   pygame.image.load('heroes/Reptile/go/7.png'),
                   pygame.image.load('heroes/Reptile/go/8.png')]
        # self.go = [pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #              pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #              pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png')]

        self.jump = [pygame.image.load('heroes/Reptile/jump/0.png'),
                     pygame.image.load('heroes/Reptile/jump/1.png'),
                     pygame.image.load('heroes/Reptile/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Reptile/stand/0.png'),
                      pygame.image.load('heroes/Reptile/stand/1.png'),
                      pygame.image.load('heroes/Reptile/stand/2.png'),
                      pygame.image.load('heroes/Reptile/stand/3.png'),
                      pygame.image.load('heroes/Reptile/stand/4.png'),
                      pygame.image.load('heroes/Reptile/stand/5.png'),
                      pygame.image.load('heroes/Reptile/stand/6.png'),
                      pygame.image.load('heroes/Reptile/stand/7.png'),
                      pygame.image.load('heroes/Reptile/stand/8.png')]
        self.versus = pygame.image.load('heroes/Reptile/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Reptile/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/0.png')]
        self.hit_arm_middle = [pygame.image.load('heroes/Reptile/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()

        if gamer_n == 1:
            self.right, self.left = True, False
            self.x, self.y = 800, 20
        else:
            self.right, self.left = False, True
            self.x, self.y = 100, 20
        self.rect.x, self.rect.y = self.x, self.y

        self.xv, self.yv = 0, 0 # СКОРОСТИ

        self.jump_power = 1
        self.jump_coeff = 2
        self.jump_beauty_coeff = 1



    def update(self, left, right, jump, platforms):

        # time_now = pygame.time.get_ticks()
        # if time_now - self.time_hp > 50:
        #     self.hp -= 1


        # if not -2 < self.yv < 2:
        #     self.particle_action = True

        if left:
            self.xv = -MOVE_SPEED  # Лево = x - n
            # self.image = pygame.transform.flip(self.frames[self.cur_frame], 50, 0)
            self.the_straight_side = False

        if right:
            self.xv = MOVE_SPEED # Право = x + n
            # self.image = self.frames[self.cur_frame]
            self.the_straight_side = True

        if not (left or right): # стоим, когда нет указаний идти
            self.xv = 0

        if jump:
            if self.on_ground:  # прыгаем, только когда можем оттолкнуться от земли
                self.yv = -JUMP_POWER
                self.jump = True
                self.jump_coeff = 10

        if self.jump_coeff >= 0 - JUMP_POWER:
            if self.jump_coeff < 0:
                self.rect.y += (self.jump_coeff ** 2) / JUMP_BEAUTY_COEFF
            elif self.jump_coeff >= 0:
                self.rect.y -= (self.jump_coeff ** 2) / JUMP_BEAUTY_COEFF
            self.jump_coeff -= 1
        elif self.rect.y != 350:
            self.rect.y += (self.jump_coeff ** 2) / JUMP_BEAUTY_COEFF
            if self.rect.y > 350:
                self.rect.y = 350
        #
        # if jump:
        #     if self.on_ground: # прыгаем, только когда можем оттолкнуться от земли
        #         self.yv = -JUMP_POWER
        #         self.jump = True
        #
        # if not self.on_ground:
        #     self.yv += GRAVITY

        self.rect.y += self.yv
        self.collide(0, self.yv, platforms)

        self.rect.x += self.xv
        self.collide(self.xv, 0, platforms)

        self.on_ground = True


    def collide(self, xv, yv, platforms):
        for p in platforms:
            if p.rect.colliderect(self.rect):
                # if pygame.sprite.collide_mask(self, p):  # если есть пересечение платформы с игроком

                # Таким образом, персонаж взаимодействет лишь верхней и нижней частью своего хитбокса
                # if xv > 0:  # если движется вправо
                #     self.rect.ri
                #     ght = p.rect.left  # то не движется вправо
                #
                # if xv < 0:  # если движется влево
                #     self.rect.left = p.rect.right  # то не движется влево

                if yv > 0 and p.rect.top - 14 < self.rect.bottom < p.rect.top + 14 and p.enable:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.on_ground = True  # и становится на что-то твердое
                    self.yv = 0  # и энергия падения пропадает

                if yv < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yv = 0  # и энергия прыжка пропадает

                if xv > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xv < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yv > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.on_ground = True  # и становится на что-то твердое
                    self.yv = 0  # и энергия падения пропадает

                if yv < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yv = 0  # и энергия прыжка пропадает



class Reptile(MainHero):
    def __init__(self, parent, gamer_n=1):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
        self.image = pygame.image.load('heroes/Reptile/go/0.png')
        self.go = [pygame.image.load('heroes/Reptile/go/0.png'),
                   pygame.image.load('heroes/Reptile/go/1.png'),
                   pygame.image.load('heroes/Reptile/go/2.png'),
                   pygame.image.load('heroes/Reptile/go/3.png'),
                   pygame.image.load('heroes/Reptile/go/4.png'),
                   pygame.image.load('heroes/Reptile/go/5.png'),
                   pygame.image.load('heroes/Reptile/go/6.png'),
                   pygame.image.load('heroes/Reptile/go/7.png'),
                   pygame.image.load('heroes/Reptile/go/8.png')]
        # self.go = [pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #              pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #              pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png'),
        #            pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png')]

        self.jump = [pygame.image.load('heroes/Reptile/jump/0.png'),
                     pygame.image.load('heroes/Reptile/jump/1.png'),
                     pygame.image.load('heroes/Reptile/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Reptile/stand/0.png'),
                      pygame.image.load('heroes/Reptile/stand/1.png'),
                      pygame.image.load('heroes/Reptile/stand/2.png'),
                      pygame.image.load('heroes/Reptile/stand/3.png'),
                      pygame.image.load('heroes/Reptile/stand/4.png'),
                      pygame.image.load('heroes/Reptile/stand/5.png'),
                      pygame.image.load('heroes/Reptile/stand/6.png'),
                      pygame.image.load('heroes/Reptile/stand/7.png'),
                      pygame.image.load('heroes/Reptile/stand/8.png')]
        self.versus = pygame.image.load('heroes/Reptile/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Reptile/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Reptile/hit/arm/up/0.png')]
        self.hit_arm_middle = [pygame.image.load('heroes/Reptile/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Reptile/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()

        if gamer_n == 1:
            self.right, self.left = True, False
            self.x, self.y = 800, 25
        else:
            self.right, self.left = False, True
            self.x, self.y = 100, 25
        self.rect.x, self.rect.y = self.x, self.y



class Scorpion(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
        self.go = [pygame.image.load('heroes/Scorpion/go/0.png'),
                   pygame.image.load('heroes/Scorpion/go/1.png'),
                   pygame.image.load('heroes/Scorpion/go/2.png'),
                   pygame.image.load('heroes/Scorpion/go/3.png'),
                   pygame.image.load('heroes/Scorpion/go/4.png'),
                   pygame.image.load('heroes/Scorpion/go/5.png'),
                   pygame.image.load('heroes/Scorpion/go/6.png'),
                   pygame.image.load('heroes/Scorpion/go/7.png'),
                   pygame.image.load('heroes/Scorpion/go/8.png')]
        self.jump = [pygame.image.load('heroes/Scorpion/jump/0.png'),
                     pygame.image.load('heroes/Scorpion/jump/1.png'),
                     pygame.image.load('heroes/Scorpion/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Scorpion/stand/0.png'),
                      pygame.image.load('heroes/Scorpion/stand/1.png'),
                      pygame.image.load('heroes/Scorpion/stand/2.png'),
                      pygame.image.load('heroes/Scorpion/stand/3.png'),
                      pygame.image.load('heroes/Scorpion/stand/4.png'),
                      pygame.image.load('heroes/Scorpion/stand/5.png'),
                      pygame.image.load('heroes/Scorpion/stand/6.png'),
                      pygame.image.load('heroes/Scorpion/stand/7.png'),
                      pygame.image.load('heroes/Scorpion/stand/8.png')]
        self.versus = pygame.image.load('heroes/Scorpion/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Scorpion/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Scorpion/hit/arm/up/0.png')]

        self.hit_arm_middle = [pygame.image.load('heroes/Scorpion/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Scorpion/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()


class SubZero(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
        self.go = [pygame.image.load('heroes/Sub_Zero/go/0.png'),
                   pygame.image.load('heroes/Sub_Zero/go/1.png'),
                   pygame.image.load('heroes/Sub_Zero/go/2.png'),
                   pygame.image.load('heroes/Sub_Zero/go/3.png'),
                   pygame.image.load('heroes/Sub_Zero/go/4.png'),
                   pygame.image.load('heroes/Sub_Zero/go/5.png'),
                   pygame.image.load('heroes/Sub_Zero/go/6.png'),
                   pygame.image.load('heroes/Sub_Zero/go/7.png'),
                   pygame.image.load('heroes/Sub_Zero/go/8.png')]
        self.jump = [pygame.image.load('heroes/Sub_Zero/jump/0.png'),
                     pygame.image.load('heroes/Sub_Zero/jump/1.png'),
                     pygame.image.load('heroes/Sub_Zero/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Sub_Zero/stand/0.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/1.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/2.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/3.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/4.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/5.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/6.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/7.png'),
                      pygame.image.load('heroes/Sub_Zero/stand/8.png')]
        self.versus = pygame.image.load('heroes/Sub_Zero/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Sub_Zero/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Sub_Zero/hit/arm/up/0.png')]
        self.hit_arm_middle = [pygame.image.load('heroes/Sub_Zero/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Sub_Zero/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()


class Smoke(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
        self.go = [pygame.image.load('heroes/Smoke/go/0.png'),
                   pygame.image.load('heroes/Smoke/go/1.png'),
                   pygame.image.load('heroes/Smoke/go/2.png'),
                   pygame.image.load('heroes/Smoke/go/3.png'),
                   pygame.image.load('heroes/Smoke/go/4.png'),
                   pygame.image.load('heroes/Smoke/go/5.png'),
                   pygame.image.load('heroes/Smoke/go/6.png'),
                   pygame.image.load('heroes/Smoke/go/7.png'),
                   pygame.image.load('heroes/Smoke/go/8.png')]
        self.jump = [pygame.image.load('heroes/Smoke/jump/0.png'),
                     pygame.image.load('heroes/Smoke/jump/1.png'),
                     pygame.image.load('heroes/Smoke/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Smoke/stand/0.png'),
                      pygame.image.load('heroes/Smoke/stand/1.png'),
                      pygame.image.load('heroes/Smoke/stand/2.png'),
                      pygame.image.load('heroes/Smoke/stand/3.png'),
                      pygame.image.load('heroes/Smoke/stand/4.png'),
                      pygame.image.load('heroes/Smoke/stand/5.png'),
                      pygame.image.load('heroes/Smoke/stand/6.png'),
                      pygame.image.load('heroes/Smoke/stand/7.png'),
                      pygame.image.load('heroes/Smoke/stand/8.png')]
        self.versus = pygame.image.load('heroes/Smoke/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Smoke/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Smoke/hit/arm/up/0.png')]
        self.hit_arm_middle = [pygame.image.load('heroes/Smoke/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Smoke/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()


class KungLao(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 81
        self.height = 136
        self.speed = 4
        self.k_jump = 4
        self.go = [pygame.image.load('heroes/Kung_Lao/go/0.png'),
                   pygame.image.load('heroes/Kung_Lao/go/1.png'),
                   pygame.image.load('heroes/Kung_Lao/go/2.png'),
                   pygame.image.load('heroes/Kung_Lao/go/3.png'),
                   pygame.image.load('heroes/Kung_Lao/go/4.png'),
                   pygame.image.load('heroes/Kung_Lao/go/5.png'),
                   pygame.image.load('heroes/Kung_Lao/go/6.png'),
                   pygame.image.load('heroes/Kung_Lao/go/7.png'),
                   pygame.image.load('heroes/Kung_Lao/go/8.png')]
        self.jump = [pygame.image.load('heroes/Kung_Lao/jump/0.png'),
                     pygame.image.load('heroes/Kung_Lao/jump/1.png'),
                     pygame.image.load('heroes/Kung_Lao/jump/2.png')]
        self.stand = [pygame.image.load('heroes/Kung_Lao/stand/0.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/1.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/2.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/3.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/4.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/5.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/6.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/7.png'),
                      pygame.image.load('heroes/Kung_Lao/stand/8.png')]
        self.versus = pygame.image.load('heroes/Kung_Lao/versus/0.png')
        self.hit_arm_up = [pygame.image.load('heroes/Kung_Lao/hit/arm/up/0.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/1.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/2.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/3.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/4.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/5.png'),
                           pygame.image.load('heroes/Kung_Lao/hit/arm/up/0.png')]
        self.hit_arm_middle = [pygame.image.load('heroes/Kung_Lao/hit/arm/middle/0.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/1.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/2.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/3.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/4.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/5.png'),
                               pygame.image.load('heroes/Kung_Lao/hit/arm/middle/0.png')]
        self.rect = self.go[0].get_rect()
