import pygame
def runEndScreen(result, screen):
    font = pygame.font.Font(None, 200)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # clear screen with black
        if result == 0: 
            text_surface = font.render("You Died!", True, (255, 255, 255))
        elif result == 1:
            text_surface = font.render("You Win!", True, (255, 255, 255))
        else: 
            text_surface = font.render("End Game!", True, (255, 255, 255))
        
        screen.blit(text_surface, (100, 100))
        pygame.display.flip()
        clock.tick(1200)  
    