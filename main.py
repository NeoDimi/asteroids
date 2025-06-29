import pygame
from constants import *

def main():
    print(pygame.init())
    clock = pygame.time.Clock() #create a clock object
    dt = 0 #delta time used to track frame time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        #clock.tick(60) pauses the loop of 1/60 of a second. Effectively capping FPS to 60
        #divide by 1000 to go from ms to s and store in dt for tracking
        dt = clock.tick(60) / 1000 

if __name__=="__main__":
    main()