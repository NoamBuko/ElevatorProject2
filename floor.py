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

         