import pygame

class Text():
    def __init__(self):
        self.title_font = pygame.font.Font('text/good timing bd.otf', 150)
        #assign a color
        self.bright_blue = (47, 147, 201)
        #make it a surface
        self.title_surface = self.title_font.render('INVADERS', 1, self.bright_blue)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (550, 350)
        self.birth_time = pygame.time.get_ticks()
        self.death_time = 2000

        #make a score font and surface
        self.score_font = pygame.font.Font('text/good timing bd.otf', 50)
        self.white = (255, 255, 255)
        self.score_surface = self.score_font.render('0', 1, self.white)

        #make a lives score and surface
        self.lives_font = pygame.font.Font('text/good timing bd.otf', 50)
        self.lives_surface = self.lives_font.render('3', 1, self.white)

    def update_score(self,score):
        self.score_surface = self.score_font.render(f"Score : {score}", 1, self.white)

    def update_lives(self, lives):
        self.lives_surface = self.lives_font.render(f"Lives : {int(lives)}", 1, self.white)

    def updatetitle(self):
        #adjust the alpha of the title based on how long the text has been in
        current_age = pygame.time.get_ticks() - self.birth_time
        current_age_percentage = current_age/self.death_time
        self.title_surface.set_alpha(255-current_age_percentage*255)

    def drawtitle(self, screen):
        screen.blit(self.title_surface, self.title_rect)
    
    def drawscore(self, screen):
        screen.blit(self.score_surface, (20, 20))

    def drawlives(self, screen):
        screen.blit(self.lives_surface, (850, 20))
