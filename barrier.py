import pygame

screen = pygame.display.set_mode((640,480))

done = False

pygame.key.set_repeat(50,50)
player = pygame.Rect([200,200,50,50])
wall = pygame.Rect([100,100,25,100])

while not done:
    test = player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                test = player.move(0,-5)
            elif event.key == pygame.K_DOWN:
                test = player.move(0,5)
            elif event.key == pygame.K_LEFT:
                test = player.move(-5,0)
            elif event.key == pygame.K_RIGHT:
                test = player.move(5,0)
    if not wall.colliderect(test):
        player = test
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,255,0),wall)
    pygame.display.flip()

pygame.quit()
