import pygame, webbrowser
from text import Text
from button import Button

class Credits:
    
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.texts, self.buttons = self.load_credits_data()

    def handle_events(self, events):
        
        # loop through game events that may or may not have happened
        for event in events:
            
            # detects left click being released and handles 
            # what happens when it is released on a button
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for button in self.buttons:
                    if button.rect.collidepoint(self.app.mouse_pos):
                        if button.name == "soundcloud":
                            webbrowser.open("https://soundcloud.com/user-164551961")
                        elif button.name == "youtube":
                            webbrowser.open("https://www.youtube.com/@amishpimpmusic")
                        elif button.name == "back":
                            self.app.scene_manager.set_active_scene("menu")

            # if a key was pressed by the player
            if event.type == pygame.KEYDOWN:
                
                # if that key was escape
                if event.key == pygame.K_ESCAPE:
                    self.app.scene_manager.set_active_scene("menu")

    def update(self):
        
        # handle changing a button's image when hovered or clicked
        for button in self.buttons:
            if button.rect.collidepoint(self.app.mouse_pos) and self.app.lmb_down:
                button.button_selected()
            elif button.rect.collidepoint(self.app.mouse_pos) and not self.app.lmb_down:
                button.button_hovered()
            else:
                button.button_normal()

    def draw(self):

        for button in self.buttons:
            button.draw(self.app.screen)

        for text in self.texts:
            text.draw(self.app.screen)
        
    def load_credits_data(self):
        music_by = Text(-1, "Music by AmishPimp", (255, 255, 255), self.app.screen, 50, 210, False)
        click_to_open = Text(-1, "Click an icon to open in browser!", (255, 255, 255), self.app.screen, 10, 3, False)
        texts = []
        texts.append(music_by)
        texts.append(click_to_open)
        # name, scale, toggleable, position, button_images
        soundcloud_button = Button("soundcloud", 4, False, (50, 90), [pygame.image.load("assets/textures/soundcloud normal.png"), pygame.image.load("assets/textures/soundcloud hovered.png"), pygame.image.load("assets/textures/soundcloud selected.png")])
        youtube_button = Button("youtube", 4, False, (180, 90), [pygame.image.load("assets/textures/youtube normal.png"), pygame.image.load("assets/textures/youtube hovered.png"), pygame.image.load("assets/textures/youtube selected.png")])
        back_button = Button("back", 4, False, (880, 17), [pygame.image.load("assets/textures/back normal.png"), pygame.image.load("assets/textures/back hovered.png"), pygame.image.load("assets/textures/back selected.png")])
        buttons = []
        buttons.append(soundcloud_button)
        buttons.append(youtube_button)
        buttons.append(back_button)
        return texts, buttons