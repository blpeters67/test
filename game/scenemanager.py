import pygame
from button import Button
from text import Text
class SceneManager:
    
    def __init__(self, app):
        self.app = app
        self.scenes = {}
        self.active_scene = None
        
        # for the vol control buttons
        self.buttons = [Button("minus", 1, False, (24, 160), [pygame.image.load("assets/textures/minus normal.png"), pygame.image.load("assets/textures/minus hovered.png"),pygame.image.load("assets/textures/minus selected.png")]), Button("plus", 1, False, (43, 160), [pygame.image.load("assets/textures/plus normal.png"), pygame.image.load("assets/textures/plus hovered.png"),pygame.image.load("assets/textures/plus selected.png"),]), Button("mute", 1, True, (5, 160), [pygame.image.load("assets/textures/mute normal.png"), pygame.image.load("assets/textures/mute hovered.png"), pygame.image.load("assets/textures/mute selected.png"), pygame.image.load("assets/textures/mute normal toggled.png"), pygame.image.load("assets/textures/mute hovered toggled.png"), pygame.image.load("assets/textures/mute selected toggled.png")])]
        self.volume_text = Text(-1, f"{self.app.music_player.volume*100}%", (0, 28, 69), 42, 154, True)
        self.button_last_hovered = ""
        self.button_counter = 0
        


    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def set_active_scene(self, name):
        self.active_scene = self.scenes[name]
        
    def handle_events(self, events):
        if self.active_scene.name in ["menu", "credits", "options"]:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    for button in self.buttons:
                        if button.rect.collidepoint(self.app.mouse_pos):
                            if button.name == "plus":
                                self.app.music_player.increase_volume()
                            elif button.name == "minus":
                                self.app.music_player.decrease_volume()
                            elif button.name == "mute":
                                self.app.music_player.mute()
                                button.toggle()
        
        # call the handle events method of the active scene
        self.active_scene.handle_events(events)

    def update(self):
        if self.active_scene.name in ["menu", "credits", "options"]:
            # handle changing a button's image when hovered or clicked
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
            
            # update the music player's text
            if 0 > self.app.music_player.volume:
                self.volume_text.text = "0%"
            else:
                self.volume_text.text = f"{self.app.music_player.volume*100:.0f}%"
            self.volume_text.update()

        # call the update method of the active scene
        self.active_scene.update()

    def draw(self):
        
        if self.active_scene.name in ["menu", "credits", "options"]:
            for button in self.buttons:
                button.draw(self.app.screen)

            self.volume_text.draw(self.app.screen)

        # call the draw method of the active scene
        self.active_scene.draw()