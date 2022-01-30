import pygame
import sys
from pygame.color import THECOLORS

from Interface import Interface


class Main:
    def __init__(self):
        pygame.init()
        self.wid = 800
        self.hei = 600
        self.screen = pygame.display.set_mode((self.wid, self.hei))
        self.interface = Interface()
        self.functions = Functions()
        self.draw_work = True

    def draw(self):
        self.interface.draw(self.screen)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
            self.draw()
            pygame.display.flip()
main = Main()
main.start()