import pygame, sys
from scenemanager import SceneManager
from musicplayer import MusicPlayer
from menu import Menu
from game import Game
from options import Options
from credits import Credits
from sfxplayer import SFXPlayer

class App:
   
    def __init__(self):
        pygame.init()
        self.width = 320
        self.height = 180
        self.flags = pygame.SCALED | pygame.RESIZABLE
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        game_icon = pygame.image.load("assets/textures/cobblestone.png").convert()
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption("Extremely Cool Game")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        self.running = True
        self.lmb_down = False
        self.fullscreen = False
        
        # the scene manager keeps track of which scene
        # is current active and therefore knows which
        # scene's methods to run
        self.sfx_player = SFXPlayer()
        self.music_player = MusicPlayer()
        self.scene_manager = SceneManager(self)
        self.menu = Menu("menu", self)
        self.game = Game("game", self)
        self.options = Options("options", self)
        self.credits = Credits("credits", self)
        self.scene_manager.add_scene(self.menu)
        self.scene_manager.add_scene(self.game)
        self.scene_manager.add_scene(self.options)
        self.scene_manager.add_scene(self.credits)
        self.scene_manager.set_active_scene("menu")
        
    def handle_events(self):
        events = pygame.event.get()
        self.mouse_pos = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.lmb_down = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.lmb_down = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if not self.fullscreen:
                    self.fullscreen = True
                    pygame.display.toggle_fullscreen()
                else:
                    self.fullscreen = False
                    pygame.display.toggle_fullscreen()

            
        self.scene_manager.handle_events(events)

    def update(self):
        self.music_player.update()
        self.scene_manager.update()

    def draw(self):
        self.screen.fill((255, 255, 224))
        self.scene_manager.draw()
        pygame.display.flip()
        
    def quit(self):
        pygame.quit()
        sys.exit()
        

    def run(self):
        while self.running:
            self.dt = self.clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.update()
            self.draw()
        self.quit()
        
app = App()
app.run()