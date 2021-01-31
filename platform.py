import pygame

PLATFORM_WIDTH = 1200
PLATFORM_HEIGHT = 5
PLATFORM_COLOR = "orange"


class PlatformX(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = 2
        self.enable = True
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        # self.image = transform.scale(load_image("data_images/platform", "p2.jpg", -1), (PLATFORM_WIDTH,
        # PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pass


class PlatformY(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = 2
        self.enable = True
        self.image = pygame.Surface((5, 600))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        # self.image = transform.scale(load_image("data_images/platform", "p2.jpg", -1), (PLATFORM_WIDTH,
        # PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, 5, 600)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pass
