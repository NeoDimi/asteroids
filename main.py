import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(pygame.init())
    clock = pygame.time.Clock() #create a clock object
    dt = 0 #delta time used to track frame time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #needs to be created after the addition of containers
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game Over!")
                return
        pygame.display.flip()
        #clock.tick(60) pauses the loop of 1/60 of a second. Effectively capping FPS to 60
        #divide by 1000 to go from ms to s and store in dt for tracking
        dt = clock.tick(60) / 1000 

if __name__=="__main__":
    main()