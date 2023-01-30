import pygame

BLACK = (0, 0, 0, 0)


class Game:
    def __init__(self, gameDisplay, display_width, display_height):
        self.gameDisplay = gameDisplay
        self.camera = Camera(display_width=display_width, display_height=display_height)
        self.surfaces = {"background": pygame.Surface((display_width, display_height), pygame.SRCALPHA),
                         "foreground": pygame.Surface((display_width, display_height), pygame.SRCALPHA)}

    def draw_everything(self):
        self.gameDisplay.fill(BLACK)
        for s in self.surfaces.values():
            s.fill(BLACK)
        self.surfaces["foreground"].blit(self.gameDisplay, (0, 0))




class Camera:
    def __init__(self, display_width, display_height, x=0, y=0):
        self.display_height = display_height
        self.display_width = display_width
        self.y = y
        self.x = x