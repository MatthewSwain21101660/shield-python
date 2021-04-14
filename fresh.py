import sys

import pygame

pygame.init()
# importing and initialising the required libraries

screen = pygame.display.set_mode((1280, 720))
# Setting the resolution

charPosX = 610
charPosY = 630
charSpeed = 1
direction = "north"
roomNum = 1
pickedUpShield = True
background = pygame.image.load("i01_wall background.jpg")


# Setting up global variables


def room1(shieldPickedUp, currentRoom, charPositionX, charPositionY):
    screen.blit(background, (0, 0))
    # Image of wall rather than a solid colour
    # https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
    pygame.draw.rect(screen, (128, 138, 135), [30, 30, 1220, 660])
    # Background and walls
    pygame.draw.rect(screen, (253, 255, 178), (590, 690, 100, 30))
    # Entrance to dungeon
    pygame.draw.rect(screen, (0, 0, 0), (590, 0, 100, 30))
    # Passage to northern room
    pygame.draw.rect(screen, (102, 51, 0), (608, 328, 64, 64))
    # Shield pedestal
    pygame.draw.rect(screen, (102, 51, 0), (615, 335, 50, 50))

    if not pickedUpShield:
        pygame.draw.rect(screen, (255, 188, 0), (615, 335, 50, 50))

    if 615 <= charPosX <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX + 50 <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX <= 715 and 335 <= charPosY <= 385:
        # Top left side of player                             Top right of player                                        Bottom left side of player                            Bottom right side of player
        shieldPickedUp = True

    if 590 < charPosX < 690 and charPosY < 30:
        if pickedUpShield:
            currentRoom = 2
            charPositionX = 610
            charPositionY = 630
        else:
            print("You should probably get that shield first")

    if 590 <= charPosX <= 690 and charPosY >= 640:
        print("You can't leave yet, you still have a job to do")


def room2():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    # Background and walls
    pygame.draw.rect(screen, (135, 130, 120), (590, 0, 100, 30))
    # Passage to northern room
    pygame.draw.rect(screen, (135, 130, 120), (590, 690, 100, 30))
    # Passage to southern room


def room3():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
    # Background and walls


def player():
    if not pickedUpShield:
        pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
    #else:
     #   pygame.draw.rect(screen, (255, 188, 0), (charPosX + 51, charPosY, 5))
    # program does not start and gives out an error if pickedUpShield = true


# Checks to see whether the player has collided with any of the coordinates that are the walls, and if they have,
# moves them back

running = True
while running:
    pygame.display.flip()

    room1(pickedUpShield, roomNum, charPosX, charPosY)
    # rather than having each room as a function, perhaps have them as a switch statement in the main running loop,
    # then dont have to worry about scope and whether the function can access or change a variable or not

    player()

    charSpeed = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if charPosY <= 30:
        charSpeed = 0
        charPosY = charPosY + 1
    # Collision detection for northern wall

    if charPosY >= 640:
        charSpeed = 0
        charPosY = charPosY - 1
    # Collision detection for southern wall

    if charPosX <= 30:
        charSpeed = 0
        charPosX = charPosX + 1
    # Collision detection for eastern wall

    if charPosX >= 1200:
        charSpeed = 0
        charPosX = charPosX - 1
    # Collision detection for western wall

    # Checks to see whether the player has collided with any of the coordinates that are the walls, and if they have,
    # moves them back

    # problem where the wall collision would not work if it was a separate method

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

pygame.quit()
quit()

# had problem with game not running, turns out there were several python files in the same folder and it was trying
# to run all of them
