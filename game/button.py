import pygame


class Button:
    

    # constructor
    def __init__(self, name: str, scale: int, toggleable: bool, position: tuple, button_images: list):

        # initialize some stuff
        self.normal = button_images[0]
        self.hovered = button_images[1]
        self.selected = button_images[2]
        self.name = name
        self.toggleable = toggleable
        
        # scale the images if a number was given
        if scale != None and scale != 1:
            self.normal = pygame.transform.scale_by(self.normal, scale)
            self.hovered = pygame.transform.scale_by(self.hovered, scale)
            self.selected = pygame.transform.scale_by(self.selected, scale)

        # initialize the toggleable button images
        if toggleable:
            self.toggled = False
            self.toggled_normal = button_images[3]
            self.toggled_hovered = button_images[4]
            self.toggled_selected = button_images[5]
            # scale the toggleable button images if a number was given
            if scale != None:
                print('scaling toggled buttons')
                self.toggled_normal = pygame.transform.scale_by(self.toggled_normal, scale)
                self.toggled_hovered = pygame.transform.scale_by(self.toggled_hovered, scale)
                self.toggled_selected = pygame.transform.scale_by(self.toggled_selected, scale)


        # make a rect based off of the normal button image
        self.current_image = self.normal
        self.rect = self.current_image.get_rect(topleft = (position[0], position[1])) 
        
        
    # change the button's image to a hovered state
    def button_hovered(self):
        if not self.toggleable:
            self.current_image = self.hovered
        else:
            if self.toggled:
                self.current_image = self.toggled_hovered
            else:
                self.current_image = self.hovered


    # change the button's image to a selected state
    def button_selected(self):
        if not self.toggleable:
            self.current_image = self.selected
        else:
            if self.toggled:
                self.current_image = self.toggled_selected
            else:
                self.current_image = self.selected


    # change the button's image to its normal state
    def button_normal(self):
        if not self.toggleable:
            self.current_image = self.normal
        else:
            if self.toggled:
                self.current_image = self.toggled_normal
            else:
                self.current_image = self.normal

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)