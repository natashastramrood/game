import pygame
from characterclass import Character

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
print(type(screen))
clock = pygame.time.Clock()
running = True

user = Character(WIDTH/2, HEIGHT/2)

sky_blue = [0, 150, 255]

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    user.update() #update user position
    screen.fill(sky_blue)
    user.draw(screen) #paint the user on top of the blue background
    pygame.display.flip() #show the person playing the game

    clock.tick(60)  

pygame.quit()
