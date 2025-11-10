from circleshape import CircleShape
from constants import *
import pygame
from logger import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rnum = uniform(20, 50)
            v1 = self.velocity.rotate(rnum)
            v2 = self.velocity.rotate(-rnum)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position[0], self.position[1], new_radius)
            a2 = Asteroid(self.position[0], self.position[1], new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
                          