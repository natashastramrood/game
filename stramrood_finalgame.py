import pygame
from background import Background
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint

pygame.init()

#make screen properties
WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#create our user spaceship
spaceship1 = Spaceship(WIDTH/2, HEIGHT/2, 5, 5)

#initialise starting enemy ships
enemy_spaceship = [EnemySpaceship(WIDTH-60, 70, 2),
                   EnemySpaceship(WIDTH-60, 160, 2),
                   EnemySpaceship(WIDTH-60, 250, 2),
                   EnemySpaceship(WIDTH-60, 340, 2),
                   EnemySpaceship(WIDTH-60, 430, 2),
                   EnemySpaceship(WIDTH-60, 520, 2)]

#make lists for laser and enemy laser to keep track of lasers in the game
laser = []
enemylaser=[]
asteroids = [Asteroid(200, 100, 0.5, 0.25, 60), 
             Asteroid(400, 150, -0.375, 0.25, 80),
             Asteroid(320, 625, 0.25, -0.5, 10),
             Asteroid(50, 530, 0.5, 0.25, 0),
             Asteroid(600, 275, 0.75, -0.25, 0),
             Asteroid(750, 400, 0.25, 0.5, 0)]
explosions = []

#set starting lives
lives = 3

#initialize font
font = pygame.font.Font(None, 36)

background = Background(WIDTH, HEIGHT)
background = background.get_background()
#blit the background to our screen
counter = 0
running = True

### LEVEL 1 #####################################################################
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw background
    screen.blit(background, (0,0))

    #draw spaceship character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if counter > 10:
            laser.append(Laser(spaceship1.x, spaceship1.y, 7, 7, spaceship1.roto))
            counter = 0
        counter += 1
    
    #go through the lasers and update their positions
    laser_remove = []
    enemy_remove = []
    enemylaser_remove = []
    for i in range(len(laser)):
        laser[i].update()
        laser[i].draw(screen)
        #check if lasers are intersecting with any enemies
        for k in range(len(enemy_spaceship)):
            if(laser[i].get_rect()).colliderect(enemy_spaceship[k].get_rect()) == True:
                laser_remove.append(i)
                enemy_remove.append(k)
                continue
    
    #go through the enemy lasers and check that none of them hit our spaceship
    for i in range(len(enemylaser)):
        if enemylaser[i].get_rect().colliderect(spaceship1.get_rect()):
            lives -= 1
            enemylaser_remove.append(i)
        for k in range(len(asteroids)):
            if enemylaser[i].get_rect().colliderect(asteroids[k].get_rect()):
                image = pygame.image.load('images/PNG/Blacksmoke/blackSmoke00.png')
                surface2 = pygame.transform.rotozoom(image, 0, 0.2)
                screen.blit(surface2, (asteroids[k].x, asteroids[k].y))
                asteroid_remove.append(k)
                enemylaser_remove.append(i)

    asteroid_remove = []

    # Check collisions between enemy lasers and player or asteroids
    for i in range(len(enemylaser)):
        if enemylaser[i].get_rect().colliderect(spaceship1.get_rect()):
            lives -= 1
            enemylaser_remove.append(i)
            continue

        # Check asteroid collisions
        for k in range(len(asteroids)):
            if enemylaser[i].get_rect().colliderect(asteroids[k].get_rect()):
                # Load explosion smoke once (better done outside loop ideally)
                image = pygame.image.load('images/PNG/Blacksmoke/blackSmoke00.png').convert_alpha()
                surface2 = pygame.transform.rotozoom(image, 0, 0.5)

                # Get center of the smoke so it aligns with asteroid center
                rect = surface2.get_rect(center=(asteroids[k].x, asteroids[k].y))
                screen.blit(surface2, rect.topleft)

                # Mark both for removal
                asteroid_remove.append(k)
                enemylaser_remove.append(i)
                break  # stop checking this laser, it already hit something

    # Remove asteroids that got hit
    asteroid_remove = list(set(asteroid_remove))
    for k in sorted(asteroid_remove, reverse=True):
        if 0 <= k < len(asteroids):
            asteroids.pop(k)

    asteroid_remove = []
    for i in range(len(asteroids)):
        asteroids[i].update()
        asteroids[i].draw(screen)

    asteroid_remove = list(set(asteroid_remove))
    for k in sorted(asteroid_remove, reverse=True):
        if 0 <= k < len(asteroid_remove):
            asteroid_remove.pop(k)

    #remove enemies and lasers that are intersecting
    laser_remove = list(set(laser_remove))
    enemy_remove = list(set(enemy_remove))
    enemylaser_remove = list(set(enemylaser_remove))
    for i in sorted(laser_remove, reverse=True):
        if 0 <= i < len(laser):
            laser.pop(i)
    for k in sorted(enemy_remove, reverse=True):
        if 0 <= k < len(enemy_spaceship):
            enemy_spaceship.pop(k)
    for j in sorted(enemylaser_remove, reverse=True):
        if 0 <= j < len(enemylaser):
            enemylaser.pop(j)

    #go through the enemy spaceships and update their position
    for i in range(len(enemy_spaceship)):
        #check if enemy is ready to shoot
        if enemy_spaceship[i].ready_to_shoot() == True :
            enemylaser.append(EnemyLaser(enemy_spaceship[i].x, enemy_spaceship[i].y, 7, 180))
        enemy_spaceship[i].update(HEIGHT)
        enemy_spaceship[i].draw(screen)

    #update enemy lasers
    for i in range(len(enemylaser)):
        enemylaser[i].update()
        enemylaser[i].draw(screen)

    #update the spaceship position
    spaceship1.input(spaceship1, keys)
    spaceship1.draw(screen)

    #check if user is still alive or if all enemies are dead    
    if lives == 0 or len(enemy_spaceship) == 0:
        running = False

    pygame.display.flip()

    clock.tick(60)


### END SCREEN #########################################################
font = pygame.font.Font(None, 200)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # clear screen with black

    text_surface = font.render("End Game!", True, (255, 255, 255))
    if lives == 0:
        text_surface = font.render("You Died!", True, (255, 255, 255))
    elif len(enemy_spaceship) == 0:
        text_surface = font.render("You Win!", True, (255, 255, 255))

    screen.blit(text_surface, (100, 100))

    pygame.display.flip()
    clock.tick(60)       

pygame.quit()