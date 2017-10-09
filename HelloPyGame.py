import pygame
pygame.init()

size = [600,480]
screen = pygame.display.set_mode(size)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))
    font = pygame.font.SysFont('Arial', 50)
    textSurface = font.render("Hello World!",True,(0,0,0))
    screen.blit(textSurface,[100,100])
    pygame.display.flip()

pygame.quit()
