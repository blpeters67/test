import pygame
from text import Text
from button import Button
from decimal import Decimal


class Menu:
    
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.texts, self.buttons = self.load_main_menu_data()
        self.button_last_hovered = ""
        self.button_counter = 0
        
    def handle_events(self, events):

        # loop through game events that may or may not have happened
        for event in events:
            
            # if the player releases left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
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
        
        # POTENTIAL PROBLEM: this checks all buttons! so 
        # even if one button is pressed or hovered, the rest are
        # normal, therefore running the code under that else statement

        # PROBLEM: the hovered button sound effect does not play if you
        # hover over the button while holding down left click
        self.button_counter = 0
        for button in self.buttons:
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
        if self.button_counter == len(self.buttons):
            self.button_last_hovered = ""


    def draw(self):

        # draw the pixel art for the four buttons
        for button in self.buttons:
            button.draw(self.app.screen)
        
        # draw the text on the buttons
        for text in self.texts:
            text.draw(self.app.screen)

    def load_main_menu_data(self):
        button_normal = pygame.image.load("assets/textures/button normal.png").convert_alpha()
        button_hovered = pygame.image.load("assets/textures/button hovered.png").convert_alpha()
        button_pressed = pygame.image.load("assets/textures/button pressed.png").convert_alpha()
        buttons = []
        buttons.append(button_normal)
        buttons.append(button_hovered)
        buttons.append(button_pressed)
        play_button = Button("play", 1, False, (3, 3), buttons)
        options_button = Button("options", 1, False, (3, 19), buttons)
        credits_button = Button("credits", 1, False, (3, 35), buttons)
        quit_button = Button("quit", 1, False, (3, 51), buttons)
        buttons.clear()
        buttons.append(play_button)
        buttons.append(options_button)
        buttons.append(credits_button)
        buttons.append(quit_button)
        play_game_text = Text(-1, "Play Game", (0, 31, 88), play_button.rect.centerx, play_button.rect.centery-1, True)
        options_text = Text(-1, "Options", (0, 31, 88), options_button.rect.centerx, options_button.rect.centery-1, True)
        credits_text = Text(-1, "Credits", (0, 31, 88), credits_button.rect.centerx, credits_button.rect.centery-1, True) 
        quit_game_text = Text(-1, "Quit Game", (0, 31, 88), quit_button.rect.centerx, quit_button.rect.centery-1, True)
        texts = []
        texts.append(play_game_text)
        texts.append(options_text)
        texts.append(credits_text)
        texts.append(quit_game_text)
        return texts, buttons