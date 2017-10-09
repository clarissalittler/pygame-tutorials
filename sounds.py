import pygame
pygame.init()

size = [600, 480]
screen = pygame.display.set_mode(size)

done = False

img = pygame.image.load("thumb.png")
img = pygame.transform.scale(img,(100,100))
imgRect = img.get_rect()
imgRect.center = (300,240)

crash = pygame.mixer.Sound("crash.wav")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                imgRect = imgRect.move(0,-10)
            elif event.key == pygame.K_DOWN:
                imgRect = imgRect.move(0,10)
            elif event.key == pygame.K_LEFT:
                imgRect = imgRect.move(-10,0)
            elif event.key == pygame.K_RIGHT:
                imgRect = imgRect.move(10,0)
        elif event.type == pygame.QUIT:
            done = True
    if imgRect.top < 0 or imgRect.bottom > 480 or imgRect.left < 0 or imgRect.right > 600:
        crash.play()
    screen.fill((255,255,255))
    screen.blit(img,imgRect)
    pygame.display.flip()

pygame.quit()
