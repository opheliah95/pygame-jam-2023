import pygame
from pygame.locals import *
from constants import *
import random, itertools

pygame.init()


def memorize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        # print(*args)
        key = str(*args) + str(kwargs)

        func(*args, **kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)

    return wrapper


class Particle:
    def __init__(self, color=WHITE) -> None:
        self.loc = list(pygame.mouse.get_pos())
        self.color = color
        self.x_velocity = random.randint(0, 20) / 10 - 1
        self.y_velocity = -1  # x and y value
        self.time_to_live = random.randint(2, 5)


class ParticleSystem:
    def __init__(self, particles_count=1) -> None:
        self.particles_list = []
        self.count = particles_count

    def generate_particles(self, color=WHITE):
        for _ in itertools.repeat(None, self.count):
            #print(f"Particle {_} has been added")
            p = Particle(color)
            self.particles_list.append(p)

    def draw_particle(self, display: pygame.Surface):
        self.update_particles()
        self.render_particle(display)

    def render_particle(self, display: pygame.Surface):
        p: Particle
        for p in self.particles_list:
            pygame.draw.circle(display, p.color, radius=p.time_to_live, center=p.loc)

    @memorize
    def update_particles(self):
        p: Particle
        for p in self.particles_list:
            # print("location of particle is: ", p.loc)
            p.loc[0] += p.x_velocity
            p.loc[1] += p.x_velocity
            p.time_to_live -= 0.1
            p.x_velocity += 0.1
            if p.time_to_live <= 0:
                self.particles_list.remove(p)
                # print(f"RIP now: {p}")
