import pygame
from math import cos, sin, radians
from random import randint
class Asteroid():
    def __init__(self, x, y, xspeed, yspeed, roto):
        image = 'images/Space/PNG/Meteors/meteor'
        #use random to get random sizes for the meteor
        color = randint(0,2)
        if color == 0: 
            image += 'Brown'
        else: 
            image += 'Grey'
        image += '_'
        size = randint(0,3)
        if size == 3:
            image += 'big' 
            image += str(randint(1,4))
        elif size == 2:
            image += 'med'
            image += str(randint(1,2))
        elif size == 1:
            image += 'small'
            image += str(randint(1,2))
        elif size == 0:
            image += 'tiny'
            image += str(randint(1,2))
        image += '.png'
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.rotozoom(self.image, roto, 1) # rotate the image
        self.x = x
        self.y = y
        self.roto = roto
        self.xspeed = xspeed*cos(radians(roto))
        self.yspeed = -yspeed*sin(radians(roto))
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.center = (self.x,self.y)

    def get_rect(self):
        return self.rect
    
    def draw(self, screen_surface): 
        screen_surface.blit(self.surface, self.rect)