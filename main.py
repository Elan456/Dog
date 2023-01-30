import pygame
import numpy as np
from game import *
from person import Person
from dog import Dog

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))


def main():
    clock = pygame.time.Clock()
    game = Game(gameDisplay, 500, 500)
    person = Person(np.array([100, 100], dtype="float64"))
    dog = Dog(np.array([150, 200], dtype="float64"))
    while True:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        move_person = np.array([0, 0], dtype="float64")

        if keys[pygame.K_UP]:
            move_person[1] -= 1
        if keys[pygame.K_DOWN]:
            move_person[1] += 1
        if keys[pygame.K_RIGHT]:
            move_person[0] += 1
        if keys[pygame.K_LEFT]:
            move_person[0] -= 1

        if move_person[0] != 0 or move_person[1] != 0:
            move_person /= np.linalg.norm(move_person)  # Normalizing
            person.update(game, move_person)

        game.clear_surfaces()
        person.draw(game.surfaces["foreground"])
        dog.draw(game.surfaces["foreground"])
        game.draw_surfaces_onto_gameDisplay()
        pygame.display.update()

main()
