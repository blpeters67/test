class SceneManager:
    
    def __init__(self, controller):
        self.controller = controller
        self.scenes = {}
        self.active_scene = None

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def set_active_scene(self, name):
        self.active_scene = self.scenes[name]

    def handle_events(self, events):
        if self.active_scene is not None:
            self.active_scene.handle_events(events)

    def update(self):
        if self.active_scene is not None:
            self.active_scene.update()

    def draw(self):
        if self.active_scene is not None:
            self.active_scene.draw()