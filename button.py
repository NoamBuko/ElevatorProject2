from settings import *
import pygame

class Button:
    def __init__(self, floor, x, y):
        self.floor = floor
        self.x_pixel = x
        self.y_pixel = y
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.color = 'black'

    
    # return the floor number if clicked, none otherwise
    def check_if_clicked(self, click_position): 
        if self.color != 'black': # this floor cannot recieve new calls at the moment, because the last call to this floor is still being carried out
            return None
        if click_position is not None: # this floor can recieve new calls 
            if click_position[0] in range(self.rect.left, self.rect.right) and click_position[1] in range(self.rect.top, self.rect.bottom):
                self.color = 'white'
                return self.floor
            else:
                return None
        return None
    

    # Draw the button on the screen 
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    
    # Functions for scrolling 
    def scroll_up(self):
        self.y_pixel -= VERTICAL_SCROLL_SPEED
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)

    def scroll_down(self):
        self.y_pixel += VERTICAL_SCROLL_SPEED
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)

    def scroll_left(self):
        self.x_pixel -= HORIZONTAL_SCROLL_SPEED
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)

    def scroll_right(self):
        self.x_pixel += HORIZONTAL_SCROLL_SPEED
        self.rect = pygame.Rect(self.x_pixel, self.y_pixel, BUTTON_WIDTH, BUTTON_HEIGHT)