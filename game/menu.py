import pygame
from text import Text
from button import Button


class Menu:
    
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.texts, self.buttons = self.load_main_menu_data(1)
        
    def handle_events(self, events):

        # loop through game events that may or may not have happened
        for event in events:
            
            # if the player releases left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.app.lmb_down = False
                for button in self.buttons:
                    if button.rect.collidepoint(self.app.mouse_pos):
                        if button.name == "quit":
                            self.app.running = False
                        elif button.name == "play":
                            self.app.scene_manager.set_active_scene("game")
                        elif button.name == "options":
                            self.app.scene_manager.set_active_scene("options")
                        elif button.name == "credits":
                            self.app.scene_manager.set_active_scene("credits")

    def update(self):
        
        # Q: Why is this not in handle_events()?
        # A: self.app gets lmb_down and mouse_pos which
        # is all this code block needs to update the buttons
        for button in self.buttons:
            if button.rect.collidepoint(self.app.mouse_pos) and self.app.lmb_down:
                button.button_selected()
            elif button.rect.collidepoint(self.app.mouse_pos) and not self.app.lmb_down:
                button.button_hovered()
            else:
                button.button_normal()

    def draw(self):

        # draw the pixel art for the four buttons
        for button in self.buttons:
            button.draw(self.app.screen)
        
        # draw the text on the buttons
        for text in self.texts:
            text.draw(self.app.screen)

    def load_main_menu_data(self, scale):
        button_normal = pygame.image.load("assets/textures/button normal.png").convert_alpha()
        button_hovered = pygame.image.load("assets/textures/button hovered.png").convert_alpha()
        button_pressed = pygame.image.load("assets/textures/button pressed.png").convert_alpha()
        buttons = []
        buttons.append(button_normal)
        buttons.append(button_hovered)
        buttons.append(button_pressed)
        play_button = Button("play", scale, False, (3, 3), buttons)
        options_button = Button("options", scale, False, (3, 20), buttons)
        credits_button = Button("credits", scale, False, (3, 36), buttons)
        quit_button = Button("quit", scale, False, (3, 52), buttons)
        buttons.clear()
        buttons.append(play_button)
        buttons.append(options_button)
        buttons.append(credits_button)
        buttons.append(quit_button)
        play_game_text = Text(-1, "Play Game", (0, 0, 0), self.app.screen, play_button.rect.centerx, play_button.rect.centery-1, True)
        options_text = Text(-1, "Options", (0, 0, 0), self.app.screen, options_button.rect.centerx, options_button.rect.centery-1, True)
        credits_text = Text(-1, "Credits", (0, 0, 0), self.app.screen, credits_button.rect.centerx, credits_button.rect.centery-1, True) 
        quit_game_text = Text(-1, "Quit Game", (0, 0, 0), self.app.screen, quit_button.rect.centerx, quit_button.rect.centery-1, True)
        texts = []
        texts.append(play_game_text)
        texts.append(options_text)
        texts.append(credits_text)
        texts.append(quit_game_text)
        return texts, buttons