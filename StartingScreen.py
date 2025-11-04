import pygame
from background import SpaceBackground
from spaceship import Spaceship

def runLevelSelectionScreen():
    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 200)

    #checker to see if the user voluntarily exited the game
    final = 0

    background = SpaceBackground(WIDTH, HEIGHT)
    background2 = background.get_background()

    spaceship1 = Spaceship(WIDTH/2, HEIGHT/2, 5, 5)

    planet1_image = pygame.image.load('images/PlanetFolder/Planets/planet00.png')
    planet1 = pygame.transform.rotozoom(planet1_image, 0, 0.17)
    planet1_rect = planet1.get_rect()
    planet1_rect.topleft = (100, 50)
    #planet 2 of 6
    planet2_image = pygame.image.load('images/PlanetFolder/Planets/planet06.png')
    planet2= pygame.transform.rotozoom(planet2_image, 0, 0.17)
    planet2_rect = planet2.get_rect()
    planet2_rect.topleft = (50, 250)
    #planet 3 of 6
    planet3_image = pygame.image.load('images/PlanetFolder/Planets/planet04.png')
    planet3 = pygame.transform.rotozoom(planet3_image, 0, 0.17)
    planet3_rect = planet3.get_rect()
    planet3_rect.topleft = (100, 450)
    #planet 4 of 6
    planet4_image = pygame.image.load('images/PlanetFolder/Planets/planet08.png')
    planet4 = pygame.transform.rotozoom(planet4_image, 0, 0.17)
    planet4_rect = planet4.get_rect()
    planet4_rect.topleft = (775, 50)
    #planet 5 of 6
    planet5_image = pygame.image.load('images/PlanetFolder/Planets/planet07.png')
    planet5 = pygame.transform.rotozoom(planet5_image, 0, 0.17)
    planet5_rect = planet5.get_rect()
    planet5_rect.topleft = (825, 250)
    #planet 6 of 6
    planet6_image = pygame.image.load('images/PlanetFolder/Planets/planet05.png')
    planet6 = pygame.transform.rotozoom(planet6_image, 0, 0.17)
    planet6_rect = planet6.get_rect()
    planet6_rect.topleft = (775, 450)

    level = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1

        screen.blit(background2, (0,0))
        screen.blit(planet1, (100, 50))
        screen.blit(planet2, (50, 250))
        screen.blit(planet3, (100, 450))
        screen.blit(planet4, (775, 50))
        screen.blit(planet5, (825, 250))
        screen.blit(planet6, (775, 450))

        #update and move spaceship
        keys = pygame.key.get_pressed()
        spaceship1.input(spaceship1, keys)
        spaceship1.draw(screen)

        #check if spaceship collides with any of the planets
        if spaceship1.get_rect().collidepoint(planet1_rect.center):
            level = 1
            running = False
        elif spaceship1.get_rect().collidepoint(planet2_rect.center):
            level = 2
            running = False
        elif spaceship1.get_rect().collidepoint(planet3_rect.center):
            level = 3
            running = False
        elif spaceship1.get_rect().collidepoint(planet4_rect.center):
            level = 4
            running = False
        elif spaceship1.get_rect().collidepoint(planet5_rect.center):
            level = 5
            running = False
        elif spaceship1.get_rect().collidepoint(planet6_rect.center):
            level = 6
            running = False
        pygame.display.flip()
        clock.tick(60)
    return final, level

