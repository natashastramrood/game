import pygame
from math import sin, cos, radians
class Spaceship:
    def __init__(self, x=0, y=0, xspeed=5, yspeed = 0):
        self.image = pygame.image.load('images/Space/PNG/playerShip1_orange.png')
        self.surface = pygame.transform.rotozoom(self.image, 270, 0.8) # rotate the image
        # make a new surface so the starting rotation of the spaceship
        self.finalsurface = pygame.transform.rotozoom(self.surface, 0, 1) 
        self.x = x
        self.y = y
        self.roto = 0
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.rect = self.finalsurface.get_rect()
        self.rect.center = (self.x,self.y)

    # it has been moving backwards because down is positive and up is negative LOL

    def update(self):
        if self.roto != 90 and self.roto != 270:
            self.x += self.xspeed*cos(self.roto)
            print("*"*20)
            print(f"position {cos(self.roto)}")
            self.y += self.yspeed*sin(self.roto)*(-1)
            print(f"position {sin(self.roto)}")
        else:
            self.x += self.xspeed
        self.rect.center = (self.x,self.y)

    def input(self, spaceship, keys):
        if keys[pygame.K_w]:
            self.update_roto()
        if keys[pygame.K_d] or keys[pygame.K_a]:
            self.update()

    def update_roto(self):
        self.roto = (self.roto + 8) % 360 # the %360 makes sure it is less than 360
        self.finalsurface = pygame.transform.rotozoom(self.image, self.roto, 0.8)
    
    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.finalsurface, self.rect)
        
    