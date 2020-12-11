import pygame


class Reptile:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.width = 68
        self.height = 129

        # персонаж
        self.wR = [pygame.image.load('персонажи/Reptile/идет/вправо/0.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/1.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/2.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/3.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/4.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/5.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/6.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/7.png')]

        self.wL = [pygame.image.load('персонажи/Reptile/идет/влево/0.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/1.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/2.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/3.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/4.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/5.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/6.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/7.png')]
        self.wL = [pygame.transform.scale(i, (self.width, self.height)) for i in self.wL]


class Trump:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.width = 120
        self.height = 50

        # персонаж
        self.wR = [pygame.image.load('персонажи/Reptile/идет/вправо/0.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/1.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/2.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/3.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/4.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/5.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/6.png'),
              pygame.image.load('персонажи/Reptile/идет/вправо/7.png')]
        self.wR = [pygame.transform.scale(i, (self.width, self.height)) for i in self.wR]
        self.wL = [pygame.image.load('персонажи/Reptile/идет/влево/0.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/1.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/2.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/3.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/4.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/5.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/6.png'),
              pygame.image.load('персонажи/Reptile/идет/влево/7.png')]
        self.wL = [pygame.transform.scale(i, (self.width, self.height)) for i in self.wL]