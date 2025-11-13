import pygame
from Block import *

class SpaceBackground():
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        background_path = 'images/Space/Backgrounds/blue.png'
        #make a tiled background
        self.space_surface = pygame.image.load(background_path)

        #get tile width and height
        self.tile_width = self.space_surface.get_width()
        self.tile_height = self.space_surface.get_height()

        self.final_background = pygame.Surface((self.width, self.height))

        #loop over the background and place tiles on it
        for x in range(0, self.width, self.tile_width):
            for y in range(0, self.height, self.tile_height):
                self.final_background.blit(self.space_surface, (x, y))

    def get_background(self):
        return self.final_background
    
class GroundBackground():
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        #self.sky_surface pygame.image.load(background_path)
        self.final_background = pygame.Surface((self.width, self.height))
        self.final_background.fill((175, 101, 75))


        self.stone_path = 'images/Tiles/Tiles/Stone/tile_0004.png'
        self.stone_surface = pygame.image.load(self.stone_path)
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, 0, 2.5) 
        self.stone_width = self.stone_surface.get_width()
        self.stone_height = self.stone_surface.get_height()

        self.blocks = []
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(x, self.height-self.stone_height))
            self.blocks.append(Tile(x, self.height-2*self.stone_height))

        for x in range(self.width-self.stone_width*6, self.width, self.stone_width):
            self.blocks.append(Tile(x, self.stone_height*4))
            self.blocks.append(Tile(x, self.stone_height*5))

        for x in range(self.stone_width*4, self.width, self.stone_width):
            self.blocks.append(Tile(x, 0))
            self.blocks.append(Tile(x, self.stone_height))

            
        stone2_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0012.png')
        stone2_surface = pygame.transform.rotozoom(stone2_surface, 0, 2.5)
        self.blocks.append(Tile(0, self.height-3*self.stone_height))
        self.blocks.append(Tile(self.stone_width, self.height-3*self.stone_height))
        self.blocks.append(Tile(0, self.height-10*self.stone_height))
        self.blocks.append(Tile(0, self.height-12*self.stone_height))
        self.blocks.append(Tile(0, self.height-11*self.stone_height))
        self.blocks.append(Tile(0, self.height-3*self.stone_height))
        self.blocks.append(Tile(self.stone_width*6, self.height-6*self.stone_height))
        self.blocks.append(Tile(self.stone_width*7, self.height-6*self.stone_height))
        self.blocks.append(Tile(self.stone_width*8, self.height-6*self.stone_height))
        self.blocks.append(Tile(self.stone_width*10, self.height-self.stone_height*8))

        self.blocks.append(Tile(self.stone_width*13, self.height-10*self.stone_height))
        self.blocks.append(Tile(self.stone_width*12, self.height-10*self.stone_height))
        self.blocks.append(Tile(self.stone_width*11, self.height-10*self.stone_height))
        

        stone3_surface = pygame.image.load('images/Tiles/Tiles/Marble/tile_0008.png')
        stone3_surface = pygame.transform.rotozoom(stone3_surface, 0, 2.5)
        self.blocks.append(Marble(self.stone_width*2, self.height-3*self.stone_height))
        self.blocks.append(Marble(self.stone_width*9, self.height-6*self.stone_height))
        marble = Marble(self.stone_width*5, self.height-6*self.stone_height)
        marble.rotate(90)
        self.blocks.append(marble)

        stone4_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0013.png')
        stone4_surface = pygame.transform.rotozoom(stone4_surface, 0, 5)
        self.blocks.append(bigSand(0, 0))
        self.blocks.append(bigSand(self.width-8*self.stone_width, self.stone_height*2))
        self.blocks.append(bigSand(self.width-8*self.stone_width, self.stone_height*4))
        self.blocks.append(bigSand(self.width-10*self.stone_width, self.height - self.stone_height*4))
        self.blocks.append(bigSand(self.width-12*self.stone_width, self.height - self.stone_height*4))
        self.blocks.append(bigSand(self.width-10*self.stone_width, self.height - self.stone_height*6))
        self.blocks.append(bigSand(self.stone_width*2, 0))
        self.blocks.append(bigSand(0, self.stone_height*2))
        self.blocks.append(bigSand(self.width-self.stone_width*2,self.height-4*self.stone_height))

        stone3_surface = pygame.transform.rotozoom(stone3_surface, 0, 2)
        self.blocks.append(bigMarble(self.width-self.stone_width*4+10,self.height-4*self.stone_height+10, 90))
        self.blocks.append(bigMarble(self.stone_width*2-5, self.stone_height*2, 270))

        # stoneleft_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0033.png')
        # stoneleft_surface = pygame.transform.rotozoom(stoneleft_surface, 0, 5)
        self.blocks.append(leftSand(self.width-self.stone_width*6, 0))
        # stonemiddle_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0034.png')
        # stonemiddle_surface = pygame.transform.rotozoom(stonemiddle_surface, 0, 5)
        self.blocks.append(middleSand(self.width-self.stone_width*4, 0))
        # stoneright_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0035.png')
        # stoneright_surface = pygame.transform.rotozoom(stoneright_surface, 0, 5)
        self.blocks.append(rightSand(self.width-self.stone_width*2, 0))

        # self.final_background.blit(stoneright_surface, (self.width-self.stone_width*2, 0))
        # self.final_background.blit(stonemiddle_surface, (self.width-self.stone_width*4, 0))
        # self.final_background.blit(stoneleft_surface, (self.width-self.stone_width*6, 0))

        # stoneleftbot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0051.png')
        # stoneleftbot_surface = pygame.transform.rotozoom(stoneleftbot_surface, 0, 5)
        self.blocks.append(leftSandBot(self.width-self.stone_width*6, self.stone_height*2))
        # stonemiddlebot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0052.png')
        # stonemiddlebot_surface = pygame.transform.rotozoom(stonemiddlebot_surface, 0, 5)
        self.blocks.append(middleSandBot(self.width-self.stone_width*4, self.stone_height*2))
        # stonerightbot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0053.png')
        # stonerightbot_surface = pygame.transform.rotozoom(stonerightbot_surface, 0, 5)
        self.blocks.append(rightSandBot(self.width-self.stone_width*2, self.stone_height*2))


        self.ground_rects = []
        ground_height = self.stone_height*2  # or whichever layer is the topmost solid layer
        ground_y = self.height - ground_height

        # For simplicity, make the whole bottom area one long ground surface
        self.ground_rects.append(pygame.Rect(0, ground_y, self.width, ground_height))

        for i in self.blocks: 
            self.final_background.blit(i.stone_surface, (i.rect.x, i.rect.y))

    def get_ground(self):
        return self.blocks


    def get_background(self):
        return self.final_background
    

class GroundBackground2():
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.final_background = pygame.Surface((self.width, self.height))
        self.final_background.fill((175, 101, 75))

        #get standard stone images/sizes
        self.stone_path = 'images/Tiles/Tiles/Stone/tile_0004.png'
        self.stone_surface = pygame.image.load(self.stone_path)
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, 0, 2.5) 
        self.stone_width = self.stone_surface.get_width()
        self.stone_height = self.stone_surface.get_height()

        self.blocks = []

        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(x, self.height-self.stone_height))
            self.blocks.append(Tile(x, self.height-2*self.stone_height))
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(0, x))
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(x,0))
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(self.width-self.stone_width, x))

        for x in range(1, 5):
            self.blocks.append(Tile(self.stone_width*(6+x), self.height-self.stone_height*5))

        for x in range(1, 4):
            self.blocks.append(Tile(self.stone_width*(x), self.height-self.stone_height*8))
        for x in range(1, 4):
            self.blocks.append(Tile(self.stone_width*(7+x), self.height-self.stone_height*10))

        for x in range(1, 11):
            self.blocks.append(Tile(self.stone_width*11, self.height-self.stone_height*(2+x)))

        for x in range(1, 10):
            self.blocks.append(Tile(self.stone_width*(11+x), self.height-self.stone_height*(12)))

        for x in range(1, 8):
            self.blocks.append(Tile(self.stone_width*(20), self.height-self.stone_height*(12-x)))

        for x in range(1, 7):
            self.blocks.append(Tile(self.stone_width*(20-x), self.height-self.stone_height*(5)))

        for x in range(1, 5):
            self.blocks.append(Tile(self.stone_width*(14), self.height-self.stone_height*(5+x)))

        self.blocks.append(Tile(self.stone_width*(13.6), self.height-self.stone_height*(7), 1))

        for x in range(1, 4):
            self.blocks.append(Tile(self.stone_width*(14+x), self.height-self.stone_height*(9)))


        for i in self.blocks: 
            self.final_background.blit(i.stone_surface, (i.rect.x, i.rect.y))
  


    def get_ground(self):
        return self.blocks

    def get_background(self):
        return self.final_background
    

class GroundBackground3():
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT
        self.final_background = pygame.Surface((self.width, self.height))
        self.final_background.fill((175, 101, 75))

        #get standard stone images/sizes
        self.stone_path = 'images/Tiles/Tiles/Stone/tile_0004.png'
        self.stone_surface = pygame.image.load(self.stone_path)
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, 0, 2.5) 
        self.stone_width = self.stone_surface.get_width()
        self.stone_height = self.stone_surface.get_height()

        self.blocks = []
        

        for x in range(0, self.width, self.stone_width):
            if x != self.stone_width*5 and x != self.stone_width*6 and x != self.stone_width*7 and x != self.stone_width*8 and x != self.stone_width*14 and x != self.stone_width*15 and x != self.stone_width*16 and x != self.stone_width*17 and x != self.stone_width*18 and x != self.stone_width*19:
                self.blocks.append(Tile(x, self.height-self.stone_height))
                self.blocks.append(Tile(x, self.height-2*self.stone_height))

        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(0, x))
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(x,0))
        for x in range(0, self.width, self.stone_width):
            self.blocks.append(Tile(self.width-self.stone_width, x))

        self.blocks.append(Tile(self.stone_width*(6.5), self.height-self.stone_height*6))

        for x in range(0, self.width - self.stone_width*4, self.stone_width):
            if x != self.stone_width*10 and x != self.stone_width*11:
                self.blocks.append(Tile(x, self.stone_height*6))

        for x in range(self.stone_width*4, self.width, self.stone_width):
            self.blocks.append(Tile(x, self.stone_height*3))

        self.blocks.append(Tile(self.width-self.stone_width*2, self.stone_height*10))
            
        for i in self.blocks: 
            self.final_background.blit(i.stone_surface, (i.rect.x, i.rect.y))

  


    def get_ground(self):
        return self.blocks

    def get_background(self):
        return self.final_background
    


        