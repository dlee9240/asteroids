from constants import *
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def asteroid_split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            new_rotation1 = self.velocity.rotate(random_angle)
            new_rotation2 = self.velocity.rotate(-random_angle)
            new_x = self.position.x
            new_y = self.position.y
            #new_asteroid = Asteroid(self.x, self.y, self.radius)
            #new_asteroid.velocity.rotate(-random_angle)

            #set the new radius for both asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            

            child_asteroid1 = Asteroid(new_x, new_y, new_radius)
            child_asteroid2 = Asteroid(new_x, new_y, new_radius)
            
            #self.velocity = pygame.Vector2(0, 0)
            child_asteroid1.velocity = new_rotation1 * 1.2
            child_asteroid2.velocity = new_rotation2 * 1.2

            #this line was added on 3/23/26
            









    

