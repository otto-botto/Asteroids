import pygame
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float):
        self.position += (self.velocity * dt)
