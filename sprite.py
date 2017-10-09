import pygame
pygame.init()

size = [600,480]
screen = pygame.display.set_mode(size)
done = False

img = pygame.image.load("thumb.png")
img = pygame.transform.scale(img,(100,100))

sprt = pygame.sprite.Sprite()
sprt.image = img
sprt.rect = sprt.image.get_rect()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sprt.rect = sprit.rect.move(0,-10)
            elif event.key == pygame.K_DOWN:
                pos[1] = pos[1] + 10
            elif event.key == pygame.K_LEFT:
                pos[0] = pos[0] - 10
            elif event.key == pygame.K_RIGHT:
                pos[0] = pos[0] + 10
