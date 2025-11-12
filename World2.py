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

    character = Character(20, 400)

    jumpcount = 0
    laser = []
    counter = 0
    laser_remove = []
    enemy = []
    enemy_remove = []

    running = True
    ###  LEVEL 2  ##########################################################
    while running and final != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1
        screen.blit(background, (0,0))

        #character.check_collision_with_ground(ground_rects)
        #character.check_block_collision(background1.get_ground())

        blocks = background1.get_ground()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if counter > 20:
                laser.append(Laser(character.x, character.y, 7, 7, character.roto))
                counter = 0
            counter += 1
        jumpcount = character.input(keys, jumpcount, blocks)

        #update the lasers
        for i in range(len(laser)):
            laser[i].update()
            for j in range(len(enemy)):
                if(laser[i].get_rect()).colliderect(enemy[j].get_rect()) == True:
                    laser_remove.append(i)
                    enemy_remove.append(j)
                    score += 100
                    continue
            laser[i].draw(screen)


        character.update(blocks)
        character.draw(screen)
        
        pygame.display.flip()

        clock.tick(60)


    return final, lives, score
