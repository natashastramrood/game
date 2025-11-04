import pygame
from background import SpaceBackground, GroundBackground
from spaceship import Spaceship
from laser import Laser
from enspaceship import EnemySpaceship
from enemylaser import EnemyLaser
from asteroid import Asteroid
from random import randint
from World1 import runWorld1
from World2 import runWorld2
from EndScreen import runEndScreen

pygame.init()

#make screen properties
WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

lives = 3
final = 0

final, lives = runWorld1(final)
final, lives = runWorld2(final, lives)

#go through and check the outcome of the match
if final == 1:
    result = 2
elif lives == 0:
    result = 0
else: 
    result = 1

#end screen
runEndScreen(result, screen)



pygame.quit()