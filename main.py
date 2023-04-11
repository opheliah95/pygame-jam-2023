import pygame
from pygame.locals import *
import sys,os

dir = f"{os.getcwd()}/lib"

if os.listdir(dir): 
    sys.path.append(dir)
    from constants import * 
    print(f"total files in library: { len(os.listdir(dir))} {sys.path}")
else :
    print("library files missing")

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
        pygame.display.set_caption(TITLE)
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
