import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load('C:\\Users\\123\\Downloads\\background.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Shooter Game')
icon = pygame.image.load('C:\\Users\\123\\Downloads\\icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('C:\\Users\\123\\Downloads\\background image3.png')

spaceshipimg = pygame.image.load('C:\\Users\\123\\Downloads\\space-invaders.png')

enemyimg = []
enemyX = []
enemyY = []
enemyspeedX = []
enemyspeedY = []

no_of_enemies = 6

for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load('C:\\Users\\123\\Downloads\\enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(30, 150))
    enemyspeedX.append(-1)
    enemyspeedY.append(40)

score = 0

bulletimg = pygame.image.load('C:\\Users\\123\\Downloads\\bullet (1).png')
check = False
bulletX = 386
bulletY = 490

spaceshipX = 370
spaceshipY = 480
changeX = 0
running = True

font = pygame.font.SysFont('Arial', 32, 'bold')


def score_text():
    img = font.render(f'Score:{score}', True, 'white')
    screen.blit(img, (10, 10))


font_gameover = pygame.font.SysFont('Arial', 64, 'bold')


def gameover():
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    screen.blit(img_gameover, (200, 250))


while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -5  # speed = 5
            if event.key == pygame.K_RIGHT:
                changeX = 5
            if event.key == pygame.K_SPACE:
                if check is False:
                    bulletSound = mixer.Sound('C:\\Users\\123\\Downloads\\laser.wav')
                    bulletSound.play()
                    check = True
                    bulletX = spaceshipX + 16

        if event.type == pygame.KEYUP:
            changeX = 0
    spaceshipX += changeX  # spaceshipX=spaceshipX-changeX
    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:  # 64 picsel,   800-64=736
        spaceshipX = 736
    for i in range(no_of_enemies):
        if enemyY[i] > 420:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            gameover()
            break
        enemyX[i] += enemyspeedX[i]
        if enemyX[i] <= 0:
            enemyspeedX[i] = 1
            enemyY[i] += enemyspeedY[i]
        if enemyX[i] >= 736:
            enemyspeedX[i] = -1
            enemyY[i] += enemyspeedY[i]

        distance = math.sqrt(math.pow(bulletX - enemyX[i], 2) + math.pow(bulletY - enemyY[i], 2))
        if distance < 27:
            explosion = mixer.Sound('C:\\Users\\123\\Downloads\\explosion.wav')
            explosion.play()
            bulletY = 480
            check = False
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(30, 150)
            score += 1
        screen.blit(enemyimg[i], (enemyX[i], enemyY[i]))
    if bulletY <= 0:
        bulletY = 490
        check = False
    if check:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= 9  # 9

    screen.blit(spaceshipimg, (spaceshipX, spaceshipY))
    score_text()
    pygame.display.update()