import pygame

pygame.init()
# importing and initialising the required libraries

screen = pygame.display.set_mode((1280, 720))
# Setting the resolution

charPosX = 610
charPosY = 630
charSpeed = 0.4
direction = "north"
roomNum = 1
pickedUpShield = False


# Setting up global variables


def room1(shieldPickedUp):
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    # Background and walls
    pygame.draw.rect(screen, (253, 255, 178), (590, 690, 100, 30))
    # Entrance to dungeon
    pygame.draw.rect(screen, (0, 0, 0), (590, 0, 100, 30))
    # Passage to northern room
    pygame.draw.rect(screen, (102, 51, 0), (608, 328, 64, 64))
    # Shield pedestal

    if not shieldPickedUp:
        pygame.draw.rect((255, 188, 0), (608, 328, 64, 64))

    if charPosX >= 615 & charPosX <= 715 & charPosY >= 335 % charPosY <= 385:
        shieldPickedUp = True


def room2():
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    # Background and walls
    pygame.draw.rect(screen, (135, 130, 120), (590, 0, 100, 30))
    # Passage to northern room
    pygame.draw.rect(screen, (135, 130, 120), (590, 690, 100, 30))
    # Passage to southern room


def room3():
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    # Background and walls


def player():
    pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))


def wallUp(charPosY, charSpeed):
    if charPosY <= 30:
        charSpeed = 0;
        charPosY = charPosY + 1;


def wallDown(charPosY, charSpeed):
    if charPosY >= 640:
        charSpeed = 0;
        charPosY = charPosY - 1;


def wallLeft(charPosX, charSpeed):
    if charPosX <= 30:
        charSpeed = 0;
        charPosX = charPosX + 1;


def wallRight(charPosX, charSpeed):
    if charPosX >= 1200:
        charSpeed = 0;
        charPosX = charPosX - 1;


# Checks to see whether the player has collided with any of the coordinates that are the walls, and if they have,
# moves them back

running = True
while running:
    pygame.display.flip()

    room1(pickedUpShield)

    player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = "north"
        charPosY -= charSpeed
    if keys[pygame.K_a]:
        charPosX -= charSpeed
        direction = "west"
    if keys[pygame.K_s]:
        charPosY += charSpeed
        direction = "south"
    if keys[pygame.K_d]:
        charPosX += charSpeed
        direction = "east"

    # if the player wanted the character to move they had to press the key everytime. This change allows the player
    # to hold the key https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down

    wallUp(charPosY, charSpeed)
    wallDown(charPosY, charSpeed)
    wallLeft(charPosX, charSpeed)
    wallRight(charPosX, charSpeed)

pygame.quit()
quit()

# had problem with game not running, turns out there were several python files in the same folder and it was trying
# to run all of them
