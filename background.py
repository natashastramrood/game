import pygame

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
        for x in range(0, self.width, self.stone_width):
            self.final_background.blit(self.stone_surface, (x, self.height-self.stone_height))
            self.final_background.blit(self.stone_surface, (x, self.height-2*self.stone_height))

        for x in range(self.width-self.stone_width*6, self.width, self.stone_width):
            self.final_background.blit(self.stone_surface, (x, self.stone_height*4))
            self.final_background.blit(self.stone_surface, (x, self.stone_height*5))

        for x in range(self.stone_width*4, self.width, self.stone_width):
            self.final_background.blit(self.stone_surface, (x, 0))
            self.final_background.blit(self.stone_surface, (x, self.stone_height))
            
        stone2_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0012.png')
        stone2_surface = pygame.transform.rotozoom(stone2_surface, 0, 2.5)
        self.final_background.blit(stone2_surface, (0, self.height-3*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width, self.height-3*self.stone_height))
        self.final_background.blit(stone2_surface, (0, self.height-7*self.stone_height))
        self.final_background.blit(stone2_surface, (0, self.height-9*self.stone_height))
        self.final_background.blit(stone2_surface, (0, self.height-8*self.stone_height))
        self.final_background.blit(stone2_surface, (0, self.height-3*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*6, self.height-6*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*7, self.height-6*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*8, self.height-6*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*10, self.height-self.stone_height*8))


        self.final_background.blit(stone2_surface, (self.stone_width*13, self.height-10*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*12, self.height-10*self.stone_height))
        self.final_background.blit(stone2_surface, (self.stone_width*11, self.height-10*self.stone_height))

        stone3_surface = pygame.image.load('images/Tiles/Tiles/Marble/tile_0008.png')
        stone3_surface = pygame.transform.rotozoom(stone3_surface, 0, 2.5)
        self.final_background.blit(stone3_surface, (self.stone_width*2, self.height-3*self.stone_height))
        self.final_background.blit(stone3_surface, (self.stone_width*9, self.height-6*self.stone_height))
        stone3_surface = pygame.transform.rotozoom(stone3_surface, 90, 1)
        self.final_background.blit(stone3_surface, (self.stone_width*5, self.height-6*self.stone_height))

        stone4_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0013.png')
        stone4_surface = pygame.transform.rotozoom(stone4_surface, 0, 5)
        self.final_background.blit(stone4_surface, (0, 0))
        self.final_background.blit(stone4_surface, (self.width-8*self.stone_width, self.stone_height*2))
        self.final_background.blit(stone4_surface, (self.width-8*self.stone_width, self.stone_height*4))
        self.final_background.blit(stone4_surface, (self.width-10*self.stone_width, self.height - self.stone_height*4))
        self.final_background.blit(stone4_surface, (self.width-12*self.stone_width, self.height - self.stone_height*4))
        self.final_background.blit(stone4_surface, (self.width-10*self.stone_width, self.height - self.stone_height*6))
        self.final_background.blit(stone4_surface, (self.stone_width*2, 0))
        self.final_background.blit(stone4_surface, (0, self.stone_height*2))
        self.final_background.blit(stone4_surface, (self.width-self.stone_width*2,self.height-4*self.stone_height))

        stone3_surface = pygame.transform.rotozoom(stone3_surface, 0, 2)
        self.final_background.blit(stone3_surface, (self.width-self.stone_width*4,self.height-4*self.stone_height))
        stone3_surface = pygame.transform.rotozoom(stone3_surface, 180, 1)
        self.final_background.blit(stone3_surface, (self.stone_width*2, self.stone_height*2))
        stone3_surface = pygame.transform.rotozoom(stone3_surface, 0, 1.25)
        self.final_background.blit(stone3_surface, (0,self.stone_height*4))

        stoneleft_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0033.png')
        stoneleft_surface = pygame.transform.rotozoom(stoneleft_surface, 0, 5)
        stonemiddle_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0034.png')
        stonemiddle_surface = pygame.transform.rotozoom(stonemiddle_surface, 0, 5)
        stoneright_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0035.png')
        stoneright_surface = pygame.transform.rotozoom(stoneright_surface, 0, 5)

        self.final_background.blit(stoneright_surface, (self.width-self.stone_width*2, 0))
        self.final_background.blit(stonemiddle_surface, (self.width-self.stone_width*4, 0))
        self.final_background.blit(stoneleft_surface, (self.width-self.stone_width*6, 0))

        stoneleftbot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0051.png')
        stoneleftbot_surface = pygame.transform.rotozoom(stoneleftbot_surface, 0, 5)
        stonemiddlebot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0052.png')
        stonemiddlebot_surface = pygame.transform.rotozoom(stonemiddlebot_surface, 0, 5)
        stonerightbot_surface = pygame.image.load('images/Tiles/Tiles/Sand/tile_0053.png')
        stonerightbot_surface = pygame.transform.rotozoom(stonerightbot_surface, 0, 5)

        self.final_background.blit(stonerightbot_surface, (self.width-self.stone_width*2, self.stone_height*2))
        self.final_background.blit(stonemiddlebot_surface, (self.width-self.stone_width*4, self.stone_height*2))
        self.final_background.blit(stoneleftbot_surface, (self.width-self.stone_width*6, self.stone_height*2))


        stone_spike_surface = pygame.image.load('images/Tiles/Tiles/Rock/tile_0008.png')
        stone_spike_surface = pygame.transform.rotozoom(stone_spike_surface, 225, 2.5)
        for x in range(0,3):
            self.final_background.blit(stone_spike_surface, (self.stone_width*(6+x)+(10*x), self.height- self.stone_height*3+5))
        self.final_background.blit(stone_spike_surface, (self.stone_width*7-10, self.height-7*self.stone_height+5))
        self.final_background.blit(stone_spike_surface, (self.stone_width*12+35, self.height-self.stone_height*5+5))
        self.final_background.blit(stone_spike_surface, (self.stone_width*16+15, self.height-self.stone_height*3+5))
        self.final_background.blit(stone_spike_surface, (self.stone_width*17+30, self.height-self.stone_height*3+5))

        self.ground_rects = []
        ground_height = self.stone_height*2  # or whichever layer is the topmost solid layer
        ground_y = self.height - ground_height

        # For simplicity, make the whole bottom area one long ground surface
        self.ground_rects.append(pygame.Rect(0, ground_y, self.width, ground_height))

    def get_ground_rects(self):
        return self.ground_rects


    def get_background(self):
        return self.final_background

        