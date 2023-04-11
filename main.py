import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (3, 41, 63)
FPS = 60

class App:
    def __init__(self) -> None:
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._title = "Pygame Jam 2023"
        pygame.display.set_caption(self._title)
        self._display_surf.fill(BLUE)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while self._running:
            self.clock.tick(FPS) 
            for event in pygame.event.get():
                self.on_event(event)
                self.on_loop()
                self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
