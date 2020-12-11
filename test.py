from setting import *
import pygame

clock = pygame.time.Clock()


# прорисовка игры
def window():
    global aC
    global aC1
    screen.fill(tuple([random.randint(0, 255) for _ in range(3)]))
    win.blit(screen, (0, 0))
    if aC >= len(wL) ** 2 - len(wL):
        aC = 0
    if aC1 >= len(wL1) ** 2 - len(wL1):
        aC1 = 0
        print(aC1)
    if left:
        win.blit(wL[aC // (len(wL) - 1)], (x, y))
        aC += 1
    elif right:
        win.blit(wR[aC // (len(wR) - 1)], (x, y))
        aC += 1
    else:
        win.blit(g1_stand, (x, y))
    if ll:
        win.blit(wL1[aC1 // (len(wL1) - 1)], (xx, yy))
        aC1 += 1
    elif rr:
        win.blit(wR1[aC1 // (len(wR1) - 1)], (xx, yy))
        aC1 += 1
        print(aC1)
    pygame.display.update()


# основной цикл
while run:
    clock.tick(clock_)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < w - w_0 - rx and not(keys[pygame.K_LEFT]):
        print('>', x)
        left = False
        right = True
        x += speed
    elif keys[pygame.K_LEFT] and x > rx:
        print('<', x)
        x -= speed
        left = True
        right = False
    else:
        aC = 0

    if keys[pygame.K_d] and xx < w - w_1 - rx and not(keys[pygame.K_a]):
        print('>', x)
        ll = False
        rr = True
        xx += speed1
    elif keys[pygame.K_a] and xx > rx:
        print('<', x)
        xx -= speed1
        ll = True
        rr = False
    else:
        aC1 = 0











    if not Jump:
        if keys[pygame.K_UP]:
            Jump = True
    else:
        print('^', y)
        if JumpC >= 0 - JumpSpeed:
            if JumpC < 0:
                y += (JumpC ** 2) / g1_k_jump
            elif JumpC >= 0:
                y -= (JumpC ** 2) / g1_k_jump
            JumpC -= 1
        else:
            Jump = False
            JumpC = JumpSpeed
    if not Jump1:
        if keys[pygame.K_w]:
            Jump1 = True
    else:




        if JumpC1 >= 0 - JumpSpeed1:
            if JumpC1 < 0:
                yy += (JumpC1 ** 2) / g2_k_jump
            elif JumpC1 >= 0:
                yy -= (JumpC1 ** 2) / g2_k_jump
            JumpC1 -= 1
        else:
            Jump1 = False
            JumpC1 = JumpSpeed


    window()
    print('--------------------------', clock.get_fps())
    if keys[pygame.K_q]:
        pygame.quit()
pygame.quit()
