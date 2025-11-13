import pygame
from background import SpaceBackground, GroundBackground4
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint
from Character import Character
from groundenemy import GroundEnemy
from Lives_and_Title_text import Text


def runonGround4(final, lives, score):

    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    final1 = final

    lives = lives

    #initialize new background for new world
    background1 = GroundBackground4(WIDTH, HEIGHT)
    background = background1.get_background()

    #ground_rects = background1.get_ground_rects()

    character = Character(100, 550)

    #initialize variables
    jumpcount = 0
    counter = 0
    #make all lists to store current class objects and objects being deleted
    laser = []
    laser_remove = []
    enemy = []
    enemy_remove = []
    enemylaser = []
    enemylaser_remove = []
    #load up images to blit
    level2_relic = pygame.image.load('images/PNG/Items/platformPack_item010.png')
    relic_rect1 = level2_relic.get_rect(topleft=(990, HEIGHT- 160))
    relic_rect2 = level2_relic.get_rect(topleft =(320, 350))
    gem_count = []
    gem_count.clear()

    #initialize texts
    texts = Text()

    running = True
    ###  LEVEL 2  ##########################################################
    while running and final != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1
        screen.blit(background, (0,0))

        #get the block list from background class initialization
        blocks = background1.get_ground()

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

        #update enemy and fire lasers
        for i in range(len(enemy)):
            #check if enemy is ready to shoot
            if enemy[i].ready_to_shoot() == True :
                if enemy[i].direction == 'left':
                    enemylaser.append(EnemyLaser(enemy[i].x, enemy[i].y, 7, 180))
                elif enemy[i].direction == 'right':
                    enemylaser.append(EnemyLaser(enemy[i].x, enemy[i].y, -7, 0))
            enemy[i].update()
            enemy[i].draw(screen)

        #update enemy lasers and check collisions with player
        for i in range(len(enemylaser)):
            enemylaser[i].update()
            enemylaser[i].draw(screen)
            if enemylaser[i].get_rect().colliderect(character.rect):
                lives = lives - 1
                score -= 20
                enemylaser_remove.append(i)
                continue
        
        #check if enemies and character are intersecting
        for i in range(len(enemy)):
            if enemy[i].get_rect().colliderect(character.rect):
                lives -= 1
                score -= 20
                if character.x - 100 >=(60*(4)-15) and character.x-100 <= (60*(6)-15):
                    character.x = 60
                    character.y = HEIGHT - (45*3 +25)
                elif character.x - 100 >= (53*(12)-5) and character.x - 100 <= (53*(16)-10):
                    character.x = 60
                    character.y = HEIGHT - (45*3 +25)
                elif character.x-100 >= 60:
                    if character.direction == 'right':
                        character.x = character.x-100
                        character.y = HEIGHT - (45*3 +25)
                    elif character.direction == 'left':
                        character.x = character.x+100
                        character.y = HEIGHT - (45*3 +25)
                else:
                    character.x = 60
                continue

        #remove enemies and lasers that are intersecting
        laser_remove = list(set(laser_remove))
        enemy_remove = list(set(enemy_remove))
        enemylaser_remove = list(set(enemylaser_remove))

        #remove lasers that intersect with enemies
        for i in sorted(laser_remove, reverse=True):
            if 0 <= i < len(laser):
                laser.pop(i)
        laser_remove.clear()

        #remove enemies that get hit
        for k in sorted(enemy_remove, reverse=True):
            if 0 <= k < len(enemy):
                enemy.pop(k)
        enemy_remove.clear()

        #remove enemy laser that intersect with character
        for j in sorted(enemylaser_remove, reverse=True):
            if 0 <= j < len(enemylaser):
                enemylaser.pop(j)
        enemylaser_remove.clear()

        #draw text files on the screen
        texts.update_score(score)
        texts.update_lives(lives)
        texts.drawscore(screen)
        texts.drawlives(screen)

        #use input to update character position and direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if counter > 20:
                if character.direction == 'right':
                    laser.append(Laser(character.x, character.y, 7, 7, character.roto))
                    counter = 0
                elif character.direction == 'left':
                    laser.append(Laser(character.x, character.y, 7, 7, 180))
                    counter = 0
            counter += 1
        jumpcount = character.input(keys, jumpcount, blocks)

        #blit the relic and check for collisions to see if they pass the level
        if (character.rect).colliderect(relic_rect1) == True:
            if 1 not in gem_count:
                gem_count.append(1)
        if(character.rect).colliderect(relic_rect2) == True:
            if 2 not in gem_count:
                gem_count.append(2)
        if 1 not in gem_count:
            screen.blit(level2_relic, (990,HEIGHT - 160))
        if 2 not in gem_count:
            screen.blit(level2_relic, (320, 350))
        if len(gem_count) == 2:
            running = False
            print(gem_count)

        #update the character and blit the character onto the screen
        character.update(blocks)
        character.draw(screen)

        #check if the character has fallen off the screen
        if character.y > 700:
            character.x = 100
            character.y = 550
            lives -= 1

        if lives <= 0:
            running = False
            final = 1

        pygame.display.flip()

        clock.tick(60)

    return final, lives, score
