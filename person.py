import pygame
import numpy as np


class Person:
    def __init__(self, loc):
        self.loc = loc
        self.speed = 3

    def update(self, game, change):
        self.loc += change * self.speed
        self.check_out_of_bounds(game)

    def check_out_of_bounds(self, game):
        for i in range(2):
            if self.loc[i] < 0:
                self.loc[i] = 0
            elif self.loc[i] > game.width:
                self.loc[i] = game.width

    def draw(self, surface):
        #print(self.loc)
        pygame.draw.circle(surface, (200, 0, 0), self.loc, 10)
