import pygame
import pyganim
import os


class MainHero:
    def __init__(self):
        pass

    def actions(self):
        # Здесь будут расписаны различные действия игроков,
        # которые и будут наследоваться каждому следующему персонажу
        pass


class Reptile(MainHero, pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 68
        self.height = 133
        self.speed = 1
        self.k_jump = 4
        self.go = [pygame.image.load('персонажи/Reptile/идет/вправо/0.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/1.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/2.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/3.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/4.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/5.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/6.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/7.png'),
                         pygame.image.load('персонажи/Reptile/идет/вправо/8.png')]



        self.jump = [pygame.image.load('персонажи/Reptile/прыгает/вправо/0.png'),
                           pygame.image.load('персонажи/Reptile/прыгает/вправо/1.png'),
                           pygame.image.load('персонажи/Reptile/прыгает/вправо/2.png')]
        self.stand = [pygame.image.load('персонажи/Reptile/стоит/вправо/0.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/1.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/2.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/3.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/4.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/5.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/6.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/7.png'),
                      pygame.image.load('персонажи/Reptile/стоит/вправо/8.png')]
        self.rect = self.go[0].get_rect()