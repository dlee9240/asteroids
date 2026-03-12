import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()



    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    #GAME LOOP
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
      
        updatable.update(dt)

        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()


