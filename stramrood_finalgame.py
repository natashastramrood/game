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
from StartingScreen import runLevelSelectionScreen

pygame.init()

lives = 3
final = 0
level = 0

final, level = runLevelSelectionScreen()

if level == 1: 
    final, lives = runWorld1(final, 'green') # world 1
    # final, lives = runWorld2(final, lives) # world 2 
if level == 2: 
    final, lives = runWorld1(final, 'red') # world 1
    #final, lives = runWorld2(final, lives) # world 2 
if level == 3: 
    final, lives = runWorld1(final, 'blue') # world 1
    #final, lives = runWorld2(final, lives) # world 2 
if level == 4: 
    final, lives = runWorld1(final, 'orange') # world 1
    #final, lives = runWorld2(final, lives) # world 2 
if level == 5: 
    final, lives = runWorld1(final, 'blue') # world 1
    #final, lives = runWorld2(final, lives) # world 2 
if level == 6: 
    final, lives = runWorld1(final, 'red') # world 1
    #final, lives = runWorld2(final, lives) # world 2 

#go through and check the outcome of the match
if final == 1:
    result = 2
elif lives == 0:
    result = 0
else: 
    result = 1

#end screen
runEndScreen(result)

pygame.quit()