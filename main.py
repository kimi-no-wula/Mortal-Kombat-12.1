from setting import *

# прорисовка игры
def window():
    global aC
    global aC1
    win.blit(fon, (0, 0))
    win.blit(update_fps(), (10, 0))
    if g1_in_jump:
        print('--------------0',aC)
    if aC >= len(g1_anim) ** 2 - len(g1_anim) and not g1_in_jump:
        aC = 0
    if aC1 >= len(g2_anim) ** 2 - len(g2_anim) and not g2_in_jump:
        aC1 = 0
    if not g1_stay_side:
        im = g1_anim[aC // (len(g1_anim) - 1)]
        im = pygame.transform.flip(im, True, False)
        g1_kAn_x = g1_w - int(im.get_rect()[2])
        win.blit(im, (g1_x + g1_kAn_x, g1_y))
    elif g1_stay_side:
        im = g1_anim[aC // (len(g1_anim) - 1)]
        win.blit(im, (g1_x, g1_y))
    if not g1_in_jump:
        aC += 1
    if g1_meter_jump == 1:
        aC = 2
    elif g1_meter_jump == 20:
        aC = 5




    if not g2_stay_side:
        im = g2_anim[aC1 // (len(g2_anim) - 1)]
        im = pygame.transform.flip(im, True, False)
        g2_kAn_x = g2_w - int(im.get_rect()[2])
        win.blit(im, (g2_x + g2_kAn_x, g2_y))
    elif g2_stay_side:
        im = g2_anim[aC1 // (len(g2_anim) - 1)]
        win.blit(im, (g2_x, g2_y))
    if not g2_in_jump or g2_meter_jump == 1 or g2_meter_jump == 21:
        aC1 += 1
    pygame.display.update()


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


# основной цикл и, получается, основа всей программы
if __name__ == '__main__':
    font = pygame.font.SysFont("Arial", 18)
    clock = pygame.time.Clock()

    while run:
        clock.tick(clock_)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and g1_x < W - g1_w - rx and not (keys[pygame.K_LEFT]):
            print('>', g1_x)
            g1_stay_side = True
            g1_x += g1_speed
            if not g1_in_jump:
                g1_anim = gamer_1.go
            g1_stand = False
        elif keys[pygame.K_LEFT] and g1_x > rx:
            print('<', g1_x)
            g1_x -= g1_speed
            g1_stay_side = False
            if not g1_in_jump:
                g1_anim = gamer_1.go
            g1_stand = False
        elif g1_stand and not g1_in_jump:
            g1_anim = gamer_1.stand
        else:
            g1_stand = True





        if keys[pygame.K_d] and g2_x < W - g2_w - rx and not (keys[pygame.K_a]):
            g2_stay_side = True
            g2_x += g2_speed
            if not g2_in_jump:
                g2_anim = gamer_2.go
            g2_stand = False
        elif keys[pygame.K_a] and g2_x > rx:
            g2_x -= g2_speed
            g2_stay_side = False
            if not g2_in_jump:
                g2_anim = gamer_2.go
            g2_stand = False
        elif g2_stand and not g2_in_jump:
            g2_anim = gamer_2.stand
        else:
            aC1 = 0
            g2_stand = True











        if not g1_in_jump:
            if keys[pygame.K_UP]:
                g1_in_jump = True
                g1_stand = False
                g1_anim = gamer_1.jump
                aC = 0
        else:
            print('^', g1_y, g1_meter_jump, aC)
            g1_meter_jump += 1
            if g1_jump_coeff >= 0 - g1_jump_speed:
                if g1_jump_coeff < 0:
                    g1_y += (g1_jump_coeff ** 2) / g1_k_jump
                elif g1_jump_coeff >= 0:
                    g1_y -= (g1_jump_coeff ** 2) / g1_k_jump
                g1_jump_coeff -= 1
            elif g1_y != H - g1_h - ry:
                g1_y += (g1_jump_coeff ** 2) / g1_k_jump
                if g1_y > H - g1_h - ry:
                    y = H - g1_h - ry
            else:
                g1_in_jump = False
                g1_jump_coeff = g1_jump_speed
                aC = 0
                g1_anim = gamer_1.stand
                g1_stand = False
                g1_meter_jump = 0
                print('-----------------')





        if not g2_in_jump:
            if keys[pygame.K_w]:
                g2_in_jump = True
                g2_stand = False
                g2_anim = gamer_2.jump
                aC1 = 0
        else:
            g2_meter_jump += 1
            if g2_jump_coeff >= 0 - g2_jump_speed:
                if g2_jump_coeff < 0:
                    g2_y += (g2_jump_coeff ** 2) / g2_k_jump
                elif g2_jump_coeff >= 0:
                    g2_y -= (g2_jump_coeff ** 2) / g2_k_jump
                g2_jump_coeff -= 1
            elif g2_y != H - g2_h - ry:
                g2_y += (g2_jump_coeff ** 2) / g2_k_jump
                if g2_y > H - g2_h - ry:
                    g2_y = H - g2_h - ry
            else:
                g2_in_jump = False
                g2_jump_coeff = g2_jump_speed
                aC1 = 0
                g2_anim = gamer_2.go
                g2_stand = True
                g2_meter_jump = 0
        all_sprites.update()

        #if gamer_1.rect.x < gamer_2.rect.x:
            #print(gamer_1.rect.left, gamer_2.rect.right)
            #print('------------------------', 'столкновение')

        window()
    pygame.quit()
