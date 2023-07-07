import pygame
from text import Text
from button import Button
from pickaxe import Pickaxe
from generatormanager import GeneratorManager

def get_color_palette(surface, exclude):
    array = pygame.PixelArray(surface)
    colors = {tuple(surface.unmap_rgb(mapped_color)) for row in array for mapped_color in row}

    if exclude:
        return [color for color in colors if color not in exclude]

    return list(colors)

class Game():
   
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.paused = False
        self.money, self.money_text = self.load_game_data()
        self.human_legible_money = ""
        self.button_last_hovered = ""
        self.pause_texts, self.pause_buttons, self.pause_menu = self.load_pause_menu_data()
        self.pickaxe = Pickaxe()
        self.generator_manager = GeneratorManager(self.app)
        self.generator_manager.add_generator((3, 145))
        self.generator_manager.add_generator((38, 145))
        self.generator_manager.add_generator((73, 145))


    def draw(self):

        self.money_text.draw(self.app.screen)
        
        self.generator_manager.draw()

        if self.paused:
            self.app.screen.blit(self.pause_menu, ((self.app.width/2)-35, (self.app.height/2)-38))
            for button in self.pause_buttons:
                button.draw(self.app.screen)
            # draw the text on the buttons
            for text in self.pause_texts:
                text.draw(self.app.screen)


    def update(self):

        self.human_legible_money = self.format_money()

        # update text and durations and stuff
        self.money_text.text = f'{self.human_legible_money}'
        self.money_text.update()

        # handle changing a (pause) button's image when hovered or clicked
        if self.paused:
            self.button_counter = 0
            for button in self.pause_buttons:
                if button.rect.collidepoint(self.app.mouse_pos) and self.app.lmb_down:
                    if self.button_last_hovered != button.name:
                        self.button_last_hovered = button.name
                        self.app.sfx_player.button_hovered.play()
                    button.button_selected()
                elif button.rect.collidepoint(self.app.mouse_pos) and not self.app.lmb_down:
                    button.button_hovered()
                    if self.button_last_hovered != button.name:
                        self.button_last_hovered = button.name
                        self.app.sfx_player.button_hovered.play()
                else:
                    button.button_normal()
                    self.button_counter += 1
            if self.button_counter == len(self.pause_buttons):
                self.button_last_hovered = ""

        self.generator_manager.update()

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
                    self.money += 1

            # detects left click being released and handles what
            # happens when it is released on a pause screen button
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.paused == True:
                    for button in self.pause_buttons:
                        if button.rect.collidepoint(self.app.mouse_pos):
                            if button.name == "resume":
                                self.paused = False
                            elif button.name == "options":
                                self.paused = False
                                self.app.scene_manager.set_active_scene("options")
                            elif button.name == "menu":
                                self.paused = False
                                self.app.scene_manager.set_active_scene("menu")
                            elif button.name == "quit":
                                self.save_game_data()
                                self.app.running = False

        self.generator_manager.handle_events(events)

            


    def load_game_data(self):
        f = open("save.txt", "r").readlines()
        try:
            money = int(f[0][f[0].find("|")+1:].rstrip("\n"))
        except:
            money = float(f[0][f[0].find("|")+1:].rstrip("\n"))
        money_text = Text(-1, f'${money:,.0f}', (51, 204, 51), 3, 0, False)
        return money, money_text
    

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
        resume_game_button = Button("resume", 1, False, (129, 57), button_images)
        options_button = Button("options", 1, False, (129, 75), button_images)
        main_menu_button = Button("menu", 1, False, (129, 93), button_images)
        save_and_quit_button = Button("quit", 1, False, (129, 111), button_images)
        buttons[0] = resume_game_button
        buttons[1] = options_button
        buttons[2] = main_menu_button
        buttons.append(save_and_quit_button)
        
        resume_game_text = Text(-1, "Resume", (0, 31, 88), resume_game_button.rect.centerx, resume_game_button.rect.centery-1, True)
        options_text = Text(-1, "Options", (0, 31, 88), options_button.rect.centerx, options_button.rect.centery-1, True)
        main_menu_text = Text(-1, "Main Menu", (0, 31, 88), main_menu_button.rect.centerx, main_menu_button.rect.centery-1, True) 
        save_and_quit_text = Text(-1, "Exit Game", (0, 31, 88), save_and_quit_button.rect.centerx, save_and_quit_button.rect.centery-1, True)
        texts = []
        texts.append(resume_game_text)
        texts.append(options_text)
        texts.append(main_menu_text)
        texts.append(save_and_quit_text)

        return texts, buttons, pause_menu
    
    def format_money(self):
        # make the money human-legible
        if self.money >= 1000000000000:
            human_legible_money = f"${self.money/1000000000000:.2f}T"
        elif self.money >= 1000000000:
            human_legible_money = f"${self.money/1000000000:.2f}B"
        elif self.money >= 1000000:
            human_legible_money = f"${self.money/1000000:.2f}M"
        elif self.money >= 1000:
            human_legible_money = f"${self.money/1000:.2f}K"
        else:
            human_legible_money = f"${self.money:.0f}"
        return human_legible_money