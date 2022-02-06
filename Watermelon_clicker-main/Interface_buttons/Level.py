import pygame.image
from pygame.color import THECOLORS

class Level:
    def __init__(self):
        self.value = 1
        self.image = pygame.image.load(r'img/Level.png')
        self.pos = (50, 0)
        self.font = pygame.font.SysFont('couriernew', 50)

    def draw(self, screen, value):
        text = self.font.render(str(f'{value}'), True, THECOLORS['green'])
        screen.blit(self.image, self.pos)
        screen.blit(text, (60, 0))