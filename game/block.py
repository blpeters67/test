class Block:
    
    def __init__(self, name, pos, screen, breaking_overlays, cobblestone):
        
        self.starting_hp = 10
        self.hp = 10
        self.pos = pos
        self.screen = screen
        self.breaking_overlay = None
        self.percent_hp_left = 100
        self.breaking_overlays = breaking_overlays
        self.cobblestone = cobblestone
        self.name = name
        self.block_image = cobblestone
        self.block_rect = cobblestone.get_rect(topleft = self.pos)

    def update(self):
        self.percent_hp_left = (self.hp/self.starting_hp)*100
        print(self.percent_hp_left)
        if 90 < self.percent_hp_left:
            pass
            print('nothing happened')
        elif self.percent_hp_left <= 90 and self.percent_hp_left > 80:
            self.breaking_overlay = self.breaking_overlays[0]
            print("0") # debug
        elif self.percent_hp_left <= 80 and self.percent_hp_left > 70:
            self.breaking_overlay = self.breaking_overlays[1]
            print("1") # debug
        elif self.percent_hp_left <= 70 and self.percent_hp_left > 60:
            self.breaking_overlay = self.breaking_overlays[2]
            print("2") # debug
        elif self.percent_hp_left <= 60 and self.percent_hp_left > 50:
            self.breaking_overlay = self.breaking_overlays[3]
            print("3") # debug
        elif self.percent_hp_left <= 50 and self.percent_hp_left > 40:
            self.breaking_overlay = self.breaking_overlays[4]
            print("4") # debug
        elif self.percent_hp_left <= 40 and self.percent_hp_left > 30:
            self.breaking_overlay = self.breaking_overlays[5]
            print("5") # debug
        elif self.percent_hp_left <= 30 and self.percent_hp_left > 20:
            self.breaking_overlay = self.breaking_overlays[6]
            print("6") # debug
        elif self.percent_hp_left <= 20 and self.percent_hp_left > 10:
            self.breaking_overlay = self.breaking_overlays[7]
            print("7") # debug
        else:
            self.breaking_overlay = self.breaking_overlays[8]
            print("8") # debug


    def draw(self):
        self.screen.blit(self.block_image, self.block_rect)
        if self.breaking_overlay != None:
            self.screen.blit(self.breaking_overlay, self.pos)