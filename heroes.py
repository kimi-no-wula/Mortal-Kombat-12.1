import pygame
import os


class MainHero:
    def __init__(self):
        pass

    def actions(self):
        # Здесь будут расписаны разwличные действия игроков,
        # которые и будут наследоваться каждому следующему персонажу
        pass


class Reptile(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 4
        self.k_jump = 4
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


class Sub_Zero(MainHero, pygame.sprite.Sprite):
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


class Kung_Lao(MainHero, pygame.sprite.Sprite):
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
