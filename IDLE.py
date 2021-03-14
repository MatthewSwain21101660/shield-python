import pygame

pygame.init()
#importing and initialising the required libraries

screen = pygame.display.set_mode((1280, 720))
#Setting the resolution

charPosX = 610
charPosY = 630
#Setting up global variables


def room1():
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    #Background and walls
    pygame.draw.rect(screen, (253, 255, 178), (590, 690, 100, 30))
    #Entrance to dungeon
    pygame.draw.rect(screen, (0, 0, 0), (590, 0, 100, 30))
    #Passage to northern room
    pygame.draw.rect(screen, (102, 51, 0), (608, 328, 64, 64))
    #Shield pedestal


def room2():
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    #Background and walls
    pygame.draw.rect(screen, (135, 130, 120), (590, 0, 100, 30))
    #Passage to northern room
    pygame.draw.rect(screen, (135, 130, 120), (590, 690, 100, 30))
    #Passage to southern room


running = True
while running:
    pygame.display.flip()

    room1()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                charPosY -= 10
            if event.key == pygame.K_a:
                charPosX -= 10
            if event.key == pygame.K_s:
                charPosY += 10
            if event.key == pygame.K_d:
                charPosX += 10

pygame.quit()
quit()
