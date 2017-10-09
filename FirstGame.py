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
    pygame.display.flip()
