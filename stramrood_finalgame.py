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
from SecondWorld1 import runSecondWorld1
from InteractiveWorld1 import runInteractiveWorld1

pygame.init()

lives = 3
final = 0
score = 0
num_completed = 0
levels_completed = []

while num_completed <= 6 and final != 1:
    level = 0
    final, level = runLevelSelectionScreen(levels_completed)

    if level == 1: 
        final, lives, score = runSecondWorld1(final, 'green', score) # world 1
        # final, lives = runWorld2(final, lives) # worldd 2 
        num_completed += 1
        levels_completed.append(1)
    if level == 2: 
        final, lives, score = runWorld1(final, 'red', score) # world 1
        #final, lives = runWorld2(final, lives) # world 2 
        num_completed += 1
        levels_completed.append(2)
    if level == 3: 
        final, lives, score = runWorld1(final, 'blue', score) # world 1
        #final, lives = runWorld2(final, lives) # world 2 
        num_completed += 1
        levels_completed.append(3)
    if level == 4: 
        final, lives, score = runWorld1(final, 'orange', score) # world 1
        #final, lives = runWorld2(final, lives) # world 2 
        num_completed += 1
        levels_completed.append(4)
    if level == 5: 
        final, lives, score = runSecondWorld1(final, 'blue', score) # world 1
        #final, lives = runWorld2(final, lives) # world 2 
        num_completed += 1
        levels_completed.append(5)
    if level == 6: 
        final, lives, score = runSecondWorld1(final, 'red', score) # world 1
        #final, lives = runWorld2(final, lives) # world 2 
        num_completed += 1
        levels_completed.append(6)

#go through and check the outcome of the match
if final == 1 and lives <= 0:
    result = 0
elif final == 1:
    result = 2
else: 
    result = 1

#end screen
runEndScreen(result)

pygame.quit()