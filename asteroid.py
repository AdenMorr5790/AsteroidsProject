from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

#next one might be tricky- can't tell if they're saying to override draw with the new and inside use pygame.draw.circle...or?
    def draw(self, screen): #screen is a pygame.display object
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)