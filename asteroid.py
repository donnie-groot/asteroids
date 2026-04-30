#imports
import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_1.velocity = a * 1.2
        new_asteroid_2.velocity = b * 1.2


