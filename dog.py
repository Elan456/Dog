import pygame
import numpy as np


class Dog:

    def __init__(self, loc):
        self.loc = loc
        self.speed = 2

    def update(self, change):
        self.loc += change * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 200), self.loc, 5)