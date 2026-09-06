import pygame
import random
from circleshape import *
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float):
        self.position += (self.velocity * dt)

    def split(self) -> None:
        # kill this asteroid, either dead or split into 2 new ones
        self.kill()

        # small asteroid, gone
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return

        # splitting 
        log_event("asteroid_split")
        new_angle: float = random.uniform(20.0, 50.0)
        
        # first new asteroid 
        new_velocity = self.velocity.rotate(new_angle)
        # second asteroid
        new_velocity_opposite = self.velocity.rotate(-new_angle)

        # new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # new asteroid 1
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity * 1.2

        # new asteroid 2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_velocity_opposite * 1.2


