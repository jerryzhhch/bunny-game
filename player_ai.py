import pygame
import random
from global_inst import *
from find_area import find_area_num, random_area_num


def Player_vs_AI():
    turn = 1
    area_num = -1
    card_left = 16
    score_player = 0
    score_ai = 0
    comp_list = []
    card_list = []
    # event click to help with ai simulation
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN)

    # initialize game
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bunny game")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    # load game images
    egg1 = pygame.image.load(os.path.join(img_folder, "egg1.png")).convert()
    egg1 = pygame.transform.scale(egg1, (80, 120))
    egg2 = pygame.image.load(os.path.join(img_folder, "egg2.png")).convert()
    egg2 = pygame.transform.scale(egg2, (80, 120))
    egg3 = pygame.image.load(os.path.join(img_folder, "egg3.png")).convert()
    egg3 = pygame.transform.scale(egg3, (80, 120))
    egg4 = pygame.image.load(os.path.join(img_folder, "egg4.png")).convert()
    egg4 = pygame.transform.scale(egg4, (80, 120))
    egg5 = pygame.image.load(os.path.join(img_folder, "egg5.png")).convert()
    egg5 = pygame.transform.scale(egg5, (80, 120))
    egg6 = pygame.image.load(os.path.join(img_folder, "egg6.png")).convert()
    egg6 = pygame.transform.scale(egg6, (80, 120))
    egg7 = pygame.image.load(os.path.join(img_folder, "egg7.png")).convert()
    egg7 = pygame.transform.scale(egg7, (80, 120))
    bunny = pygame.image.load(os.path.join(img_folder, "bunny.png")).convert()
    bunny = pygame.transform.scale(bunny, (80, 120))
    card_back = pygame.image.load(os.path.join(img_folder, "card.png")).convert()
    card_back = pygame.transform.scale(card_back, (80, 120))
    background = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
    background = pygame.transform.scale(background, (width, height))
    bg_rect = background.get_rect()
    bg_rect.center = (width / 2, height / 2)
    text_cover = pygame.image.load(os.path.join(img_folder, "cover.png")).convert()
    text_cover = pygame.transform.scale(text_cover, (50, 50))
    # load texts and scores on the screen
    font_name = pygame.font.SysFont("Arial", 40, True, False)
    text_player_name = font_name.render("YOU", False, red)
    text_ai_name = font_name.render("AI", False, black)
    font_score = pygame.font.SysFont("Arial", 30, True, False)
    text_player = font_score.render("0", False, black)
    text_ai = font_score.render("0", False, black)
    font_win = pygame.font.SysFont("Arial", 100, True, False)
    font_draw = pygame.font.SysFont("Arial", 100, True, False)
    font_lose = pygame.font.SysFont("Arial", 100, True, False)
    # load sound
    turn_sound = pygame.mixer.Sound(os.path.join(sound_folder, "turn_over.wav"))
    turn_sound.set_volume(0.4)
    win_sound = pygame.mixer.Sound(os.path.join(sound_folder, "win.wav"))
    draw_sound = pygame.mixer.Sound(os.path.join(sound_folder, "draw.wav"))
    lose_sound = pygame.mixer.Sound(os.path.join(sound_folder, "lose.wav"))
    bunny_sound = pygame.mixer.Sound(os.path.join(sound_folder, "bunny.wav"))
    bunny_sound.set_volume(5)
    score_sound = pygame.mixer.Sound(os.path.join(sound_folder, "score.wav"))
    score_sound.set_volume(0.4)
    # shuffle the cards
    random.shuffle(value_in_area)

    # class for card object
    class Card:
        def __init__(self, value, area):
            self.card_value = value
            self.card_area = area
            self.shown = False
            if self.card_value == 1:
                self.image = egg1
            if self.card_value == 2:
                self.image = egg2
            if self.card_value == 3:
                self.image = egg3
            if self.card_value == 4:
                self.image = egg4
            if self.card_value == 5:
                self.image = egg5
            if self.card_value == 6:
                self.image = egg6
            if self.card_value == 7:
                self.image = egg7
            if self.card_value == 8:
                self.image = bunny

    # add cards to a card list
    for i in range(16):
        card = Card(value_in_area[i], area_list[i])
        card_list.append(card)

    # setup board with 16 cards face down, and texts
    screen.fill(white)
    screen.blit(background, bg_rect)
    for coor in area_list:
        screen.blit(card_back, coor)
    screen.blit(text_player_name, (60, 100))
    screen.blit(text_ai_name, (670, 100))
    screen.blit(text_player, (90, 150))
    screen.blit(text_ai, (680, 150))

    running = True
    # game loop
    while running:
        # if ai turn then simulate mouse button click to continue ai picking
        if turn == 2:
            pygame.event.post(click)
        # after ai turn, update highlight to reflect player turn
        elif turn == 1:
            text_player_name = font_name.render("YOU", False, red)
            screen.blit(text_player_name, (60, 100))
            text_ai_name = font_name.render("AI", False, black)
            screen.blit(text_ai_name, (670, 100))
            #pygame.time.wait(1000)

        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            else:
                windows_focus = pygame.mouse.get_focused()
                if windows_focus == 1:
                    # player's turn
                    if turn == 1:
                        # if the player has selected two cards:
                        if comp_list.__len__() == 2:
                            # compare two selected cards
                            # if match
                            if comp_list[0].card_value == comp_list[1].card_value:
                                # update the score
                                score_sound.play()
                                score_player = score_player + 1
                                # user white cover overlap the old score
                                screen.blit(text_cover, (70, 150))
                                # show up the new score text
                                text_player = font_score.render(str(score_player), False, black)
                                screen.blit(text_player, (90, 150))
                                pygame.display.update()
                                # decrease the total fo card by 2
                                card_left = card_left - 2
                                # if bunny is found, get extra turn
                                if comp_list[0].card_value == 8:
                                    print("found bunny, get extra turn")
                                    bunny_sound.play()
                                    turn = 1
                                else:
                                    turn = 2
                            # if not match
                            else:
                                comp_list[0].shown = False
                                comp_list[1].shown = False
                                screen.blit(card_back, comp_list[0].card_area)
                                screen.blit(card_back, comp_list[1].card_area)
                                pygame.time.wait(500)
                                turn = 2
                            # clear the compare list
                            comp_list.clear()
                        # if the player has NOT selected two cards:
                        else:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos_x, pos_y = pygame.mouse.get_pos()
                                area_num = find_area_num(pos_x, pos_y)
                                if area_num:
                                    if area_num == 1:
                                        if not card_list[0].shown:
                                            turn_sound.play()
                                            screen.blit(card_list[0].image, card_list[0].card_area)
                                            card_list[0].shown = True
                                            comp_list.append(card_list[0])
                                        else:
                                            pass
                                    if area_num == 2:
                                        if not card_list[1].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[1].image, card_list[1].card_area)
                                            card_list[1].shown = True
                                            comp_list.append(card_list[1])
                                        else:
                                            pass
                                    if area_num == 3:
                                        if not card_list[2].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[2].image, card_list[2].card_area)
                                            card_list[2].shown = True
                                            comp_list.append(card_list[2])
                                        else:
                                            pass
                                    if area_num == 4:
                                        if not card_list[3].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[3].image, card_list[3].card_area)
                                            card_list[3].shown = True
                                            comp_list.append(card_list[3])
                                        else:
                                            pass
                                    if area_num == 5:
                                        if not card_list[4].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[4].image, card_list[4].card_area)
                                            card_list[4].shown = True
                                            comp_list.append(card_list[4])
                                        else:
                                            pass
                                    if area_num == 6:
                                        if not card_list[5].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[5].image, card_list[5].card_area)
                                            card_list[5].shown = True
                                            comp_list.append(card_list[5])
                                        else:
                                            pass
                                    if area_num == 7:
                                        if not card_list[6].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[6].image, card_list[6].card_area)
                                            card_list[6].shown = True
                                            comp_list.append(card_list[6])
                                        else:
                                            pass
                                    if area_num == 8:
                                        if not card_list[7].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[7].image, card_list[7].card_area)
                                            card_list[7].shown = True
                                            comp_list.append(card_list[7])
                                        else:
                                            pass
                                    if area_num == 9:
                                        if not card_list[8].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[8].image, card_list[8].card_area)
                                            card_list[8].shown = True
                                            comp_list.append(card_list[8])
                                        else:
                                            pass
                                    if area_num == 10:
                                        if not card_list[9].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[9].image, card_list[9].card_area)
                                            card_list[9].shown = True
                                            comp_list.append(card_list[9])
                                        else:
                                            pass
                                    if area_num == 11:
                                        if not card_list[10].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[10].image, card_list[10].card_area)
                                            card_list[10].shown = True
                                            comp_list.append(card_list[10])
                                        else:
                                            pass
                                    if area_num == 12:
                                        if not card_list[11].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[11].image, card_list[11].card_area)
                                            card_list[11].shown = True
                                            comp_list.append(card_list[11])
                                        else:
                                            pass
                                    if area_num == 13:
                                        if not card_list[12].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[12].image, card_list[12].card_area)
                                            card_list[12].shown = True
                                            comp_list.append(card_list[12])
                                        else:
                                            pass
                                    if area_num == 14:
                                        if not card_list[13].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[13].image, card_list[13].card_area)
                                            card_list[13].shown = True
                                            comp_list.append(card_list[13])
                                        else:
                                            pass
                                    if area_num == 15:
                                        if not card_list[14].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[14].image, card_list[14].card_area)
                                            card_list[14].shown = True
                                            comp_list.append(card_list[14])
                                        else:
                                            pass
                                    if area_num == 16:
                                        if not card_list[15].shown:
                                            turn_sound.play()
                                            pygame.time.wait(300)
                                            screen.blit(card_list[15].image, card_list[15].card_area)
                                            card_list[15].shown = True
                                            comp_list.append(card_list[15])
                                        else:
                                            pass
                                else:
                                    pass

                    # AI's turn
                    if turn == 2:
                        text_player_name = font_name.render("YOU", False, black)
                        screen.blit(text_player_name, (60, 100))
                        text_ai_name = font_name.render("AI", False, red)
                        screen.blit(text_ai_name, (670, 100))
                        # if AI has selected two cards:
                        if comp_list.__len__() == 2:
                            # compare two selected cards
                            if comp_list[0].card_value == comp_list[1].card_value:
                                # update the score
                                score_sound.play()
                                score_ai = score_ai + 1
                                # user white cover overlap the old score
                                screen.blit(text_cover, (660, 150))
                                # show up the new score text
                                text_ai = font_score.render(str(score_ai), False, black)
                                screen.blit(text_ai, (680, 150))
                                pygame.display.update()
                                # decrease the total fo card by 2
                                card_left = card_left - 2
                                # if bunny is found, get extra turn
                                if comp_list[0].card_value == 8:
                                    print("found bunny, get extra turn")
                                    bunny_sound.play()
                                    turn = 2
                                else:
                                    turn = 1
                            else:
                                comp_list[0].shown = False
                                comp_list[1].shown = False
                                screen.blit(card_back, comp_list[0].card_area)
                                screen.blit(card_back, comp_list[1].card_area)
                                pygame.time.wait(500)
                                turn = 1
                            comp_list.clear()
                        # if AI has NOT selected two cards:
                        else:
                            pygame.time.wait(2000)
                            # level 0 AI (pick the two cards randomly)
                            print("AI is choosing card...")
                            # GET A RANDOM CARD POSITION FROM A FUNCTION
                            area_num = random_area_num(card_list)
                            if area_num:
                                if area_num == 1:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[0].image, card_list[0].card_area)
                                    card_list[0].shown = True
                                    comp_list.append(card_list[0])
                                if area_num == 2:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[1].image, card_list[1].card_area)
                                    card_list[1].shown = True
                                    comp_list.append(card_list[1])
                                if area_num == 3:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[2].image, card_list[2].card_area)
                                    card_list[2].shown = True
                                    comp_list.append(card_list[2])
                                if area_num == 4:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[3].image, card_list[3].card_area)
                                    card_list[3].shown = True
                                    comp_list.append(card_list[3])
                                if area_num == 5:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[4].image, card_list[4].card_area)
                                    card_list[4].shown = True
                                    comp_list.append(card_list[4])
                                if area_num == 6:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[5].image, card_list[5].card_area)
                                    card_list[5].shown = True
                                    comp_list.append(card_list[5])
                                if area_num == 7:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[6].image, card_list[6].card_area)
                                    card_list[6].shown = True
                                    comp_list.append(card_list[6])
                                if area_num == 8:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[7].image, card_list[7].card_area)
                                    card_list[7].shown = True
                                    comp_list.append(card_list[7])
                                if area_num == 9:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[8].image, card_list[8].card_area)
                                    card_list[8].shown = True
                                    comp_list.append(card_list[8])
                                if area_num == 10:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[9].image, card_list[9].card_area)
                                    card_list[9].shown = True
                                    comp_list.append(card_list[9])
                                if area_num == 11:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[10].image, card_list[10].card_area)
                                    card_list[10].shown = True
                                    comp_list.append(card_list[10])
                                if area_num == 12:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[11].image, card_list[11].card_area)
                                    card_list[11].shown = True
                                    comp_list.append(card_list[11])
                                if area_num == 13:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[12].image, card_list[12].card_area)
                                    card_list[12].shown = True
                                    comp_list.append(card_list[12])
                                if area_num == 14:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[13].image, card_list[13].card_area)
                                    card_list[13].shown = True
                                    comp_list.append(card_list[13])
                                if area_num == 15:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[14].image, card_list[14].card_area)
                                    card_list[14].shown = True
                                    comp_list.append(card_list[14])
                                if area_num == 16:
                                    turn_sound.play()
                                    pygame.time.wait(300)
                                    screen.blit(card_list[15].image, card_list[15].card_area)
                                    card_list[15].shown = True
                                    comp_list.append(card_list[15])
                            else:
                                pass

        # exit game when all cards are flipped
        if card_left == 0:
            if score_player > score_ai:
                result = font_win.render("YOU WIN", False, red)
                win_sound.play()
            elif score_player == score_ai:
                result = font_draw.render("DRAW", False, blue)
                draw_sound.play()
            else:
                result = font_lose.render("YOU LOSE", False, black)
                lose_sound.play()
            result_rect = result.get_rect()
            result_rect.center = (width / 2, height / 2)
            screen.blit(result, result_rect)
            running = False

        pygame.display.flip()

    # end loop
    pygame.time.wait(5000)
    pygame.quit()
