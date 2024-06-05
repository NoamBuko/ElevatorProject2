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

        self.create_buildings()
    

    def create_buildings(self):
        for number in range(NUM_OF_BUILDINGS):
            self.list_of_buildings.append(Building(number))

    
    def update_all(self):
        for building in self.list_of_buildings:
            building.update_all()
    

    def draw_all(self, screen):
        for building in self.list_of_buildings:
            building.draw_all(screen)

    
    def check_for_new_calls(self, position):
        for building in self.list_of_buildings:
            building.check_for_new_calls(position)