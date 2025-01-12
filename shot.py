import pygame

from astroids.circleshape import CircleShape
from astroids.constants import SHOT_RADIUS, SHOT_COLOR


class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt