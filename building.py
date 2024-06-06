import pygame
from settings import *
from floor import Floor
from elevator import Elevator
from button import Button
from timer import Timer # type: ignore
from gap import Gap


class Building:
    def __init__(self, number, floor_x): # not sure if list of elvs or num of elvs
        # init building according to num of floors and elvs, assign the speed for the elvs, and the pixels for each element
        pygame.init()

        self.vertical_scrolled = 0
        self.horizontal_scrolled = 0

        self.floor_x = floor_x

        self.number = number

        self.floor_num_font = pygame.font.SysFont(FLOOR_NUMBER_FONT, FLOOR_NUMBER_FONT_SIZE)

        self.list_of_floors = []
        self.list_of_elevators = []
        self.list_of_buttons = []
        self.list_of_gaps = []
        self.list_of_timers = []

        self.speed = self.calculate_speed()

        self.build_floors()
        self.build_elevators()
        self.add_gaps()
        self.add_buttons()

    def calculate_speed(self): # returns speed for elevators (pixels per seconds)
        pixels_per_floor = FLOOR_HEIGHT + GAP_HEIGHT
        speed = pixels_per_floor / SECONDS_BETWEEN_FLOORS
        return speed
    

    def build_floors(self): 
        x_pixel = self.floor_x # does not change for different floors
        y_pixel = SCREEN_HEIGHT - FLOOR_HEIGHT # does change for different floors
        for number in range(NUM_OF_FLOORS[self.number]):
            self.list_of_floors.append(Floor(number, x_pixel, y_pixel))
            y_pixel -= (GAP_HEIGHT + FLOOR_HEIGHT)
        


    def build_elevators(self):
        x_pixel = self.floor_x + FLOOR_WIDTH + PIXELS_BETWEEN_ELEVATOR # does change for different elevators
        y_pixel = SCREEN_HEIGHT - ELEVATOR_HEIGHT - GAP_HEIGHT # does not change for different elevators
        for number in range(NUM_OF_ELEVATORS[self.number]):
            self.list_of_elevators.append(Elevator(number, x_pixel, y_pixel, self.speed))
            x_pixel += (PIXELS_BETWEEN_ELEVATOR + ELEVATOR_WIDTH)
    

    def add_gaps(self):
        x_pixel = self.floor_x
        y_pixel = SCREEN_HEIGHT - FLOOR_HEIGHT - GAP_HEIGHT
        for gap in range(NUM_OF_FLOORS[self.number] - 1):
            self.list_of_gaps.append(Gap(x_pixel, y_pixel))
            y_pixel -= (GAP_HEIGHT + FLOOR_HEIGHT)
    

    def add_buttons(self):
        x_pixel = self.floor_x + (FLOOR_WIDTH - BUTTON_WIDTH) / 2 
        y_pixel = SCREEN_HEIGHT - FLOOR_HEIGHT + (FLOOR_HEIGHT - BUTTON_HEIGHT) / 2
        for number in range(NUM_OF_FLOORS[self.number]):
            self.list_of_buttons.append(Button(number, x_pixel, y_pixel))
            y_pixel -= (GAP_HEIGHT + FLOOR_HEIGHT)

    
    def add_floor_numbers(self, screen):
        for number in range(NUM_OF_FLOORS[self.number]):
            text_font = pygame.font.SysFont(FLOOR_NUMBER_FONT, FLOOR_NUMBER_FONT_SIZE)
            text = str(number)
            text_surface = text_font.render(text, True, FLOOR_NUMBER_COLOR)
            text_rect = text_surface.get_rect()
            text_rect.center = self.list_of_buttons[number].rect.center
            screen.blit(text_surface, text_rect)


    def check_for_new_calls(self, position):
        for button in self.list_of_buttons:
            result = button.check_if_clicked(position)
            if result is not None:
                self.call_elevator(result)
            
        return None
            

    def call_elevator(self, floor):
        arrival_times = []
        
        # check arrival time for each elevator and add it to the list
        for elevator in self.list_of_elevators:
            time_from_last_floor = abs(SECONDS_BETWEEN_FLOORS * (elevator.last_floor - floor))
            arrival_time = time_from_last_floor + elevator.time_to_available.seconds_left
            arrival_times.append((arrival_time, elevator))

        best_arrival = min(arrival_times, key=lambda x: x[0]) # stores a tuple
        time_to_arrival = best_arrival[0]
        best_elevator = best_arrival[1]

        self.list_of_timers.append(Timer(time_to_arrival, self.floor_x - TIMER_MARGIN + self.horizontal_scrolled, (SCREEN_HEIGHT - FLOOR_HEIGHT) - floor * (GAP_HEIGHT + FLOOR_HEIGHT) + self.vertical_scrolled))
        best_elevator.new_call(floor, time_to_arrival) 

        
    def update_all(self): # update all the objects -  elvs, timers, buttons
        for elevator in self.list_of_elevators:
            result = elevator.update() # result is either None, or a floor number if the button there should be changed back to black
            if result != None:
                self.list_of_buttons[result].color = 'black'
        
        for timer in self.list_of_timers:
            timer.update_timer()


    def draw_all(self, screen):   # draw everything just updated 
        for floor in self.list_of_floors:
            floor.draw(screen)
        
        for elevator in self.list_of_elevators:
            elevator.draw(screen)
        
        for button in self.list_of_buttons:
            button.draw(screen)

        for gap in self.list_of_gaps:
            gap.draw(screen)

        for timer in self.list_of_timers:
            timer.plot(screen)

        self.add_floor_numbers(screen)

    def scroll_up_all(self):
        self.vertical_scrolled -= VERTICAL_SCROLL_SPEED

        for gap in self.list_of_gaps:
            gap.scroll_up()
            
        for elevator in self.list_of_elevators:
                elevator.scroll_up()

        for floor in self.list_of_floors:
                floor.scroll_up()
            
        for button in self.list_of_buttons:
                button.scroll_up()

        for timer in self.list_of_timers:
                timer.scroll_up()


    def scroll_down_all(self):
        self.vertical_scrolled += VERTICAL_SCROLL_SPEED

        for gap in self.list_of_gaps:
            gap.scroll_down()
        
        for elevator in self.list_of_elevators:
            elevator.scroll_down()

        for floor in self.list_of_floors:
            floor.scroll_down()
        
        for button in self.list_of_buttons:
            button.scroll_down()

        for timer in self.list_of_timers:
            timer.scroll_down()

    def scroll_left_all(self):
        self.horizontal_scrolled -= HORIZONTAL_SCROLL_SPEED

        for gap in self.list_of_gaps:
            gap.scroll_left()
        
        for elevator in self.list_of_elevators:
            elevator.scroll_left()

        for floor in self.list_of_floors:
            floor.scroll_left()
        
        for button in self.list_of_buttons:
            button.scroll_left()

        for timer in self.list_of_timers:
            timer.scroll_left()

    def scroll_right_all(self):
        self.horizontal_scrolled += HORIZONTAL_SCROLL_SPEED

        for gap in self.list_of_gaps:
            gap.scroll_right()
        
        for elevator in self.list_of_elevators:
            elevator.scroll_right()

        for floor in self.list_of_floors:
            floor.scroll_right()
        
        for button in self.list_of_buttons:
            button.scroll_right()

        for timer in self.list_of_timers:
            timer.scroll_right()
                     