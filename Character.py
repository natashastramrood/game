import pygame

class Character():
    def __init__(self, x, y, xspeed = 3, yspeed = 3):
        standing_raw = pygame.image.load('images/Characters/Final/tile_0006.png')
        running_raw = pygame.image.load('images/Characters/Final/tile_0007.png')
        scale = 3
        #scale the images and flip them for when facing the opposite direction
        self.standingimageleft = pygame.transform.rotozoom(standing_raw, 0, scale)
        self.standingimageright = pygame.transform.flip(self.standingimageleft, 1, 0)
        self.runningimageleft = pygame.transform.rotozoom(running_raw, 0, scale)
        self.runningimageright = pygame.transform.flip(self.runningimageleft, 1, 0)
        #start direction tracking to control which way the character is facing
        self.direction = 'right'
        self.finalsurface = self.standingimageright
        #declare speed and position variables
        self.x = x
        self.y = y
        self.ay = 1
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.gravity = 50/1000
        self.rect = self.finalsurface.get_rect()
        self.rect.center = (self.x,self.y)
        self.onGround = False
        self.dt = 60/1000

    # def input(self, keys, jumpcount):
    #     if keys[pygame.K_d]:
    #         self.xspeed = 5
    #         self.finalsurface = self.runningimageright
    #     if keys[pygame.K_a]:
    #         self.xspeed = -5
    #         self.finalsurface = self.runningimageleft
    #     if keys[pygame.K_d] != True and keys[pygame.K_a] != True: 
    #         self.xspeed = 0
    #         self.finalsurface = self.standingimageright
    #     if keys[pygame.K_w] and jumpcount < 2:
    #         self.yspeed = -5
    #         self.onGround = False
    #         self.finalsurface = self.runningimageright
    #     if keys[pygame.K_w] != True and self.onGround != True:
    #         self.yspeed = 10
    #         self.finalsurface = self.standingimageright
    #     if keys[pygame.K_w] != True and self.onGround == True:
    #         self.yspeed = 0
    #         self.finalsurface = self.standingimageright
    #     if jumpcount == 2 and self.onGround == True:
    #         jumpcount = 0
    #     self.update()
    #     return jumpcount
    
    def input(self, keys, jumpcount):
        #check input and adjust position and speed based on keys being pressed
        if keys[pygame.K_d]:
            self.xspeed = 5
            self.direction = 'right'
            self.finalsurface = self.runningimageright
        elif keys[pygame.K_a]:
            self.xspeed = -5
            self.direction = 'left'
            self.finalsurface = self.runningimageleft
        else: 
            self.xspeed = 0
            #change the direction the person is facing based on which way they were going last
            if self.direction == 'right':
                self.finalsurface = self.standingimageright
            else:
                self.finalsurface = self.standingimageleft 
                
        #set up so that we can jump and double jump
        if keys[pygame.K_w] and jumpcount < 2:
            #make it a more drastic vertical increase so its noticeably jumping
            self.yspeed = -3
            self.onGround = False
        
        if jumpcount == 2 and self.onGround == True:
            jumpcount = 0
            
        self.update()
        return jumpcount
    
    # def update(self):
    #     """Update x and y position based on speed"""
    #     if self.onGround == False:
    #         self.yspeed = (-1)*(self.yspeed*self.dt*1000/50) + (9.81*1000/50)*self.dt
    #     if self.onGround:
    #         self.yspeed = 0
    #     if self.y == 600:
    #         self.yspeed = 0

    #     self.x += self.xspeed
    #     self.y += self.yspeed
    #     self.rect.center = (self.x, self.y) 

    def update(self):
        #check if the character is on the ground, and if they aren't then add gravity to their y position
        if not self.onGround:
            self.yspeed += self.gravity 

        #update position based on x and y speed
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.center = (self.x, self.y)

    def collisioncheck(self, blocks):
        self.onGround = False
        #iterate through each block in the blocks list and check if they are colliding with the user
        for block in blocks:
            if self.rect.colliderect(block.get_rect()):
                #check if character was falling
                if self.yspeed > 0:
                    #snap the character to the top of the block they are intersecting with
                    self.rect.bottom = block.get_rect().top
                    self.y = self.rect.centery
                    self.yspeed = 0
                    self.onGround = True

                # If you want to add collision from below (head bonk), you'd need
                # another check (e.g., self.yspeed < 0) and resolution logic here.

    # def collisioncheck(self, blocks):
    #     counter = 0
    #     for i in blocks:
    #         if i.get_rect().collidepoint(self.rect.midbottom) == True:
    #             self.yspeed = 0
    #             self.onGround = True
    #             counter += 1
            
    #     if len(blocks) == counter:
    #         self.onGround = False
    
    def draw(self, screen_surface):
        """Draw character at his x,y on the provided surface"""
        screen_surface.blit(self.finalsurface, self.rect)