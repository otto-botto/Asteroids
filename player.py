from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.cooldown: float = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right   = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # tip (front) 
        b = self.position - forward * self.radius - right # left
        c = self.position - forward * self.radius + right # right

        return[a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt: float) -> None:
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt

    def update(self, dt:float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        if keys[pygame.K_a]:
            # reverse dt
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            dt = -1 * dt
            self.move(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0.0:
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()


    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation) # rotate() returns a new vector
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector 

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        new_vector = pygame.Vector2(0, 1)
        new_vector = new_vector.rotate(self.rotation)
        new_vector *= PLAYER_SHOOT_SPEED
        shot.velocity = new_vector

