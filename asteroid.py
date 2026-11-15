import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import PLAYER_SPEED, LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.color = "white"
        pygame.draw.circle(
            self.screen,
            self.color,
            self.position,
            self.radius,
            LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = 1.2 * vector1
            asteroid2.velocity = 1.2 * vector2
