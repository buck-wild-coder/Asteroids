import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            randomness = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(randomness)
            new_vector2 = self.velocity.rotate(-randomness)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.velocity = new_vector2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 