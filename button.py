from settings import *
import pygame

class Button:
    def __init__(self, floor, x, y):
        self.floor = floor
        self.x_pixel = x
        self.y_pixel = y
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.color = 'black'

    
    def check_if_clicked(self, click_position): # return the floor number if clicked, none otherwise
        if self.color != 'black': # this floor cannot recieve new calls at the moment, because the last call to this floor is still being carried out
            return None
        if click_position is not None:
            if click_position[0] in range(self.rect.left, self.rect.right) and click_position[1] in range(self.rect.top, self.rect.bottom):
                self.color = 'white'
                return self.floor
            else:
                return None
        return None
    

    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

