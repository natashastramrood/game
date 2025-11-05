import pygame
from background import SpaceBackground

def runEndScreen(result):
    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font('text/good timing bd.otf', 150)
    bright_blue = (47, 147, 201)
    running = True
    clock = pygame.time.Clock()

    background = SpaceBackground(WIDTH, HEIGHT)
    background = background.get_background()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0,0))  # space background
        if result == 0: 
            text_surface = font.render("You Died!", True, bright_blue)
        elif result == 1:
            text_surface = font.render("You Win!", True, bright_blue)
        else: 
            text_surface = font.render("End Game!", True, bright_blue)
        
        screen.blit(text_surface, (150, 200))
        pygame.display.flip()
        clock.tick(1200)  
    