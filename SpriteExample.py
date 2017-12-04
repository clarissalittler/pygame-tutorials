import pygame
pygame.init()

size = [640,480]

screen = pygame.display.set_mode(size)

white = (255,255,255)

running = True

class Thumb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        im = pygame.image.load("thumb.png")
        self.image = pygame.transform.scale(im,(100,100))
        self.rect = self.image.get_rect()

thumb = Thumb()
spriteList = pygame.sprite.Group()
spriteList.add(thumb)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                thumb.rect.move_ip(0,-10)
            elif event.key == pygame.K_s:
                thumb.rect.move_ip(0,10)
            elif event.key == pygame.K_a:
                thumb.rect.move_ip(-10,0)
            elif event.key == pygame.K_d:
                thumb.rect.move_ip(10,0)
    screen.fill(white)
    spriteList.draw(screen)
    pygame.display.flip()

    clock.tick(60)
