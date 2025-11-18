import pygame
from background import SpaceBackground, GroundBackground2
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint
from Character import Character
from groundenemy import GroundEnemy
from Lives_and_Title_text import Text


def runonGround2(final, lives, score):

    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    final1 = final

    lives = lives

    #initialize new background for new world
    background1 = GroundBackground2(WIDTH, HEIGHT)
    background = background1.get_background()

    #Initialize sounds
    hit_sound = pygame.mixer.Sound("Sounds/hitonground.ogg")
    laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")
    relic_collect_sound = pygame.mixer.Sound("Sounds/reliccollect.ogg")

    character = Character(100, 550)

    jumpcount = 0
    laser = []
    counter = 0
    laser_remove = []
    enemy = [GroundEnemy(700, 135, 170, 'left', 0, 1.5),
             GroundEnemy(90, HEIGHT-(9*45)+20, 60, 'right'), 
             GroundEnemy(685, (6*45), 85),
             GroundEnemy(700, HEIGHT - 115, 160, 'right')]
    enemy_remove = []
    enemylaser = []
    enemylaser_remove = []
    level2_relic = pygame.image.load('images/PNG/Items/platformPack_item004.png')
    relic_rect = level2_relic.get_rect(topleft=(675, 400))
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
                #maybe add a new hit sound
                continue
        
        #check if enemies and character are intersecting
        for i in range(len(enemy)):
            if enemy[i].get_rect().colliderect(character.rect):
                lives -= 1
                score -= 20
                hit_sound.play()
                if character.x-100 >= 20:
                    character.x = character.x-100
                else:
                    character.x = 20
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
                    laser_sound.play()
                elif character.direction == 'left':
                    laser.append(Laser(character.x, character.y, 7, 7, 180))
                    counter = 0
                    laser_sound.play()
            counter += 1
        jumpcount = character.input(keys, jumpcount, blocks)

        #blit the relic
        if (character.rect).colliderect(relic_rect) != True:
            screen.blit(level2_relic, (675,400))
        if (character.rect).colliderect(relic_rect): 
            running = False
            relic_collect_sound.play()

        character.update(blocks)
        character.draw(screen)

        if lives <= 0:
            running = False
            final = 1

        pygame.display.flip()

        clock.tick(60)

    return final, lives, score
