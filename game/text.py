import pygame
class Text:

    def __init__(self, duration: int, text: str, color: tuple, screen: object, x: int, y: int, centered: bool):
        self.duration = duration # how long the text is on screen
        self.text = text # what the text says
        self.color = color # color of the text
        self.x = x # x pos of the text
        self.y = y # y pos of the text
        self.centered = centered # decides whether to place the text centered or whatever
        
        self.font = pygame.font.Font("EXEPixelPerfect.ttf", 16)

    def draw(self, screen):
        if self.duration != 0:
            if self.duration != -1:
                self.duration -= 1
                for each in self.color:
                    each -= 10
            textobj = self.font.render(self.text, False, self.color)
            textrect = textobj.get_rect()
            if self.centered == True:
                textrect.center = (self.x, self.y)
            else:
                textrect.topleft = (self.x, self.y)
            screen.blit(textobj, textrect)
        else:
            pass