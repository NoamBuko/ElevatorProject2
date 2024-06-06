import time
from settings import *
import pygame 

class Timer:
    def __init__(self, seconds, x = None, y = None):
        pygame.init()
        self.start_time = time.time()
        self.seconds_at_start = seconds # stores the amount of seconds the timer was called for
        self.seconds_left = float(seconds) # float - so that the plot function can work properly
        self.x_pixel = x
        self.y_pixel = y
        self.text_font = pygame.font.SysFont(TIMER_FONT, TIMER_FONT_SIZE)

    # update the seconds left on the timer 
    def update_timer(self): 
        if self.seconds_left > 0:
            current_time = time.time()
            time_past = current_time - self.start_time
            self.seconds_left = self.seconds_at_start - time_past


    # put the timer on the screen - if there is more than 1 second left 
    def plot(self, screen):
        if self.seconds_left > 0:
            integer_part, decimal_part = str(self.seconds_left).split('.')
            time_left = integer_part + '.' + decimal_part[:1] # now only has first 2 numbers after the decimal point
            img = self.text_font.render(time_left, True, TIMER_FONT_COLOR)
            screen.blit(img, (self.x_pixel, self.y_pixel))

    
    # functions for scrolling
    def scroll_up(self):
        self.y_pixel -= VERTICAL_SCROLL_SPEED

    def scroll_down(self):
        self.y_pixel += VERTICAL_SCROLL_SPEED

    def scroll_left(self):
        self.x_pixel -= HORIZONTAL_SCROLL_SPEED

    def scroll_right(self):
        self.x_pixel += HORIZONTAL_SCROLL_SPEED
                     
    
