import time
import pygame
from pygame import mixer
from settings import *
from timer import Timer # type: ignore

class Elevator:
    def __init__(self, number, x, y, speed) -> None: # name maybe not needed 
        self.name = number
        self.source_floor = 0 # if not moving - current, if in motion - source.
        self.destination_floor = None # in motion - destination
        self.trip_time = None # ( | source - dest | ) * SECONDS_BETWEEN_FLOORS
        self.queue = [] # list of next floors
        self.last_floor = 0 # if in rest - current, if in motion - the last floor in queue
        self.time_to_available = Timer(0) # in how many seconds will i finish the queue
        self.moving = False
        self.departure_time = 0 # if moving - departure time, if in rest - none
        self.direction = None # in rest - none, if moving - false for up, true for down
        self.current_x_pixel = x # assigned by building in beginning - does not change 
        self.start_trip_y_pixel = y # assigned by building in beginning - changes whenever i leave to new destination
        self.current_y_pixel = y
        self.speed = speed
        self.resting = False # if in rest - true
        self.rest_start_time = None # if in rest - holds start rest time 
        self.pic_up = pygame.image.load(ELEVATOR_PIC_UP)
        self.pic_up = pygame.transform.scale(self.pic_up, (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.pic_down = pygame.image.load(ELEVATOR_PIC_DOWN)
        self.pic_down = pygame.transform.scale(self.pic_down, (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.busy = False

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('/Users/noambooko/Desktop/python/ElevatorChallenge - Python/ding.mp3')


    
    # Take care of what happens when elv reaches destination (called by update func)
    def arrived_destination(self):
        # Take care of sound
        self.sound.play()
        
        # Start rest mode
        self.moving = False
        self.resting = True
        self.rest_start_time = time.time()


    # Called when the rest time is over
    def rest_over(self):
        if len(self.queue) == 0:
            self.busy = False
        else:
            self.new_trip(self.queue.pop(0))

    def new_trip(self, destination): # when calling this func, self.source is already set to where the elevator is now
        self.destination_floor = destination
        self.trip_time = (self.destination_floor - self.source_floor) * SECONDS_BETWEEN_FLOORS
        if self.trip_time < 0:
            self.trip_time *= -1
            self.direction = True # Going down 
        else:
            self.direction = False # Going up
        self.moving = True
        self.departure_time = time.time()
        self.start_trip_y_pixel = self.current_y_pixel
        self.resting = False

    
    # Update the position of the elevator, and update the time to available field 
    def update(self):
        
        current_time = time.time()
        # Update time to available
        self.time_to_available.update_timer()
    
        if not self.moving: # elevator is not moving
             if self.resting and current_time - self.rest_start_time >= 2: # if rest time is up
                    current_floor = self.destination_floor
                    self.rest_over()
                    return current_floor
        
        else: # elevator moving
            self.move()


    # function activated by the building, gives the elevator a destination floor, and the time to arrive to that destination
    def new_call(self, floor, time_to_floor): 
        if self.busy:
            self.queue.append(floor)
            time_to_available = time_to_floor + 2 # add trip_time and rest to self.time_to_available
            self.time_to_available = Timer(time_to_available)
        
        else:
            self.busy = True
            self.time_to_available = Timer(time_to_floor + 2)
            self.new_trip(floor)

        self.last_floor = floor
      
    def move(self):
        current_time = time.time()
        # update elevator height
        time_traveled = current_time - self.departure_time
        ground_traveled = time_traveled * self.speed
        if self.direction: # moving down
            self.current_y_pixel = self.start_trip_y_pixel + ground_traveled 
        else: # moving up 
            self.current_y_pixel = self.start_trip_y_pixel - ground_traveled

        # check if elevator reached destination
        if time_traveled >= self.trip_time:
            self.source_floor = self.destination_floor
            
            self.sound.play()
    
            self.moving = False
            self.resting = True
            self.rest_start_time = time.time()


    # Draw the elevator on the screen
    def draw(self, screen):
        if self.direction == True:
            screen.blit(self.pic_down, (self.current_x_pixel, self.current_y_pixel))

        else:
            screen.blit(self.pic_up, (self.current_x_pixel, self.current_y_pixel))


    # Function for scrolling
    def scroll_up(self):
        self.current_y_pixel -= VERTICAL_SCROLL_SPEED
        self.start_trip_y_pixel -= VERTICAL_SCROLL_SPEED


    def scroll_down(self):
        self.current_y_pixel += VERTICAL_SCROLL_SPEED
        self.start_trip_y_pixel += VERTICAL_SCROLL_SPEED

    def scroll_left(self):
        self.current_x_pixel -= HORIZONTAL_SCROLL_SPEED

    def scroll_right(self):
        self.current_x_pixel += HORIZONTAL_SCROLL_SPEED
