import pygame
pygame.init()

size = [640, 480]

screen = pygame.display.set_mode(size)

white = (255,255,255)
blue = (0,0,255)

playing = True

rec = pygame.Rect([320,240,100,100])

while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing = False
        #Here we test for the pygame.KEYDOWN event
        #If this event fires, then we should see *what* key fired
        #We test to see if the key was one of WASD and move the rect accordingly if it is
        #for the move_ip function the first argument is how much to change the x-coordinate
        #and the second is how much to change the y-coordinate
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rec.move_ip(-10,0)
            elif event.key == pygame.K_d:
                rec.move_ip(10,0)
            elif event.key == pygame.K_s:
                rec.move_ip(0,10)
            elif event.key == pygame.K_w:
                rec.move_ip(0,-10)

    screen.fill(white)
    pygame.draw.rect(screen,blue,rec)
    pygame.display.flip()
