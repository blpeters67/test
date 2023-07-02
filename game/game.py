import pygame
from text import Text
from button import Button
from random import randint

class Game():
   
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.paused = False
        self.texts, self.money, self.human_readable_mps, self.mpc = self.load_game_data()
        self.pause_texts, self.pause_buttons, self.pause_menu = self.load_pause_menu_data()


    def draw(self):

        for text in self.texts:
            text.draw(self.app.screen)

        if self.paused:
            self.app.screen.blit(self.pause_menu, (100, 140))
            for button in self.pause_buttons:
                button.draw(self.app.screen)
            # draw the text on the buttons
            for text in self.pause_texts:
                text.draw(self.app.screen)

    def update(self):
        
        # increment the money if game not paused; this is the money gained per second!
        if not self.paused:
            self.money += self.human_readable_mps/self.app.fps

        # update text and durations and stuff
        self.texts = [text for text in self.texts if text.duration > 0 or text.duration == -1]
        self.texts[1].text = f"${self.money:,.0f}"
        self.texts[3].text = f"${self.human_readable_mps:,.0f}"
        self.texts[5].text = f"${self.mpc:,.0f}"

        for text in self.texts:
            if text.duration == 0:
                del text
        print(len(self.texts))


        # handle changing a (pause) button's image when hovered or clicked
        if self.paused:
            for button in self.pause_buttons:
                if button.rect.collidepoint(self.app.mouse_pos) and self.app.lmb_down:
                    button.button_selected()
                elif button.rect.collidepoint(self.app.mouse_pos) and not self.app.lmb_down:
                    button.button_hovered()
                else:
                    button.button_normal()

    def handle_events(self, events):
    
        # loop through game events that may or may not have happened
        for event in events:
            
            # if a key was pressed by the player
            if event.type == pygame.KEYDOWN:
                
                # if that key was escape
                if event.key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.paused = True
                    else:
                        self.paused = False

                # if that key was the space bar
                elif event.key == pygame.K_SPACE and not self.paused:
                    click_money = Text(self.app.fps, f'+${self.mpc:,.0f}', (51, 204, 51), self.app.screen, randint(50,800), randint(100,500), False)
                    self.texts.append(click_money)
                    self.money += self.mpc

            # detects left click being released and handles what
            # happens when it is released on a pause screen button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.paused == True:
                    for button in self.pause_buttons:
                        if button.rect.collidepoint(self.app.mouse_pos):
                            if button.name == "resume":
                                self.paused = False
                            elif button.name == "options":
                                self.app.scene_manager.set_active_scene("options")
                            elif button.name == "menu":
                                self.paused = False
                                self.texts = [text for text in self.texts if text.text != f'+${self.mpc:,.0f}']
                                self.app.scene_manager.set_active_scene("menu")
                            elif button.name == "quit":
                                self.save_game_data()
                                self.app.running = False

    def load_game_data(self):
        f = open("save.txt", "r").readlines()
        try:
            money = int(f[0][f[0].find("|")+1:].rstrip("\n"))
        except:
            money = float(f[0][f[0].find("|")+1:].rstrip("\n"))
        try:
            human_readable_mps = int(f[1][f[1].find("|")+1:].rstrip("\n"))
        except:
            human_readable_mps = float(f[1][f[1].find("|")+1:].rstrip("\n"))
        try:
            mpc = int(f[2][f[2].find("|")+1:].rstrip("\n"))
        except:
            mpc = float(f[2][f[2].find("|")+1:].rstrip("\n"))
        current_balance_text = Text(-1, "Current balance:", (255, 255, 255), self.app.screen, 10, 3, False)
        current_money_text = Text(-1, f'${money:,.0f}', (102, 255, 102), self.app.screen, 233, 3, False)
        per_second_text = Text(-1, f'Per second:', (255, 255, 255), self.app.screen, 10, 33, False)
        mps_text = Text(-1, human_readable_mps, (51, 204, 51), self.app.screen, 170, 33, False)
        money_per_spacebar_press_text = Text(-1, f'Per space bar press:', (255, 255, 255), self.app.screen, 10, 63, False)
        money_gained_per_spacebar_press_text = Text(-1, mpc, (51, 204, 51), self.app.screen, 298, 63, False)
        texts = []
        texts.append(current_balance_text) # 0
        texts.append(current_money_text) # 1
        texts.append(per_second_text) # 2
        texts.append(mps_text) # 3
        texts.append(money_per_spacebar_press_text) # 4
        texts.append(money_gained_per_spacebar_press_text) # 5
        return texts, money, human_readable_mps, mpc
    

    def load_pause_menu_data(self):
        
        button_normal = pygame.image.load("assets/textures/button normal.png").convert_alpha()
        button_hovered = pygame.image.load("assets/textures/button hovered.png").convert_alpha()
        button_pressed = pygame.image.load("assets/textures/button pressed.png").convert_alpha()
        buttons = []
        buttons.append(button_normal)
        buttons.append(button_hovered)
        buttons.append(button_pressed)
        pause_menu = pygame.image.load("assets/textures/pause menu.png").convert_alpha()
        # create the five buttons
        button_images = [buttons[0], buttons[1], buttons[2]]
        resume_game_button = Button("resume", 4, False, (112, 152), button_images)
        options_button = Button("options", 4, False, (112, 204), button_images)
        main_menu_button = Button("menu", 4, False, (112, 256), button_images)
        save_and_quit_button = Button("quit", 4, False, (112, 308), button_images)
        buttons[0] = resume_game_button
        buttons[1] = options_button
        buttons[2] = main_menu_button
        buttons.append(save_and_quit_button)
        pause_menu = pygame.transform.scale_by(pause_menu, 4)
        
        resume_game_text = Text(-1, "Resume Game", (0, 0, 0), self.app.screen, resume_game_button.rect.centerx, resume_game_button.rect.centery-2, True)
        options_text = Text(-1, "Options", (0, 0, 0), self.app.screen, options_button.rect.centerx, options_button.rect.centery-2, True)
        main_menu_text = Text(-1, "Main Menu", (0, 0, 0), self.app.screen, main_menu_button.rect.centerx, main_menu_button.rect.centery-2, True) 
        save_and_quit_text = Text(-1, "Save and Quit", (0, 0, 0), self.app.screen, save_and_quit_button.rect.centerx, save_and_quit_button.rect.centery-2, True)
        texts = []
        texts.append(resume_game_text)
        texts.append(options_text)
        texts.append(main_menu_text)
        texts.append(save_and_quit_text)

        return texts, buttons, pause_menu