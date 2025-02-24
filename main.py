# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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
    player_1 = Player(x,y)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Solution had this as the top line in the while statement...
        player_1.update(dt)    
        screen.fill("black")
        player_1.draw(screen) 
        pygame.display.flip()
       
        #FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
