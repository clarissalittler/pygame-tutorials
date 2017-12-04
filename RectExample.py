import pygame
pygame.init()

size = [640, 480]

screen = pygame.display.set_mode(size)

white = (255,255,255)
blue = (0,0,255)

playing = True

#rectangles are objects, which means that you make them
#with the constructor provided by PyGame
#To make a rectangle you provide the:
#   x-coordinate of the upper left corner
#   y-coordinate of the upper left corner
#   width
#   height
# Note that you're not giving it a color or anything like that, just shape
rec = pygame.Rect([320,240,100,100])

while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing = False
    screen.fill(white)
    #drawing a rectangle is done with the pygame.draw.rect function
    #you give it the pygame surface to draw on, a color, and the rectangle object to draw
    pygame.draw.rect(screen,blue,rec)
    pygame.display.flip()
