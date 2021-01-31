import pygame
import random


# ФОНЫ
class Fons:
    def __init__(self, size):
        self.fon1 = [pygame.image.load('fons/pygame_bg.jpg'),
                     pygame.image.load('fons/pygame_bg_1.jpg'),
                     pygame.image.load('fons/pygame_bg_2.jpg')]
        self.image = pygame.transform.scale(random.choice(self.fon1), size)
        self.image.get_rect()
