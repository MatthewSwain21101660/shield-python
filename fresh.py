import sys

import pygame

pygame.init()
# importing and initialising the required libraries

screen = pygame.display.set_mode((1280, 720))
# Setting the resolution

charPosX = 615
charPosY = 580
charSpeed = 1
direction = "north"
roomNum = 1
pickedUpShield = False
background = pygame.image.load("i01_wall background.jpg")
locked = True


enemyPosX = 190
enemyPosy = 500
enemyAlive = True
projectileCount = 0
projectilePosX = enemyPosX + 50
projectilePosY = enemyPosy + 22
travelling = "east"
deflect = False

# Setting up global variables


running = True
while running:
    pygame.display.flip()

    print(charPosX, charPosY, roomNum, pickedUpShield, projectileCount)

    if roomNum == 1:
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
            # Top left side of player                            Top right of player                                        Bottom left side of player                            Bottom right side of player
            pickedUpShield = True

        if 590 < charPosX < 690 and charPosY < 31:
            if pickedUpShield:
                roomNum = 2
                charPosX = 615
                charPosY = 580
            else:
                print("You should probably get that shield first")

        if 590 <= charPosX <= 690 and charPosY >= 640:
            print("You can't leave yet, you still have a job to do")

    elif roomNum == 2:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
        # Background and walls
        pygame.draw.rect(screen, (135, 130, 120), (590, 0, 100, 30))
        # Passage to northern room
        pygame.draw.rect(screen, (135, 130, 120), (590, 690, 100, 30))
        # Passage to southern room


        if 590 < charPosX < 690 and charPosY < 31:
            if not locked:
                roomNum = 1
                charPosX = 615
                charPosY = 580
            else:
                print("It's locked, you need a key")

        if 590 <= charPosX <= 690 and charPosY >= 640:
            roomNum = 1
            charPosX = 615
            charPosY = 580



        if enemyAlive:
            pygame.draw.rect(screen, (255, 0, 0), (enemyPosX, enemyPosy, 50, 50))
            # Drawing the enemy

            if projectileCount == 300:
                projectileCount = 0
                projectilePosX = enemyPosX + 52
                projectilePosY = enemyPosy + 22
                travelling = "east"
                deflect = False

            if projectileCount < 300 and deflect == False:
                pygame.draw.rect(screen, (255, 255, 0), (projectilePosX, projectilePosY, 5, 5))
                projectilePosX += 1

            if deflect:
                pygame.draw.rect(screen, (255, 255, 0), (projectilePosX, projectilePosY, 5, 5))
                projectilePosX -= 1

            if projectilePosX > charPosX and projectilePosY > charPosY and direction == "west":
                deflect = True

            if projectilePosX > enemyPosX and projectilePosY > enemyPosy and deflect == True:
                enemyAlive = False

            projectileCount += 1
            # enemy deflection is very broken, when deflecting, instantly kills the enemy, can be above the enemy and it still counts as deflecting

    elif roomNum == 3:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
        # Background and walls



    if pickedUpShield:
        if direction == "north":
            pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
            pygame.draw.rect(screen, (255, 188, 0), (charPosX, charPosY, 50, 5))

        if direction == "east":
            pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
            pygame.draw.rect(screen, (255, 188, 0), (charPosX + 51, charPosY, 5, 50))

        if direction == "south":
            pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
            pygame.draw.rect(screen, (255, 188, 0), (charPosX, charPosY + 51, 50, 5))

        if direction == "west":
            pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
            pygame.draw.rect(screen, (255, 188, 0), (charPosX, charPosY, 5, 50))

    else:
        pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))




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
    # Movement for when the player presses the "w" key

    if keys[pygame.K_a]:
        charPosX -= charSpeed
        direction = "west"
    # Movement for when the player presses the "a" key

    if keys[pygame.K_s]:
        charPosY += charSpeed
        direction = "south"
    # Movement for when the player presses the "s" key

    if keys[pygame.K_d]:
        charPosX += charSpeed
        direction = "east"
    # Movement for when the player presses the "d" key

    # if the player wanted the character to move they had to press the key everytime. This change allows the player
    # to hold the key https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down

pygame.quit()
quit()

# had problem with game not running, turns out there were several python files in the same folder and it was trying
# to run all of them


# scrap code
# def room1(shieldPickedUp, currentRoom, charPositionX, charPositionY):
#   screen.blit(background, (0, 0))
#  # Image of wall rather than a solid colour
# # https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
# pygame.draw.rect(screen, (128, 138, 135), [30, 30, 1220, 660])
# Background and walls
# pygame.draw.rect(screen, (253, 255, 178), (590, 690, 100, 30))
# Entrance to dungeon
# pygame.draw.rect(screen, (0, 0, 0), (590, 0, 100, 30))
# Passage to northern room
# pygame.draw.rect(screen, (102, 51, 0), (608, 328, 64, 64))
# Shield pedestal
# pygame.draw.rect(screen, (102, 51, 0), (615, 335, 50, 50))

#    if not pickedUpShield:
#        pygame.draw.rect(screen, (255, 188, 0), (615, 335, 50, 50))

#    if 615 <= charPosX <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX + 50 <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX <= 715 and 335 <= charPosY <= 385 and 615 <= charPosX <= 715 and 335 <= charPosY <= 385:
# Top left side of player                             Top right of player                                        Bottom left side of player                            Bottom right side of player
#        shieldPickedUp = True

# if 590 < charPosX < 690 and charPosY < 30:
#    if pickedUpShield:
#        currentRoom = 2
#        charPositionX = 610
#        charPositionY = 630
#    else:
#        print("You should probably get that shield first")

#    if 590 <= charPosX <= 690 and charPosY >= 640:
#        print("You can't leave yet, you still have a job to do")
# room1(pickedUpShield, roomNum, charPosX, charPosY)
# rather than having each room as a function, perhaps have them as a switch statement in the main running loop,
# then dont have to worry about scope and whether the function can access or change a variable or not
#
# def room2():
#     screen.blit(background, (0, 0))
#     pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
#     # Background and walls
#     pygame.draw.rect(screen, (135, 130, 120), (590, 0, 100, 30))
#     # Passage to northern room
#     pygame.draw.rect(screen, (135, 130, 120), (590, 690, 100, 30))
#     # Passage to southern room
#
#
# def room3():
#     screen.blit(background, (0, 0))
#     pygame.draw.rect(screen, (169, 169, 169), [30, 30, 1220, 660])
#     # Background and walls
#
#     def player():
#     if not pickedUpShield:
#         pygame.draw.rect(screen, (0, 0, 255), (charPosX, charPosY, 50, 50))
#     #else:
#      #   pygame.draw.rect(screen, (255, 188, 0), (charPosX + 51, charPosY, 5))
#     # program does not start and gives out an error if pickedUpShield = true
