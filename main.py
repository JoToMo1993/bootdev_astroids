import pygame

from astroids.asteroid import Asteroid
from astroids.asteroidfield import AsteroidField
from astroids.player import Player
from astroids.shot import Shot
from constants import *

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        print(f'num updatable: {len(updatable)}')
        print(f'num drawable: {len(drawable)}')
        print(f'num asteroids: {len(asteroids)}')

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if player.collide(a):
                print('Game over!')
                return

        for s in shots:
            for a in asteroids:
                if s.collide(a):
                    a.split()
                    s.kill()

        screen.fill((0, 0, 0))
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()