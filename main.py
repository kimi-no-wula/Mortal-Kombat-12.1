from setting import *


# анимация
def animation(aC, anim, stay_side, w, x, y, in_jump, meter_jump):
    if meter_jump == 1:
        aC = 2
    elif meter_jump == 20:
        aC = 5
    if not stay_side:
        im = anim[aC // (len(anim) - 1)]
        x_rect = anim[aC // (len(anim) - 1)].get_rect()
        print(x_rect)
        im = pygame.transform.flip(im, not stay_side, False)
        kAn_x = w - int(im.get_rect()[2])
        win.blit(im, (x + kAn_x, y))
    elif stay_side:
        im = anim[aC // (len(anim) - 1)]
        x_rect = anim[aC // (len(anim) - 1)].get_rect()
        print(x_rect)
        win.blit(im, (x, y))
    if not in_jump:
        aC += 1
    if aC >= len(anim) ** 2 - len(anim) and not in_jump:
        aC = 0
    return aC


# прорисовка игры
def window():
    global aC
    global aC1
    win.blit(fon, (0, 0))
    win.blit(update_fps(), (10, 0))
    aC = animation(aC, g1_anim, g1_stay_side, g1_w, g1_x, g1_y, g1_in_jump, g1_meter_jump)
    aC1 = animation(aC1, g2_anim, g2_stay_side, g2_w, g2_x, g2_y, g2_in_jump, g2_meter_jump)
    pygame.display.update()


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("red"))
    return fps_text




def keyboard00(key1, key2, x, W, w, rx, stay_side, speed, stand, in_jump, anim, gamer):
    if key1 and x < W - w - rx and not key2:
        stay_side = True
        x += speed
        if not in_jump:
            anim = gamer.go
        stand = False
    elif key2 and x > rx:
        x -= speed
        stay_side = False
        if not in_jump:
            anim = gamer.go
        stand = False
    elif stand and not in_jump:
        anim = gamer.stand
    else:
        stand = True
    return [x, stay_side, stand, in_jump, anim, fon]


def keyboard(key1, key2, x, W, w, rx, stay_side, speed, stand, in_jump, anim, gamer):
    if key1 and x < W - w - rx and not key2:
        x += speed
        stand = False
    elif key2 and x > rx:
        x -= speed
        stand = False
    elif stand and not in_jump:
        anim = gamer.stand
    else:
        stand = True
    return [x, stay_side, stand, in_jump, anim]


def keyboard1(in_jump, key3, stand, anim, aC, meter_jump, jump_coeff, jump_speed, y, k_jump, H, h, ry, gamer):
    if not in_jump:
        if key3:
            in_jump = True
            stand = False
            anim = gamer.jump
            aC = 0
    else:
        meter_jump += 1
        if jump_coeff >= 0 - jump_speed:
            if jump_coeff < 0:
                y += (jump_coeff ** 2) / k_jump
            elif jump_coeff >= 0:
                y -= (jump_coeff ** 2) / k_jump
            jump_coeff -= 1
        elif y != H - h - ry:
            y += (jump_coeff ** 2) / k_jump
            if y > H - h - ry:
                y = H - h - ry
        else:
            in_jump = False
            jump_coeff = jump_speed
            aC = 0
            anim = gamer.stand
            stand = True
            meter_jump = 0
    return [in_jump, stand, anim, aC, meter_jump, y]


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
        print(g2_anim)
        if g2_x + int(g2_anim[aC1 // (len(g2_anim) - 1)].get_rect()[2]) < g1_x:
            g1_stay_side = False
            g2_stay_side = True
            if not g1_in_jump:
                g1_anim = gamer_1.go
            if not g2_in_jump:
                g2_anim = gamer_2.go
        else: 
            g1_stay_side = True

            g2_stay_side = False
            if not g1_in_jump:
                g1_anim = gamer_1.go[::-1]
            if not g2_in_jump:
                g2_anim = gamer_2.go[::-1]
        kk = keyboard(keys[pygame.K_RIGHT], keys[pygame.K_LEFT], g1_x, W, g1_w, rx, g1_stay_side, g1_speed, g1_stand,
                      g1_in_jump, g1_anim, gamer_1)
        g1_x = kk[0]
        g1_stay_side = kk[1]
        g1_stand = kk[2]
        g1_in_jump = kk[3]
        g1_anim = kk[4]
        kk = keyboard(keys[pygame.K_d], keys[pygame.K_a], g2_x, W, g2_w, rx, g2_stay_side, g2_speed, g2_stand,
                      g2_in_jump, g2_anim, gamer_2)
        g2_x = kk[0]
        g2_stay_side = kk[1]
        g2_stand = kk[2]
        g2_in_jump = kk[3]
        g2_anim = kk[4]

        #kk = keyboard1(g1_in_jump, keys[pygame.K_UP], g1_stand, g1_anim, aC, g1_meter_jump, g1_jump_coeff,
                       #g1_jump_speed, g1_y, g1_k_jump, H, g1_h, ry, gamer_1)
        #g1_in_jump = kk[0]
        #g1_stand = kk[1]
        #g1_anim = kk[2]
        #aC = [3]
        #g1_meter_jump = kk[4]
        #g1_y = kk[5]















        if not g1_in_jump:
            if keys[pygame.K_UP]:
                g1_in_jump = True
                g1_stand = False
                g1_anim = gamer_1.jump
                aC = 0
        else:
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
                g1_stand = True
                g1_meter_jump = 0


        if not g2_in_jump:
            if keys[pygame.K_w]:
                g2_in_jump = True
                g2_stand = False
                g2_anim = gamer_2.jump
                aC1 = 0
                g2_meter_jump = 0
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
                g2_anim = gamer_2.stand
                g2_stand = True



        all_sprites.update()
        if keys[pygame.K_ESCAPE]:
            run = False


        #if gamer_1.rect.x < gamer_2.rect.x:
            #print(gamer_1.rect.left, gamer_2.rect.right)
            #print('------------------------', 'столкновение')

        window()
    pygame.quit()
