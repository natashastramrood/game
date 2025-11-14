import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, scale = 2.5, tile_type="GROUND"):
        # Initialize the base sprite class
        super().__init__()
        self.image = pygame.image.load('images/Tiles/Tiles/Stone/tile_0004.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, scale) 
        self.rect = self.stone_surface.get_rect() 
        self.rect.x = x
        self.rect.y = y

        self.type = tile_type 

    def get_width(self):
        return self.stone_surface.get_width()
    
    def get_height(self):
        return self.stone_surface.get_height()
    
    def get_rect(self):
        return self.rect
    
class Fire(Tile):
    def __init__(self, x, y, roto, scale, tile_type = 'GROUND'):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Water/bushOrange1.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, roto, scale)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = tile_type
    def get_width(self):
        return self.stone_surface.get_width()
    
    def get_height(self):
        return self.stone_surface.get_height()
    
    def get_rect(self):
        return self.rect
    

class GroundBlock(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type="GROUND")
        #self.image.fill((50, 200, 50)) # Green for ground

class Sand(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0012.png')
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, 0, 2.5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class Marble(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Marble/tile_0008.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 2.5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

    def rotate(self, roto):
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, roto, 1)
        self.rect = self.stone_surface.get_rect()

class bigMarble(Tile):
    def __init__(self, x, y, roto):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Marble/tile_0008.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, roto, 4.5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class bigSand(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0013.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

    def rotate(self, roto):
        self.stone_surface = pygame.transform.rotozoom(self.stone_surface, roto, 1)
        self.rect = self.stone_surface.get_rect()

class leftSand(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0033.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class middleSand(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0034.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class rightSand(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0035.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class leftSandBot(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0051.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class middleSandBot(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0052.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type

class rightSandBot(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, tile_type = 'GROUND')
        self.image = pygame.image.load('images/Tiles/Tiles/Sand/tile_0053.png')
        self.stone_surface = pygame.transform.rotozoom(self.image, 0, 5)
        self.rect = self.stone_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        tile_type = 'GROUND'
        self.type = tile_type


