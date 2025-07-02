import pygame
import random
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50) #new asteroids shall split at random, opposite angles
        new_velocity1 = self.velocity.rotate(split_angle)
        new_velocity2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2 #the new asteroids shall move faster
        asteroid2.velocity = new_velocity2 * 1.2
        