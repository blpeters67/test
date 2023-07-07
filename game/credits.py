import pygame, webbrowser
from text import Text
from button import Button

class Credits:
    
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.texts, self.buttons = self.load_credits_data()
        self.button_last_hovered = ""

    def handle_events(self, events):
        
        # loop through game events that may or may not have happened
        for event in events:
            
            # detects left click being released and handles 
            # what happens when it is released on a button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for button in self.buttons:
                    if button.rect.collidepoint(self.app.mouse_pos):
                        if button.name == "andrew soundcloud":
                            webbrowser.open("https://soundcloud.com/user-164551961")
                        elif button.name == "andrew youtube":
                            webbrowser.open("https://www.youtube.com/@amishpimpmusic")
                        elif button.name == "wayne soundcloud":
                            webbrowser.open("https://soundcloud.com/onebigparadox")
                        elif button.name == "wayne youtube":
                            webbrowser.open("https://www.youtube.com/channel/UCr33DbysJdX3_sDeUllmQQA")
                        elif button.name == "back":
                            self.app.scene_manager.set_active_scene("menu")
                        elif button.name == "plus":
                            self.app.music_player.increase_volume()
                        elif button.name == "minus":
                            self.app.music_player.decrease_volume()
                        elif button.name == "mute":
                            self.app.music_player.mute()

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
        
    def load_credits_data(self):
        soundcloud_button_images = [pygame.image.load("assets/textures/soundcloud normal.png"), pygame.image.load("assets/textures/soundcloud hovered.png"), pygame.image.load("assets/textures/soundcloud selected.png")]
        youtube_button_images = [pygame.image.load("assets/textures/youtube normal.png"), pygame.image.load("assets/textures/youtube hovered.png"), pygame.image.load("assets/textures/youtube selected.png")]
        soundcloud_button_1 = Button("andrew soundcloud", 1, False, (68, 115), soundcloud_button_images)
        youtube_button_1 = Button("andrew youtube", 1, False, (100, 115), youtube_button_images)
        soundcloud_button_2 = Button("wayne soundcloud", 1, False, (160, 70), soundcloud_button_images)
        youtube_button_2 = Button("wayne youtube", 1, False, (192, 70), youtube_button_images)
        back_button = Button("back", 1, False, (300, 4), [pygame.image.load("assets/textures/back normal.png"), pygame.image.load("assets/textures/back hovered.png"), pygame.image.load("assets/textures/back selected.png")])
        buttons = []
        buttons.append(soundcloud_button_1)
        buttons.append(soundcloud_button_2)
        buttons.append(youtube_button_1)
        buttons.append(youtube_button_2)
        buttons.append(back_button)
        music_by_andrew = Text(-1, "BGM by AmishPimp", (0, 0, 0), 36, 100, False)
        click_to_open = Text(-1, "Click an icon to open in browser!", (0, 0, 0), 3, 0, False)
        music_by_wayne = Text(-1, "and OneBigParadox!", (0, 0, 0), 130, 100, False)
        texts = []
        texts.append(music_by_andrew)
        texts.append(music_by_wayne)
        texts.append(click_to_open)
        return texts, buttons