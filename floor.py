import pygame
from settings import *

class Floor:
    def __init__(self, number, x, y) -> None:
        self.number = number
        self.waiting = False
        self.x_pixel = x
        self.y_pixel = y
        self.pic = pygame.image.load(FLOOR_PIC)
        self.pic = pygame.transform.scale(self.pic, (FLOOR_WIDTH, FLOOR_HEIGHT))
    

    def draw(self, screen):
        screen.blit(self.pic, (self.x_pixel, self.y_pixel))

    
    def scroll_up(self):
        self.y_pixel -= VERTICAL_SCROLL_SPEED

    def scroll_down(self):
        self.y_pixel += VERTICAL_SCROLL_SPEED

    def scroll_left(self):
        self.x_pixel -= HORIZONTAL_SCROLL_SPEED

    def scroll_right(self):
        self.x_pixel += HORIZONTAL_SCROLL_SPEED


         