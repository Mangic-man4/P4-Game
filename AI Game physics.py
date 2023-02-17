import pygame
import sys     # sys-module will be needed to exit the game
from pygame.locals import * # imports the constants of pygame
pygame.init()  # initializes pygame
##### NEW #####
import random 

# Set screen size
screen = pygame.display.set_mode((800, 600))

level = pygame.image.load("level.jpg").convert()
mario = pygame.image.load("mario.png").convert()
fireball = pygame.image.load("fireball.png").convert()

# Set initial position and velocity for player
player_pos = [400, 300]
player_vel = [0, 0]

# Set gravity
gravity = 0.5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move player based on keys pressed
    if keys[pygame.K_LEFT]:
        player_vel[0] -= 0.1
    if keys[pygame.K_RIGHT]:
        player_vel[0] += 0.1
    if keys[pygame.K_UP]:
        player_vel[1] -= 0.1
    if keys[pygame.K_DOWN]:
        player_vel[1] += 0.1

    # Apply gravity to player
    player_vel[1] += gravity

    # Update player position based on velocity
    player_pos[0] += player_vel[0]
    player_pos[1] += player_vel[1]

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw player
    pygame.draw.circle(screen, (255, 255, 255), (int(player_pos[0]), int(player_pos[1])), 10)

    # Update display
    pygame.display.update()

# Exit pygame
while True:


    # loop to check if the user has closed the display window or pressed esc
    for event in pygame.event.get():  # list of all the events in the event queue
        if event.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display window closes
            sys.exit()    # the python program exits
        if event.type == KEYDOWN:     # if the player pressed down any key
            if event.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display window closes
                sys.exit()    # the python program exits