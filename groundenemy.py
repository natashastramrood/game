import pygame
from math import sin, cos, radians, pi
from laser import Laser
from random import randint

class GroundEnemy:
    def __init__(self,  x=0, y=0, rotation=0, xspeed = 1):
        image = 'images/Characters/Final/tile_0008.png'
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.rotozoom(self.image, rotation, 2.25) # rotate the image
        # make a new surface so the starting rotation of the spaceship
        self.finalsurface = pygame.transform.rotozoom(self.surface, 0, 1) 
        self.x = x
        self.y = y
        self.xstart = y
        self.roto = rotation # this is in degrees
        self.yspeed = 0
        self.xspeed = xspeed
        self.range = 120
        self.rect = self.finalsurface.get_rect()
        self.rect.center = (self.x,self.y)
        self.height = self.surface.get_height()
        self.shoot_cooldown = randint(60, 200)
        
    #keep enemy ships bouncing back and forth between sides of the screen
    def update(self):
        self.x += self.xspeed
        #furthest y that it can travel is within 10 pixels of the top most and bottom most parts of screen
        if self.x <= self.xstart-20 or self.x == self.xstart+self.range+10:
            self.xspeed = -self.xspeed
        self.rect.center = (self.x,self.y)
        self.rect = self.finalsurface.get_rect(center = self.rect.center)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def ready_to_shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = randint(60, 500)
            return True
        else:
            return False

    def get_rect(self):
        return self.rect

    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.finalsurface, self.rect)
