import pygame
pygame.init()
size = [600,480]
screen = pygame.display.set_mode(size)
done = False
rect = pygame.Rect(0,0,50,50)
white = (255,255,255)
blue = (0,0,255)

pygame.key.set_repeat(50,50)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    rect = rect.move(1,1)
    pygame.draw.rect(screen,blue,rect)
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
