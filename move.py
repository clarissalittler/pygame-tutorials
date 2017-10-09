import pygame
pygame.init()

size = [600,480]
screen = pygame.display.set_mode(size)

done = False

rect = pygame.Rect(200,200,50,50)

white = (255,255,255)
blue = (0,0,255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect = rect.move(0,-10)
            elif event.key == pygame.K_DOWN:
                rect = rect.move(0,10)
            elif event.key == pygame.K_LEFT:
                rect = rect.move(-10,0)
            elif event.key == pygame.K_RIGHT:
                rect = rect.move(10,0)
        elif event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    pygame.draw.rect(screen,blue,rect)
    pygame.display.flip()

pygame.quit()
