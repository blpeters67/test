import pygame
from text import Text
from button import Button

class Options:

    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.texts, self.buttons = self.load_options_data(1)
        self.button_last_hovered = ""
        
    def handle_events(self, events):
        
        # loop through game events that may or may not have happened
        for event in events:
            
            # detects left click being released and handles 
            # what happens when it is released on a button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for button in self.buttons:
                    if button.rect.collidepoint(self.app.mouse_pos):
                        if button.name == "1920x1080":
                            if self.app.screen.get_size() != (1920, 1080):
                                self.app.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.SCALED)
                        elif button.name == "1280x720":
                            if self.app.screen.get_size() != (1280, 720):
                                self.app.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
                        elif button.name == "640x480":
                            if self.app.screen.get_size() != (640, 480):
                                self.app.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE | pygame.SCALED)
                        elif button.name == "back":
                            self.app.scene_manager.set_active_scene("menu")

            # if a key was pressed by the player
            if event.type == pygame.KEYDOWN:
                
                # if that key was escape
                if event.key == pygame.K_ESCAPE:
                    self.app.scene_manager.set_active_scene("menu")

    def update(self):
        
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

        for button in self.buttons:
            button.draw(self.app.screen)

        for text in self.texts:
            text.draw(self.app.screen)

    def load_options_data(self, scale):
        
        button_normal = pygame.image.load("assets/textures/button normal.png").convert_alpha()
        button_hovered = pygame.image.load("assets/textures/button hovered.png").convert_alpha()
        button_pressed = pygame.image.load("assets/textures/button pressed.png").convert_alpha()
        buttons = []
        buttons.append(button_normal)
        buttons.append(button_hovered)
        buttons.append(button_pressed)
        fhd_button = Button("1920x1080", scale, False, (50, 50), buttons)
        hd_button = Button("1280x720", scale, False, (50, 66), buttons)
        hhd_button = Button("640x480", scale, False, (50, 82), buttons)
        back_button = Button("back", scale, False, (300, 4), [pygame.image.load("assets/textures/back normal.png"), pygame.image.load("assets/textures/back hovered.png"), pygame.image.load("assets/textures/back selected.png")])
        buttons.clear()
        buttons.append(fhd_button)
        buttons.append(hd_button)
        buttons.append(hhd_button)
        buttons.append(back_button)
 
        fhd_text = Text(-1, "1920x1080", (0,0,0), fhd_button.rect.centerx, fhd_button.rect.centery, True)
        hd_text = Text(-1, "1280x720", (0,0,0), hd_button.rect.centerx, hd_button.rect.centery, True)
        hhd_text = Text(-1, "640x480", (0,0,0), hhd_button.rect.centerx, hhd_button.rect.centery, True)
        resolution_text = Text(-1, "There's not a lot to see here, huh? :/", (0, 0, 0), 3, 0, False)
        texts = []
        texts.append(fhd_text)
        texts.append(hd_text)
        texts.append(hhd_text)
        texts.append(resolution_text)

        return texts, buttons