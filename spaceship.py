import pygame
from math import sin, cos, radians, pi
from laser import Laser
class Spaceship:
    def __init__(self, x=0, y=0, xspeed=5, yspeed = 5):
        self.image = pygame.image.load('images/Space/PNG/playerShip1_orange.png')
        self.surface = pygame.transform.rotozoom(self.image, 270, 0.8) # rotate the image
        # make a new surface so the starting rotation of the spaceship
        self.finalsurface = pygame.transform.rotozoom(self.surface, 0, 1) 
        self.x = x
        self.y = y
        self.roto = 0 # this is in degrees
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.rect = self.finalsurface.get_rect()
        self.rect.center = (self.x,self.y)


    def update(self):
        if self.roto != 90 and self.roto != 270:
            self.x += self.xspeed*cos(radians(self.roto))
            self.y += self.yspeed*sin(radians(self.roto))*(-1)
        else:
            self.x += self.xspeed
        self.rect.center = (self.x,self.y)

    def input(self, spaceship, keys):
        if keys[pygame.K_w]:
            self.update()
        if keys[pygame.K_d]:
            self.update_roto(-4)
        if keys[pygame.K_a]:
            self.update_roto(4)

    def get_rect(self):
        return self.rect

    def update_roto(self, rate):
        self.roto = (self.roto + rate) % 360 # the %360 makes sure it is less than 360
        self.finalsurface = pygame.transform.rotozoom(self.surface, self.roto, 1)
        #update my rect
        self.rect = self.finalsurface.get_rect(center = self.rect.center)
    
    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.finalsurface, self.rect)
        
    