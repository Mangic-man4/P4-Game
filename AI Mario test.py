import pygame
import sys     # sys-module will be needed to exit the game
from pygame.locals import * # imports the constants of pygame
pygame.init()  # initializes pygame
##### NEW #####
import random  # random module will be needed for random numbers
##### NEW #####


# the display surface
screen_width = 960
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("AI Mario test")

# the Surface objects
background = pygame.image.load("background.png").convert()
player = pygame.image.load("player.png").convert()
enemy_image = pygame.image.load("enemy.png").convert()
enemy = enemy_image
player_x = 50
player_y = 50
background_x = 0
background_y = 0
x=0


# Create enemy list
enemies = []

# Add enemies to the list
for i in range(5):
    enemies.append({"x": random.randint(0, screen_width), "y": random.randint(0, screen_height), "speed": 2})

# Create rectangles for player and enemies for collision detection
player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
for enemy in enemies:
    enemy["rect"] = pygame.Rect(enemy["x"], enemy["y"], enemy_image.get_width(), enemy_image.get_height())

# empty black Surface(width, height)
rectangle = pygame.Surface((300,50))

# RGB-colors are tuples (r,g,b), where 0<r,g,b<255
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,0,130)

# Surface objects can be filled with a color using fill() method
rectangle.fill(red)

# Surface objects can be added to the display surface with blit() method
# blit(Surface,(x,y)) adds "Surface" into coordinates (x,y)=(left, top)
screen.blit(background, (0,0))
#screen.blit(enemy, (0,0))
screen.blit(player, (400,500))
screen.blit(rectangle, (0,200))

# the display surface needs to be updated for the blitted Surfaces to become visible
# pygame.display.update() would do the same
pygame.display.flip()

# Surface.get_rect() method returns the Rect object of "Surface"
# Rect objects are needed to move Surfaces and for collision detection
# Rect(left, top, width, height) contains left/top-coordinates and width/height
#enemyarea = enemy.get_rect()
playerarea = player.get_rect()
rectangleArea = rectangle.get_rect()

# get_rect() method by default sets the left-top corner to (0,0)
# player and rectangle were not blitted into (0,0)
# the left and top coordinates have to be changed with dot notation
playerarea.left = 400
playerarea.top = 500
rectangleArea.left = 0
rectangleArea.top = 200

# speed contains the [x,y]-speed of the enemy in pixels
speed = [1,1]





######################################
# NEW!
######################################

# rgba-colors have alpha value 0<a<255, which determines the transparency level
# convert_alpha() recognizes the alpha values if the picture has them
# set_colorkey(r,g,b) makes the given rgb-color of a surface transparent
# set_alpha(a) will set the whole surface transparent with value a
redAlpha = (255,0,0,150)
rectangle = pygame.Surface((300,50)).convert_alpha()
rectangle.fill(redAlpha)
player = pygame.image.load("playerAlpha.png").convert_alpha()
#enemy.set_colorkey((0,0,0))
player.set_alpha(200)
#pointball = pygame.image.load("pointball.png").convert() # collectable ball

# Event() function will create Event-object of a given type
# pygame.USEREVENT = 32847 is preferred type
# if you need more events, use pygame.USEREVENT+1, pygame.USEREVENT+2, etc.
pointEvent = pygame.event.Event(pygame.USEREVENT)

# set_timer() puts pointEvent into the event queue every 2000 milliseconds
pygame.time.set_timer(pointEvent,2000)

# some variables
pointballList = [] # list of pointballs
coordList = [] # list of their coordinates
speedList = [] # list of their speeds
speed2 = [1,1] # the speed of the pointballs
points = 0 # variable that keeps tracking the points
jump = 0 # variable to implement jumping
air = True # variable to check if mario is on the air
clock = pygame.time.Clock() # Clock object can set the framerate of the game
#boom = pygame.mixer.Sound("boom.wav") # Sound object from waw/ogg-file
#house = pygame.mixer.music.load("house.mp3") # loads background music
#pygame.mixer.music.play(loops=-1) # play() function will start the music
# sounds might create dll-errors, they have nothing to do with pygame

# font module is used to create text into the game
# pygame.font.get_fonts() returns a list of all the available fonts
# SysFont(font,size) creates a font object of given font and size
# font.render(text,antialiased,color) creates Surface object from the font
fontEnd = pygame.font.SysFont('arial', 90)
fontPoint = pygame.font.SysFont('cambria', 40)
textEnd = fontEnd.render('GAME OVER', True, blue)
textPoint = fontPoint.render('Points: '+str(points), True, green)

######################################
# NEW!
######################################







# the game loop which runs until sys.exit()
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
##### NEW #####
        """  if event.type == pygame.USEREVENT:
            # pygame.USEREVENT was added to the queue every 2000 milliseconds
            # new pointball is appended to the lists
            pointballList.append(pointball)
            coordList.append(pointball.get_rect())
            speedList.append([speed2[0],speed2[1]])"""
##### NEW #####



    # enemy will be moved by speed=[1,1] in every iteration
    # move_ip([x,y]) changes the Rect-objects left-top coordinates by x and y
    #enemyarea.move_ip(speed)


    # enemy bounces from the edges of the display surface
    #if enemyarea.left < 0 or enemyarea.right > screen_width: # enemy is vertically outside the game
    #    speed[0] = -speed[0] # the x-direction of the speed will be converted
    #if enemyarea.top < 0 or enemyarea.bottom > screen_height: # enemy is horizontally outside the game
    #    speed[1] = -speed[1] # the y-direction of the speed will be converted

    """
    # enemy bounces from the rectangle
    if rectangleArea.colliderect(playerarea):
    # a.colliderect(b) returns True if Rect-objects a and b overlap
        if rectangleArea.colliderect(playerarea.move(-speed[0],0)):
        # if the enemy came from vertical direction
            speed[1] = -speed[1] # the y-direction of the speed will be converted
        else:
        # otherwise the enemy came from horizontal direction
            speed[0] = -speed[0] # the x-direction of the speed will be converted
    """

    # player can be moved with left/right/up/down-keys
    # get.pressed() function gives a boolean list of all the keys if they are being pressed
   # Move player based on key presses
    keys = pygame.key.get_pressed()


    #Original 'mario' movement
    if keys[pygame.K_LEFT]:          # if left-key is true in the list
        playerarea.move_ip((-2,0))  # mario will be moved one pixel left
    elif keys[pygame.K_a]:          
        playerarea.move_ip((-2,0)) 
    if keys[pygame.K_RIGHT]:
        playerarea.move_ip((2,0))
    elif keys[pygame.K_d]:
        playerarea.move_ip((2,0))
    """if keys[pygame.K_DOWN]:
        playerarea.move_ip((0,1))
    elif keys[pygame.K_s]:
        playerarea.move_ip((0,1))
    if keys[pygame.K_UP]:
        playerarea.move_ip((0,-1)) 
    elif keys[pygame.K_w]:
        playerarea.move_ip((0,-1))
    """







######################################
# NEW!
######################################

    # player will appear on the other side of the display surface
    if playerarea.left > screen_width:  # if player is over the right side
        playerarea.right=0       # right coordinate goes to 0
    if playerarea.right < 0:
        playerarea.left = screen_width
    if playerarea.top > screen_height:
        playerarea.bottom = 0
    if playerarea.bottom < 0:
        playerarea.top = screen_height

    # player will bounce from the edges of the display surface
    if playerarea.left > screen_width:           # if player is over the right side
        playerarea.left=playerarea.left-70 # move 70 pixels left
    if playerarea.right < 0:
        playerarea.right=playerarea.right+70
    if playerarea.top > screen_height:
        playerarea.top=playerarea.top-70
    if playerarea.bottom < 0:
        playerarea.bottom=playerarea.bottom+70

    # player will jump if you press space button
    if keys[pygame.K_SPACE] and air==False: # if player is not in air
        jump = 12 # vertical speed will go to 15
        air = True # player is now in the air
    if air == True: # if player is in the air
        playerarea.move_ip((0,-jump)) # player will move vertically by jump
        jump = round(jump - 0.2,1) # jump will decrease 0.2 pixels
    if playerarea.bottom >= screen_height: # if player hits bottom, jumping ends
        air = False

    """
    # if player overlaps enemy, the game will end
    if playerarea.colliderect(enemy["rect"]):
        screen.blit(textEnd,(300, 250))
        pygame.display.update()
        # pygame.quit() would close the window, no time see the "game over"
        sys.exit()
    """

    # moves all the pointballs and bounces them from the edges
    for i in range(0,len(pointballList)):
        coordList[i].move_ip(speedList[i])
        if coordList[i].left < 0 or coordList[i].right > screen_width:
            speedList[i][0] = -speedList[i][0]
        if coordList[i].top < 0 or coordList[i].bottom > screen_height:
            speedList[i][1] = -speedList[i][1]

    """
    # player collects pointballs and gets randomly 50-100 points
    j=0 # variable that tracks the number of deleted balls
    for i in range(0,len(pointballList)):
        if playerarea.colliderect(coordList[i-j]): # player overlaps with ball
            pointballList.pop(i-j) # ball is deleted from all the lists
            coordList.pop(i-j)
            speedList.pop(i-j)
            j = j+1
            points = points + random.randint(50,100) # random 50-100 points
            boom.play() # boom sound is played
            """


    # text to show the current points
    textPoint = fontPoint.render('Points: '+str(points), True, green)

    # clock object and tick() method will set the frame rate per second
    clock.tick(260)
    # clock.get_fps() # returns the current frame rate of the game
    # pygame.time.get_ticks() # returns time passed from calling pygame.init()
    # pygame.time.wait(1000) # pauses the game for given milliseconds

######################################
# NEW!
######################################

    for enemy in enemies:
        if player_x < enemy["x"]:
            enemy["x"] -= enemy["speed"]
        elif player_x > enemy["x"]:
            enemy["x"] += enemy["speed"]
        if player_y < enemy["y"]:
            enemy["y"] -= enemy["speed"]
        elif player_y > enemy["y"]:
            enemy["y"] += enemy["speed"]
        enemy["rect"].x = enemy["x"]
        enemy["rect"].y = enemy["y"]

            # Check for collision with enemies
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_image.get_width(), enemy_image.get_height())
        if player_rect.colliderect(enemy_rect):
            x+=1
            print("Player collided with enemy!", x)



    screen.fill((0, 0, 0))
    # blits all the Surfaces in their new places
    screen.blit(background, (0,0)) # without this, moving characters would have a "trace"
    #screen.blit(enemy, enemyarea)
    screen.blit(player, playerarea)
    screen.blit(rectangle, rectangleArea)
##### NEW #####
    for i in range(0,len(pointballList)):
        screen.blit(pointballList[i], coordList[i]) # blits pointballs
    screen.blit(textPoint, (0,0)) # blits point calculator
##### NEW #####
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))
    # updating the display surface is always needed at the end of each iteration of game loop
    pygame.display.flip()