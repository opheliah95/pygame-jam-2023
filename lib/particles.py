import pygame
from pygame.locals import *
from constants import *
import random, itertools

pygame.init()


class Particle:
    def __init__(self) -> None:
        self.loc = [random.randint(0, 100), random.randint(0, 100)]
        self.color = BLUE
        self.x_velocity = random.randint(0, 20) / 10 - 1
        self.y_velocity = -1 # x and y value
        self.time_to_live = random.randint(2, 5)


class ParticleSystem:
    def __init__(self, particles_count=1) -> None:
        self.particles_list = []
        self.count = particles_count
        # self.generate_particles()

    def generate_particles(self):
        for _ in itertools.repeat(None, self.count):
            print(f"Particle {_} has been added")
            p = Particle()
            self.particles_list.append(p)

    def draw_particle(self, display: pygame.Surface):
        p:Particle 
        for p in self.particles_list:
            print("location of particle is: ", p.loc)
            p.loc[0] += p.x_velocity
            p.loc[1] += p.x_velocity
            p.time_to_live -= 0.1
            p.x_velocity += 0.1
            pygame.draw.circle(display, WHITE, radius=p.time_to_live, center=p.loc)
            if p.time_to_live <= 0:
                self.particles_list.remove(p)
                print(f"RIP now: {p}")