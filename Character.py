import pygame

class Character():
    def __init__(self, x, y, xspeed = 5, yspeed = 5, ):
        self.standingimageleft = pygame.image.load('images/Characters/Final/tile_0006.png')
        self.runningimageleft = pygame.image.load('images/Characters/Final/tile_0007.png')
        self.standingimageleft = pygame.transform.rotozoom(self.standingimageleft, 0, 3)
        self.standingimageright = pygame.transform.flip(self.standingimageleft, 1, 0)
        self.runningimageleft = pygame.transform.rotozoom(self.runningimageleft, 0, 3)
        self.runningimageright = pygame.transform.flip(self.standingimageleft, 1, 0)
        self.finalsurface = self.standingimageright
        self.x = x
        self.y = y
        self.ay = 2
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.gravity = 2
        self.rect = self.finalsurface.get_rect()
        self.rect.center = (self.x,self.y)
        self.onGround = False

    def input(self, keys, jumpcount):
        if keys[pygame.K_d]:
            self.xspeed = 5
            self.finalsurface = self.runningimageright
        if keys[pygame.K_a]:
            self.xspeed = -5
            self.finalsurface = self.runningimageleft
        if keys[pygame.K_d] != True and keys[pygame.K_a] != True: 
            self.xspeed = 0
            self.finalsurface = self.standingimageright
        if keys[pygame.K_w] and jumpcount < 2:
            self.yspeed = -5
            self.onGround = False
            self.finalsurface = self.runningimageright
        if keys[pygame.K_w] != True and self.onGround != True:
            self.yspeed = 1
            self.finalsurface = self.standingimageright
        if keys[pygame.K_w] != True and self.onGround == True:
            self.yspeed = 0
            self.finalsurface = self.standingimageright
        if jumpcount == 2 and self.onGround == True:
            jumpcount = 0
        self.update()
        return jumpcount
    
    def update(self):
        """Update x and y position based on speed"""
        if not self.onGround:
            self.yspeed += self.ay
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.center = (self.x, self.y) 

    # def check_collision_with_ground(self, ground_rects):
    #     self.onGround = False
    #     for rect in ground_rects:
    #         if self.rect.colliderect(rect):
    #             # Only handle collision when falling or stationary
    #             if self.yspeed >= 0:
    #                 # Snap the bottom of the player to the top of the ground
    #                 self.y = rect.top - self.rect.height / 2
    #                 self.yspeed = 0
    #                 self.onGround = True
    #                 break

    #     # Update rect position after possible correction
    #     self.rect.center = (int(self.x), int(self.y))

    def check_block_collision(self, blocks):
        counter = 0
        for i in blocks:
            if(i.get_rect()).colliderect(self.rect) == True:
                self.onGround = True
            else:
                counter += 1
        
        if counter == len(blocks):
            self.onGround = False

    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.finalsurface, self.rect)