import pygame
from background import SpaceBackground, GroundBackground
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint

def runWorld2(final, lives):

    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    lives = lives

    #initialize new background for new world
    background = GroundBackground(WIDTH, HEIGHT)
    background = background.get_background()

    running = True
    ###  LEVEL 2  ##########################################################
    while running and final != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1
        screen.blit(background, (0,0))
        
        pygame.display.flip()

        clock.tick(60)

    return final, lives
