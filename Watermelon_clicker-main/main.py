from typing import Any

import pygame

from Interface import Interface
from Boss import Boss


class Main:
    def __init__(self):
        pygame.init()
        self.wid = 800
        self.hei = 600
        self.screen = pygame.display.set_mode((self.wid, self.hei))
        self.interface = Interface()
        self.boss = Boss(1)
        self.player_damage = 5
        self.damage_per_sec = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.interface.draw(self.screen, self.boss.level)
        self.boss.draw(self.screen)
        self.draw_hp_bar()

    def try_to_click(self, pos):
        if 100 < pos[0] < 700 and 200 < pos[1] < 600:
            self.interface.seed.count += self.boss.bite(self.player_damage)

    def draw_hp_bar(self):
        k = self.boss.hp / (50 * self.boss.level)
        width = 400 * k
        pygame.draw.rect(self.screen, (0, 250, 0), (200, 100, int(width), 50), 0)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.try_to_click(event.pos)
            self.draw()
            pygame.display.flip()


main = Main()
main.start()
