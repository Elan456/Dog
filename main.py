import pygame
import numpy as np
from game import *
from person import Person

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))


def main():
    clock = pygame.time.Clock()
    game = Game(gameDisplay, 500, 500)
    person = Person(np.array([100, 100], dtype="float64"))
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

        if np.sum(move_person) > 0:
            move_person /= np.linalg.norm(move_person)  # Normalizing
            person.update(move_person)

        pygame.draw.circle(gameDisplay, (255 ,255, 255), (100, 100), 5)
        pygame.display.update()

        person.draw(game.surfaces["foreground"])
        game.draw_everything()


main()