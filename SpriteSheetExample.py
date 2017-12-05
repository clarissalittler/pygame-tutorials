import pygame
pygame.init()

size = [640,480]

screen = pygame.display.set_mode(size)

white = (255,255,255)

running = True

clock = pygame.time.Clock()

class Flapper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load("FlappySpritesheet.png")
        self.image = pygame.Surface((100,100)).convert()
        self.image.set_colorkey((0,0,0))
        self.image.blit(self.sheet,(0,0),[0,0,100,100])
        self.rect = self.image.get_rect()
        self.tick = 0

    def update(self):
        self.tick = self.tick + 1
        self.image = pygame.Surface((100,100)).convert()
        self.image.set_colorkey((0,0,0))
        if self.tick % 2 == 1:
            self.image.blit(self.sheet,(0,0),[0,100,100,100])
        else:
            self.image.blit(self.sheet,(0,0),[0,0,100,100])


flapper = Flapper()

spriteList = pygame.sprite.Group()

spriteList.add(flapper)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                flapper.rect.move_ip(0,-10)
            elif event.key == pygame.K_s:
                flapper.rect.move_ip(0,10)
            elif event.key == pygame.K_a:
                flapper.rect.move_ip(-10,0)
            elif event.key == pygame.K_d:
                flapper.rect.move_ip(10,0)
    screen.fill(white)
    spriteList.update()
    spriteList.draw(screen)
    pygame.display.flip()

    clock.tick(20)
