import pygame
pygame.init()

size = [600,480]
screen = pygame.display.set_mode(size)

white = (255,255,255)
blue = (0,0,255)

rect = pygame.Rect([200,200,50,50])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    pygame.draw.rect(screen,blue,rect)

    pygame.display.flip()

pygame.quit()
