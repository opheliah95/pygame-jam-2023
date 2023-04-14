import pygame
from pygame.locals import *
import sys, os

dir = f"{os.getcwd()}/lib"
pixel_location = []
if os.listdir(dir):
    sys.path.append(dir)
    from constants import *
    from clock import *
    from particles import *

    print(f"total files in library: { len(os.listdir(dir))} {sys.path}")
else:
    print("library files missing")

def draw_saved_strokes(display:pygame.Surface):
    for loc in pixel_location:
        # print(f'drawing:{loc}')
        rect = Rect((loc[0], loc[1], 10,10))
        pygame.draw.rect(surface=display, rect=rect, color=GREEN)
        # pygame.draw.circle(display, GREEN, radius=5, center=loc)

class App:
    def __init__(
        self, clock: Clock, fps_renderer: FPS_Renderer, particles: ParticleSystem
    ) -> None:
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.clock = clock
        self.fps_renderer = fps_renderer
        self.particles = particles

    @profile
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT_CLICK:
                pixel_location.append(pygame.mouse.get_pos())

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.set_caption(TITLE)
        self._display_surf.fill(BLUE)
        self.fps_renderer.render(self._display_surf)
        # create and display game elements
        self.particles.generate_particles()
        self.particles.draw_particle(self._display_surf)
        draw_saved_strokes(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while self._running:
            self.clock.set_tick()
            self.on_render()
            for event in pygame.event.get():
                self.on_event(event)
                self.on_loop()

        self.on_cleanup()


if __name__ == "__main__":
    fps_clock: Clock = Clock()
    fps_renderer: FPS_Renderer = FPS_Renderer(fps_clock)
    game_particle_system: ParticleSystem = ParticleSystem()
    theApp = App(fps_clock, fps_renderer, game_particle_system)
    theApp.on_execute()
