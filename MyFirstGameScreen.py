import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Bird & Dog Game")

background_image = pygame.transform.scale(
    pygame.image.load("download (1).jpeg").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))

random_image = pygame.transform.scale(
    pygame.image.load("images.jpeg").convert_alpha(), (200,200))
random_rect = random_image.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 +30))

text = pygame.font.Font(None,36).render("Bird & Dog Game",True,pygame.Color("black"))

text_rect = text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2 +200))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0,0))
        display_surface.blit(random_image, random_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_loop()

