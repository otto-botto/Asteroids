from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)



