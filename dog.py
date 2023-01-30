import pygame
import math as m
import numpy as np
import random

STRETCH = 10
LEASH_NODES = 10


def normalize(x):
    return x / np.linalg.norm(x)


class Dog:

    def __init__(self, loc, owner):
        self.loc = loc
        self.speed = 2
        self.leash = []
        self.owner = owner

        owner_dir = normalize(owner.loc - self.loc)
        owner_dist = np.linalg.norm(self.loc - owner.loc)
        for i in range(LEASH_NODES):
            self.leash.append(self.loc + i * owner_dir * owner_dist / LEASH_NODES)

    def update(self, change=np.zeros(2)):
        self.loc += change * self.speed
        self.update_leash()
        diff = self.owner.loc - self.loc
        distance = np.linalg.norm(diff)
        if distance > LEASH_NODES * STRETCH:
            if not np.all(self.leash[1] - self.loc == 0):
                self.loc += normalize(self.leash[1] - self.loc) * self.speed

    def update_leash(self):
        for i in range(LEASH_NODES):
            if 0 < i < LEASH_NODES - 1:
                if i % 2 == 0:
                    order = [-1, 1]
                else:
                    order = [1, -1]
                for look in order:
                    # calculate direction and distance to next and previous node
                    diff = self.leash[i + look] - self.leash[i]
                    direction = normalize(diff)
                    dist = np.linalg.norm(diff)

                    if dist > STRETCH:
                        move = direction * (dist - STRETCH) / 2
                        self.leash[i] += move
            elif i == LEASH_NODES - 1:
                self.leash[i] = self.owner.loc
            elif i == 0:
                self.leash[i] = self.loc

    def draw_leash(self, surface):
        # for l in self.leash:
        #     pygame.draw.circle(surface, (128, 128, 0), l, 2)

        pygame.draw.lines(surface, (128, 128, 128), False, self.leash, 2)

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 200), self.loc, 5)
        self.draw_leash(surface)
