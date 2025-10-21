import pygame
from background import Background
from spaceship import Spaceship


pygame.init()

#make screen properties
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

spaceship1 = Spaceship(WIDTH/2, HEIGHT/2, 10, 5)

background = Background(WIDTH, HEIGHT)
background = background.get_background()
#blit the background to our screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw background
    screen.blit(background, (0,0))
    #draw spaceship character
    keys = pygame.key.get_pressed()
    spaceship1.input(spaceship1, keys)
    spaceship1.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()