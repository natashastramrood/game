import pygame
from background import SpaceBackground, GroundBackground
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint
from Character import Character


def runWorld2(final, lives, score):

    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    lives = lives

    #initialize new background for new world
    background1 = GroundBackground(WIDTH, HEIGHT)
    background = background1.get_background()

    #ground_rects = background1.get_ground_rects()

    character = Character(20, 500)

    jumpcount = 0


    running = True
    ###  LEVEL 2  ##########################################################
    while running and final != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1
        screen.blit(background, (0,0))

        keys = pygame.key.get_pressed()
        jumpcount = character.input(keys, jumpcount)
        character.update()
        character.draw(screen)
        #character.check_collision_with_ground(ground_rects)
        character.check_block_collision(background1.get_ground())

        pygame.display.flip()

        clock.tick(60)

    return final, lives, score
