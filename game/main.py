import pygame, sys
from text import Text
from scenemanager import SceneManager

from menu import Menu
from game import Game
from options import Options
from credits import Credits

class Controller:
   
    def __init__(self):
        pygame.init()

        self.width = 320
        self.height = 180
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.SCALED | pygame.FULLSCREEN)
        game_icon = pygame.image.load("assets/textures/cobblestone.png").convert()
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption("Extremely Cool Game")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.fps_overlay_text = Text(-1, "FPS: ", (255, 255, 255), self.screen, 10, self.height-3, False)
        
        self.running = True
        self.lmb_down = False

        # start the music player for the bg music
        pygame.mixer.music.load("assets/audio/idle.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0)

        # the scene manager keeps track of which scene
        # is current active and therefore knows which
        # scene's methods to run
        self.scene_manager = SceneManager(self)
        self.scene_manager.add_scene(Menu("menu", self))
        self.scene_manager.add_scene(Game("game", self))
        self.scene_manager.add_scene(Options("options", self))
        self.scene_manager.add_scene(Credits("credits", self))
        self.scene_manager.set_active_scene("menu")
        
    def handle_events(self):
        events = pygame.event.get()
        self.mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.lmb_down = True
            if event.type == pygame.VIDEORESIZE:
                # Update the window dimensions
                self.width = event.w
                self.height = event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        self.scene_manager.handle_events(events)

    def update(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        self.scene_manager.update()

    def draw(self):
        self.screen.fill((255, 255, 224))
        self.scene_manager.draw()
        self.fps_overlay_text.draw(self.screen)
        pygame.display.flip()
        
    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.running:
            self.delta_time = self.clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.update()
            self.draw()
        self.quit()
        

controller = Controller()
controller.run()