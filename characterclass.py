import pygame
class Character:
    def __init__(self, x=0, y=0, xspeed=5, yspeed = 0):
        self.image = pygame.image.load('images/character_femaleAdventurer_wide.png')
        self.surface = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x,self.y)
    def reverse_x(self):
        """Change x speed to the opposite direction"""
        self.xspeed = self.xspeed*(-1)
    def reverse_y(self):
        """Change y speed to the opposite direction"""
        self.yspeed = self.yspeed*(-1)
    def update(self):
        """Update x and y position based on speed"""
        self.x += self.xspeed
        self.y += self.yspeed
    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.surface,self.rect)
        
    