import pygame
pygame.init()

#make screen properties
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode(WIDTH, HEIGHT)
clock = pygame.time.Clock()
running = True

#################   Testing Zone for Background   #################

#make a tiled background
space_background = 'images/images/Space/Backgrounds/blue.png'
space_surface = pygame.image.load(space_background)

#get tile width and height
tile_width = space_surface.get_width()
tile_height = space_surface.get_height()

#make a new surface, background, with the same w,h as the screen
background = pygame.Surface((WIDTH, HEIGHT))

#loop over the background and place tiles on it

for x in range(0, WIDTH, tile_width):
    for y in range(0, HEIGHT, tile_height):
        background.blit(space_surface, (x, y))





#blit the background to our screen
screen.blit(background, (0,0))



###################################################################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()