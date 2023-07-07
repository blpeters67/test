import pygame

class Text:

    def __init__(self, duration: int, text: str, color: tuple, x: int, y: int, centered: bool):
        self.opacity = 255
        self.font = pygame.font.Font("EXEPixelPerfect.ttf", 16)
        self.duration = duration # how long the text is on screen
        self.text = text # what the text says
        self.color = color # color of the text
        self.x = x # x pos of the text
        self.y = y # y pos of the text
        self.centered = centered # decides whether to place the text centered or whatever
        self.textobj = self.font.render(self.text, False, self.color)
        self.textrect = self.textobj.get_rect()
        
    def draw(self, screen):
        if self.centered == True:
            self.textrect.center = (self.x, self.y)
        else:
            self.textrect.topleft = (self.x, self.y)
        screen.blit(self.textobj, self.textrect)

    def update(self):
        self.textobj = self.font.render(self.text, False, self.color)
        self.textrect = self.textobj.get_rect()