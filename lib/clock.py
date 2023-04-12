import pygame
from pygame.locals import *
from constants import *

pygame.init()


class Clock:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

    def set_tick(self):
        # print(f"display current tick {self.clock.get_fps()}")
        self.clock.tick(FPS)

    def update_fps(self):
        # print(self.clock.get_fps())
        return self.clock.get_fps()


class FPS_Renderer:
    def __init__(self, clock: Clock) -> None:
        self.game_clock = clock
        self.font = pygame.font.SysFont("Ariel", 35)
        self.text = self.font.render(
            str(round(self.game_clock.update_fps(), 2)), True, WHITE
        )

    def render(self, display: pygame.Surface):
        self.text = self.font.render(
            str(round(self.game_clock.update_fps(), 2)), True, WHITE
        )
        display.blit(self.text, (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.9))
