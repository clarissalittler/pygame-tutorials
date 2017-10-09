import pygame
pygame.init()

size = [600,480]
screen = pygame.display.set_mode(size)

done = False
text = ""

alphabet = "abcdefghijklmnopqrstuvwxzy"

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).lower()
            if key in alphabet:
                text = text + key
            elif event.key == pygame.K_BACKSPACE:
                text = text[0:len(text)-1]
    screen.fill((255,255,255))
    font = pygame.font.SysFont('Arial', 25)
    textSurface = font.render(text,True,(0,0,0))
    screen.blit(textSurface,[100,100])
    pygame.display.flip()
