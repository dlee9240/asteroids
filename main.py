# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    #initialize pygame
    pygame.init()

    #set window size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #creating two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    #adding player_1 into the two groups using pygame methods
    Player.containers = (updatable, drawable)

    #adding asteroids group
    Asteroid.containers = (asteroids, updatable, drawable)

    #adding asteroidField into only the updatable group
    AsteroidField.containers = (updatable)


    #create object after these groups so they get into groups
    player = Player(x,y)
    
    #create asteroids
    asteroid_field = AsteroidField()

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Solution had this as the top line in the while statement...
        #update before draw!!! This makes sense
        
        #for u in updatable:
        #    u.update(dt)
        updatable.update(dt)

        #checking for collisions
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                sys.exit()
            

        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        #drawable.draw(screen) 
        pygame.display.flip()
       
        #FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
