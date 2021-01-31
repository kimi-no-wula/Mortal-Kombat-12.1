from setting import *


def default():
    global num_iteration, fon, g1_x, g1_y, g2_x, g2_y, g2_anim, g1_stand, g2_stand, g1_h, g2_h
    num_iteration = 0
    fon = fon_
    g1_x = W - 50 - g1_w - rx - g1_w
    g1_h = gamer_1.height
    g1_y = H - g1_h - ry
    g1_stand = True
    g2_x = 50 + g2_w + rx
    g2_h = gamer_2.height
    g2_y = H - g2_h - ry
    g2_stand = True


# анимация
def animation(aC, anim, stay_side, w, x, y, in_jump, meter_jump, in_hit):
    if meter_jump == 1:
        aC = 2
    elif meter_jump == 20:
        aC = 5
    elif meter_jump == 23:
        aC = 0
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
        if in_hit:
            in_hit = False
        aC = 0
    return [aC, in_hit]


# прорисовка игры
def window():
    global aC
    global aC1
    global choose_heroes_right_heroes_y
    global choose_heroes_right_heroes_x
    global g1_in_hit
    global g2_in_hit
    win.blit(fon, (0, 0))
    win.blit(update_fps(), (10, 0))
    kk = animation(aC, g1_anim, g1_stay_side, g1_w, g1_x, g1_y, g1_in_jump, g1_meter_jump, g1_in_hit)
    aC = kk[0]
    g1_in_hit = kk[1]
    kk = animation(aC1, g2_anim, g2_stay_side, g2_w, g2_x, g2_y, g2_in_jump, g2_meter_jump, g2_in_hit)
    aC1 = kk[0]
    g2_in_hit = kk[1]
    if window_num == 0:
        for i in choose_heroes_right_heroes:
            win.blit(i, (choose_heroes_right_heroes_x, choose_heroes_right_heroes_y))
            choose_heroes_right_heroes_x += 65
    pygame.display.update()


# выбор персонажа
def window_choose_heroes():
    global choose_heroes_fons_aC
    global fon
    global choose_heroes_right_heroes_x
    fon = choose_heroes_fons_anim[choose_heroes_fons_aC // (len(choose_heroes_fons_anim) - 1)]
    choose_heroes_fons_aC += 1
    if choose_heroes_fons_aC >= len(choose_heroes_fons_anim) ** 2 - len(choose_heroes_fons_anim):
        choose_heroes_fons_aC = 0
    window()
    choose_heroes_right_heroes_x = 5


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("red"))
    return fps_text


def keyb_go(key1, key2, x, W, w, rx, stay_side, speed, stand, in_jump, anim, gamer, go):
    if key1 and x < W - w - rx and not key2:
        if not stay_side and not in_jump:
            anim = gamer.go[::-1]
        x += speed
        stand = False
        go = True
    elif key2 and x > rx and not key1:
        if stay_side and not in_jump:
            anim = gamer.go[::-1]
        x -= speed
        stand = False
        go = True
    elif stand and not in_jump:
        anim = gamer.stand
        go = False
    else:
        stand = True
        go = False
    return [x, stay_side, stand, in_jump, anim, go]


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

        if keys[pygame.K_p]:
            if window_num == 1:
                window_num = -1
            window_num += 1

        if window_num == 1:

            #   разворот игроков
            if keys[pygame.K_l] and not g1_in_jump and not g1_in_hit:
                g1_anim = gamer_1.hit_arm_up
                if (keys[pygame.K_LEFT] and gamer_position) or (keys[pygame.K_RIGHT] and not gamer_position):
                    g1_anim = gamer_1.hit_arm_middle
                aC = 0
                g1_in_hit = True
                g1_stand = False
                g1_go = False


            if keys[pygame.K_g] and not g2_in_jump and not g2_in_hit:
                g2_anim = gamer_2.hit_arm_up
                if (keys[pygame.K_d] and gamer_position) or (keys[pygame.K_a] and not gamer_position):
                    g2_anim = gamer_2.hit_arm_middle
                aC1 = 0
                g2_in_hit = True
                g2_stand = False
                g2_go = False

            if g2_x + int(g2_anim[aC1 // (len(g2_anim) - 1)].get_rect()[2]) // 2 < g1_x + \
                    int(g1_anim[aC // (len(g1_anim) - 1)].get_rect()[2]) // 2:
                if g1_stand:
                    g1_stay_side = False
                if g2_stand:
                    g2_stay_side = True
                gamer_position = True
            else:
                if g1_stand:
                    g1_stay_side = True
                if g2_stand:
                    g2_stay_side = False
                gamer_position = False
            if not g1_in_jump and not g1_in_hit:
                g1_anim = gamer_1.go
            if not g2_in_jump and not g2_in_hit:
                g2_anim = gamer_2.go
            if not g1_in_hit and not g1_pause:
                kk = keyb_go(keys[pygame.K_RIGHT], keys[pygame.K_LEFT], g1_x, W, g1_w, rx, g1_stay_side, g1_speed, g1_stand,
                             g1_in_jump, g1_anim, gamer_1, g1_go)
                g1_x = kk[0]
                g1_stay_side = kk[1]
                g1_stand = kk[2]
                g1_in_jump = kk[3]
                g1_anim = kk[4]
                g1_go = kk[5]
            if not g2_in_hit and not g2_pause:
                kk = keyb_go(keys[pygame.K_d], keys[pygame.K_a], g2_x, W, g2_w, rx, g2_stay_side, g2_speed, g2_stand,
                             g2_in_jump, g2_anim, gamer_2, g2_go)
                g2_x = kk[0]
                g2_stay_side = kk[1]
                g2_stand = kk[2]
                g2_in_jump = kk[3]
                g2_anim = kk[4]
                g2_go = kk[5]

            # kk = keyboard1(g1_in_jump, keys[pygame.K_UP], g1_stand, g1_anim, aC, g1_meter_jump, g1_jump_coeff,
            # g1_jump_speed, g1_y, g1_k_jump, H, g1_h, ry, gamer_1)
            # g1_in_jump = kk[0]
            # g1_stand = kk[1]
            # g1_anim = kk[2]
            # aC = [3]
            # g1_meter_jump = kk[4]
            # g1_y = kk[5]
            if not g1_in_hit:
                if not g1_in_jump:
                    if keys[pygame.K_UP] and not g1_pause:
                        g1_in_jump = True
                        g1_stand = False
                        g1_go = False
                        g1_anim = gamer_1.jump
                        aC = 0
                        g1_meter_jump = 0
                else:
                    g1_meter_jump += 1
                    if g1_jump_coeff >= 0 - g1_jump_speed:
                        if g1_jump_coeff < 0:
                            g1_y += (g1_jump_coeff ** 2) / g1_k_jump - 2
                        elif g1_jump_coeff >= 0:
                            g1_y -= (g1_jump_coeff ** 2) / g1_k_jump + 2
                        g1_jump_coeff -= 1
                    elif g1_y != H - g1_h - ry:
                        g1_y += (g1_jump_coeff ** 2) / g1_k_jump
                        if g1_y > H - g1_h - ry:
                            g1_y = H - g1_h - ry
                    elif g1_meter_jump >= 24 and g1_meter_jump < 32:
                        g1_pause = True
                        g1_meter_jump += 1
                    elif g1_meter_jump == 32:
                        g1_pause = False
                    else:
                        g1_in_jump = False
                        g1_jump_coeff = g1_jump_speed
                        aC = 0
                        g1_anim = gamer_1.stand
                        g1_stand = True

                if not g2_in_hit:
                    if not g2_in_jump:
                        if keys[pygame.K_w] and not g2_pause:
                            g2_in_jump = True
                            g2_stand = False
                            g2_anim = gamer_2.jump
                            aC1 = 0
                            g2_meter_jump = 0
                            g2_go = False
                    else:
                        g2_meter_jump += 1
                        if g2_jump_coeff >= 0 - g2_jump_speed:
                            if g2_jump_coeff < 0:
                                g2_y += (g2_jump_coeff ** 2) / g2_k_jump - 2
                            elif g2_jump_coeff >= 0:
                                g2_y -= (g2_jump_coeff ** 2) / g2_k_jump + 2
                            g2_jump_coeff -= 1
                        elif g2_y != H - g2_h - ry:
                            g2_y += (g2_jump_coeff ** 2) / g2_k_jump
                            if g2_y > H - g2_h - ry:
                                g2_y = H - g2_h - ry
                        elif g2_meter_jump >= 24 and g2_meter_jump < 32:
                            g2_pause = True
                            g2_meter_jump += 1
                        elif g2_meter_jump == 32:
                            g2_pause = False
                        else:
                            g2_in_jump = False
                            g2_jump_coeff = g2_jump_speed
                            aC1 = 0
                            g2_anim = gamer_2.stand
                            g2_stand = True

            all_sprites.update()
            if keys[pygame.K_ESCAPE]:
                run = False





            # if gamer_1.rect.x < gamer_2.rect.x:
            # print(gamer_1.rect.left, gamer_2.rect.right)
            # print('------------------------', 'столкновение')

            window()
        elif window_num == 0:
            window_choose_heroes()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]:
                gamer_1 = heroes_all[0]
            elif keys[pygame.K_1]:
                gamer_1 = heroes_all[1]
            elif keys[pygame.K_2]:
                gamer_1 = heroes_all[2]
            elif keys[pygame.K_3]:
                gamer_1 = heroes_all[3]
            elif keys[pygame.K_4]:
                gamer_1 = heroes_all[4]
            if keys[pygame.K_q]:
                gamer_2 = heroes_all[0]
            elif keys[pygame.K_w]:
                gamer_2 = heroes_all[1]
            elif keys[pygame.K_e]:
                gamer_2 = heroes_all[2]
            elif keys[pygame.K_r]:
                gamer_2 = heroes_all[3]
            elif keys[pygame.K_t]:
                gamer_2 = heroes_all[4]
            g2_anim = gamer_2.stand
            g1_anim = gamer_1.stand
            default()
    pygame.quit()
