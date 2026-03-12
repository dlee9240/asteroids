from circleshape import *
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle = self.triangle()
        pygame.draw.polygon(screen, "White", triangle, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        #shoot if space bar is pressed
        if keys[pygame.K_SPACE]:
            self.shoot()

        

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    #unsure if this is correct or not
    def shoot(self):
        

        #start with pygame vector of 0,1
        if self.shot_cooldown_timer > 0:
            #dont do anything!
            return
        
        #the problem that I had was WHEN I called this... Ultimately I should exit the entire function to execute
        #first thing!!!
        player_shot = Shot(self.position.x, self.position.y)
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        player_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        


        #rotate the vector in the direction the player is facing...
        
        #player_shot.velocity.rotate(self.rotation)
        #Scale it up (multiply by Player_shoot_speed constant)
        
        #player_shot.velocity *= PLAYER_SHOOT_SPEED
        #solution file says this shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED






