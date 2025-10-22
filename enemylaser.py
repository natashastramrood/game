import pygame
from math import cos, sin, radians
class EnemyLaser():
    def __init__(self, x, y, xspeed, roto):
        self.image = pygame.image.load('images/Space/PNG/Lasers/laserBlue01.png')
        self.surface = pygame.transform.rotozoom(self.image, roto+270, 0.4) # rotate the image
        self.x = x
        self.y = y
        self.roto = roto-180
        self.xspeed = xspeed
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self):
        self.x -= self.xspeed
        self.rect.center = (self.x,self.y)

    def get_rect(self):
        return self.rect
    
    def draw(self, screen_surface): 
        screen_surface.blit(self.surface, self.rect)