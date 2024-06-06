import pygame
from settings import *
from floor import Floor
from elevator import Elevator
from button import Button
from timer import Timer # type: ignore
from building import Building

class City:
    def __init__(self):
        self.list_of_buildings = []
        self.start_building = FLOOR_MARGIN # where each building should start 

        self.create_buildings()
    
    # Create buildings in the city
    def create_buildings(self):
        for number in range(NUM_OF_BUILDINGS):
            self.list_of_buildings.append(Building(number, self.start_building))
            self.start_building += (FLOOR_MARGIN + NUM_OF_ELEVATORS[number] * (ELEVATOR_WIDTH + PIXELS_BETWEEN_ELEVATOR) + FLOOR_WIDTH)

    # Update all the objects in the city
    def update_all(self):
        for building in self.list_of_buildings:
            building.update_all()
    

    # Draw all the objects in the city
    def draw_all(self, screen):
        for building in self.list_of_buildings:
            building.draw_all(screen)

    
    # Idenftify new calls from floors 
    def check_for_new_calls(self, position):
        for building in self.list_of_buildings:
            building.check_for_new_calls(position)

    
    # Functions for scrolling 
    def scroll_down_all(self):
        for building in self.list_of_buildings:
            building.scroll_down_all()

    def scroll_up_all(self):
        for building in self.list_of_buildings:
            building.scroll_up_all()

    def scroll_left_all(self):
        for building in self.list_of_buildings:
            building.scroll_left_all()

    def scroll_right_all(self):
        for building in self.list_of_buildings:
            building.scroll_right_all()
