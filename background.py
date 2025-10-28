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
        block_path = ''#get a background path
        building_path = '' #get building pieces
        #self.sky_surface pygame.image.load(background_path)
        self.final_background = pygame.Surface((self.width, self.height))
        self.final_background.fill('blue')
    def get_background(self):
        return self.final_background

        