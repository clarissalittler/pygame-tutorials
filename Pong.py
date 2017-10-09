import pygame
import random
pygame.init()
pygame.mixer.init()

#helper function for choosing random ball velocities to start
def randomVel():
    v = random.randrange(-5,5)
    while v == 0:
        v = random.randrange(-5,5)
    return v

screenHeight = 480
screenWidth = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))

done = False

playerYPos = screenHeight / 2
enemyYPos = screenHeight / 2

playerRect = pygame.Rect(50,screenHeight / 2 - 30, 20, 60)
enemyRect = pygame.Rect(500,screenHeight / 2 - 30, 20, 60)

ballRect = pygame.Rect(screenWidth/2,screenHeight/2,10,10)
ballVel = [randomVel(),randomVel()]

playerScore = 0
enemyScore = 0

backgroundColor = (0,0,0)
blockColor = (255,255,255)

pygame.key.set_repeat(50,50)

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 50)

pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP:
                playerRect = playerRect.move(0,-15)
            elif key == pygame.K_DOWN:
                playerRect = playerRect.move(0,15)

    screen.fill(backgroundColor)
    #displayScore
    pscore = font.render(str(playerScore),True,blockColor)
    escore = font.render(str(enemyScore),True,blockColor)
    screen.blit(pscore,[50,50])
    screen.blit(escore,[500,50])
    #move ball and check collisions
    ballRect = ballRect.move(ballVel[0],ballVel[1])
    if ballRect.bottom > screenHeight or ballRect.top < 0:
        ballVel[1] = -ballVel[1]
    elif ballRect.left < 0:
        enemyScore = enemyScore + 1
        ballRect.center = (screenWidth / 2, screenHeight / 2)
        ballVel = [randomVel(),randomVel()]
    elif ballRect.right > screenWidth:
        playerScore = playerScore + 1
        ballRect.center = (screenWidth / 2, screenHeight / 2)
        ballVel = [randomVel(),randomVel()]
    elif ballRect.colliderect(playerRect):
        ballVel[0] = -ballVel[0]
    elif ballRect.colliderect(enemyRect):
        ballVel[0] = -ballVel[0]

    pygame.draw.rect(screen,blockColor, ballRect)
    # draw player
    pygame.draw.rect(screen,blockColor, playerRect)
    # draw enemy
    pygame.draw.rect(screen,blockColor, enemyRect)

    pygame.display.flip()

    clock.tick(30)
