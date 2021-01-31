import pygame
import setting

# основной цикл и, получается, основа всей программы
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('mk')
    # размеры окна:
    size = width, height = setting.W, setting.H
    fps = 90
    running = True
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont("Arial", 18)
    left, right, jump = False, False, False

    clock = pygame.time.Clock()

    while running:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
                elif ev.key == pygame.K_w:
                    jump = True
                elif ev.key == pygame.K_d:
                    right = True
                elif ev.key == pygame.K_a:
                    left = True

            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_w:
                    jump = False
                elif ev.key == pygame.K_d:
                    right = False
                elif ev.key == pygame.K_a:
                    left = False

        screen.blit(setting.fon.image, (0, 0))
        setting.platforms.draw(screen)
        setting.all_sprites.draw(screen)
        setting.gamer_1.update(left, right, jump, setting.platforms)
        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
