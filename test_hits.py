import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()
        self.im = pygame.load(pygame.image.load('персонажи/Reptile/идет/вправо/0.png'))

        self.rect = self.im.get_rect()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()
        self.im = pygame.load(pygame.image.load('sprite/pygame_idle.png'))

        self.rect = self.im.get_rect()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,  600), pygame.RESIZABLE)

    fps = 90
