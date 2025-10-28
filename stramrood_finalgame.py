import pygame
from background import SpaceBackground, GroundBackground
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
enemy_spaceship = [EnemySpaceship(WIDTH-60, 70, 90, 2),
                   EnemySpaceship(WIDTH-60, 160, 90, 2),
                   EnemySpaceship(WIDTH-60, 250, 90, 2),
                   EnemySpaceship(WIDTH-60, 340, 90, 2),
                   EnemySpaceship(WIDTH-60, 430, 90, 2),
                   EnemySpaceship(WIDTH-60, 520, 90, 2)]

#make lists for laser and enemy laser to keep track of lasers in the game
laser = []
enemylaser=[]

#create the asteroids
asteroids = [Asteroid(200, 100, 0.1, 0.04, 60), 
             Asteroid(400, 150, -0.075, 0.05, 80),
             Asteroid(320, 625, 0.05, -0.1, 10),
             Asteroid(50, 530, 0.1, 0.05, 0),
             Asteroid(600, 275, 0.15, -0.05, 0),
             Asteroid(750, 400, 0.05, 0.1, 0)]

#set starting lives
lives = 3

#initialize font
font = pygame.font.Font(None, 36)

#initialize the background
background = SpaceBackground(WIDTH, HEIGHT)
background = background.get_background()

#final checks if the person exited the game voluntarily
final = 0
#running checks if that level is running or not
running = True

counter = 0
### LEVEL 1 #####################################################################
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            final = 1
    
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

    # Check collisions between enemy lasers and player
    for i in range(len(enemylaser)):
        if enemylaser[i].get_rect().colliderect(spaceship1.get_rect()):
            lives -= 1
            enemylaser_remove.append(i)
            continue
    
    #update asteroid position
    for i in range(len(asteroids)):
        asteroids[i].update()
        asteroids[i].draw(screen)

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
    if lives == 0:
        running = False
        final += 1
    elif len(enemy_spaceship) == 0:
        running = False

    pygame.display.flip()

    clock.tick(60)

#create new enemy spaceships on the other side of the screen
enemy_spaceship = [EnemySpaceship(60, 70, 270, 2),
                   EnemySpaceship(60, 160, 270, 2),
                   EnemySpaceship(60, 250, 270, 2),
                   EnemySpaceship(60, 340, 270, 2),
                   EnemySpaceship(60, 430, 270, 2),
                   EnemySpaceship(60, 520, 270, 2)]

laser = []
enemylaser = []

#reset running as true
running = True

### LEVEL 1 CONTINUED #####################################################################
while running and final != 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            final = 1
    
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

    # Check collisions between enemy lasers and player
    for i in range(len(enemylaser)):
        if enemylaser[i].get_rect().colliderect(spaceship1.get_rect()):
            lives -= 1
            enemylaser_remove.append(i)
            continue

    for i in range(len(asteroids)):
        asteroids[i].update()
        asteroids[i].draw(screen)

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
    if lives == 0:
        running = False
        final = 1
    elif len(enemy_spaceship) == 0:
        running = False

    pygame.display.flip()

    clock.tick(60)

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