import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.color = "white"
        pygame.draw.circle(
            self.screen,
            self.color,
            self.position,
            SHOT_RADIUS,
            LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += self.velocity * dt
