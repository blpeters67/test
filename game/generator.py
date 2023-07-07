from block import Block

class Generator():
    
    def __init__(self, pos, screen, cobblestone, breaking_overlays):
        
        self.speed = 3
        self.pos = pos
        self.screen = screen
        self.cobblestone = cobblestone
        self.breaking_overlays = breaking_overlays
        self.block = Block("cobblestone", self.pos, self.screen, self.breaking_overlays, self.cobblestone)
        self.timer = 0
        self.dt = 0
        self.block_broken = False
        
        
    def update(self):
        if self.block_broken == True:
            self.timer += self.dt
            print(f"block broken. here's the timer: {self.timer}")
            if self.timer >= self.speed:
                self.timer = 0
                self.generate_block()

    
    def draw(self):
        if not self.block_broken:
            self.block.draw()
    

    def break_block(self):
        self.block_broken = True
        del self.block

    
    def generate_block(self):
        self.block_broken = False
        self.block = Block("cobblestone", self.pos, self.screen, self.breaking_overlays, self.cobblestone)