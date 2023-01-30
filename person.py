import pygame
import numpy as np


class Person:
    def __init__(self, loc):
        self.loc = loc
        self.speed = 3

    def update(self, change):
        self.loc += change * self.speed

    def draw(self, surface):
        #print(self.loc)
        pygame.draw.circle(surface, (200, 0, 0), self.loc, 10)
