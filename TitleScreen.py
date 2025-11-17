import pygame
from background import SpaceBackground
from spaceship import Spaceship
from Lives_and_Title_text import Text

def runTitleScreen(final):
    WIDTH = 1100
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True


    background = SpaceBackground(WIDTH, HEIGHT)
    background2 = background.get_background()

    bright_blue = (47, 147, 201)
    font = pygame.font.Font('text/good timing bd.otf', 25)
    font2 = pygame.font.Font('text/good timing bd.otf', 55)
    font3 = pygame.font.Font('text/good timing bd.otf', 35)
    text_surface = font2.render("Welcome to Invader!", True, bright_blue)
    text7_surface = font3.render("Object of the Game:", True, bright_blue)
    text8_surface = font.render("Your ship has been hit! You need to obtain relics in order to fix it,", True, bright_blue)
    text9_surface = font.render("but the planets that the relics reside on are heavily guarded. Defeat the", True, bright_blue)
    text10_surface = font.render("enemy fighters and get the relics required to fix your ship!", True, bright_blue)
    text2_surface = font3.render("How to Play:", True, bright_blue)
    text3_surface = font.render(" 1. Move your spaceship to select a planet", True, bright_blue)
    text4_surface = font.render(" 2. Fight and defeat the enemy spaceships", True, bright_blue)
    text5_surface = font.render(" 3. Land on the planets ground, and defeat the enemy aliens", True, bright_blue)
    text6_surface = font.render(" 4. Obtain the relic and repeat for all planets!", True, bright_blue)
    text11_surface = font3.render("Controls:", True, bright_blue)
    text12_surface = font.render("  -  In Space: Use the W button to move forward, A and D to rotate.", True, bright_blue)
    text13_surface = font.render("  -  On Ground: Use A and D to move left and right, W to jump", True, bright_blue)
    text14_surface = font.render("  -  For Both: Use SPACE to shoot lasers!", True, bright_blue)
    text15_surface = font2.render("Press SPACE to Play!", True, bright_blue)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False
            
        screen.blit(background2, (0,0))
        screen.blit(text_surface, (250, 30))
        screen.blit(text2_surface, (100, 250))
        screen.blit(text3_surface, (100, 300))
        screen.blit(text4_surface, (100, 325))
        screen.blit(text5_surface, (100, 350))
        screen.blit(text6_surface, (100, 375))
        screen.blit(text7_surface, (100, 100))
        screen.blit(text8_surface, (100, 150))
        screen.blit(text9_surface, (100, 175))
        screen.blit(text10_surface, (100, 200))
        screen.blit(text11_surface, (100, 425))
        screen.blit(text12_surface, (100, 475))
        screen.blit(text13_surface, (100, 500))
        screen.blit(text14_surface, (100, 525))
        screen.blit(text15_surface, (200, 600))

        pygame.display.flip()
        clock.tick(60)

    return final


