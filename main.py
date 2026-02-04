import sys
import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from logger import log_state, log_event
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)

        for asteroid_obj in asteroids:
            if player.collides_with(asteroid_obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid_obj in asteroids:
            for bullet in shots:
                if bullet.collides_with(asteroid_obj):
                    bullet.kill()
                    asteroid_obj.split()
                    log_event("asteroid_shot")

        pygame.display.flip()

        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
