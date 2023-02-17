import pygame
import random
import sys
from pygame.locals import *
pygame.init() # Initialize pygame

# Set screen dimensions
screen_width = 1550
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
dispSurf = screen
pygame.display.set_caption("AI game v0.1")

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.width / 2)
        y = -target.rect.y + int(self.height / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 1280), x)  # right
        y = max(-(self.height - 720), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)

# Load player image
player = pygame.image.load("player.png").convert()
player_x = 50
player_y = 480
player_speed = 5

# Load background image
background = pygame.image.load("background.png").convert()
background_x = 0
background_y = 0

#camera = screen.get_rect() 
#camera.center = 100, player_y

x=0
y=0
camera_x = 0
camera_y = 0
screen.blit(background, (0,0))
screen.blit(player, (400,500))
#screen.blit(background,(0 -CameraX,0 -CameraY))
#screen.blit(player,(x -CameraX,y -CameraY))
pygame.display.flip()
playerarea = player.get_rect()
playerarea.left = 400
playerarea.top = 500




jump = 0 # variable to implement jumping
air = True 
clock = pygame.time.Clock()
fps = clock.get_fps()

# Create enemy list
enemies = []

# Add enemies to the list
for i in range(1):
    enemies.append({"x": random.randint(0, screen_width), "y": random.randint(0, screen_height), "speed": 2})

# Load enemy image
enemy_image = pygame.image.load("enemy.png").convert()
enemy = enemy_image


# Create rectangles for player and enemies for collision detection
player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
for enemy in enemies:
    enemy["rect"] = pygame.Rect(enemy["x"], enemy["y"], enemy_image.get_width(), enemy_image.get_height())





# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if not running:
        pygame.quit()
        sys.exit()

    #camera.center = player_x, player_y

    # Move the camera based on the player's position
    #camera_x = player_rect.centerx - 400
    #camera_y = player_rect.centery - 300
    # Move player based on key presses
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
 #       CameraX += 10
 #      if x > screen_width /4 *3:
 #           CameraX += 10
    elif keys[pygame.K_d]:
        player_x += player_speed
 #       CameraX += 10
 #       if x > screen_width /4 *3:
 #           CameraX += 10
    if keys[pygame.K_UP]:
        player_y -= player_speed
    elif keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    elif keys[pygame.K_s]:
        player_y += player_speed
    """

    #Original 'mario' movement
    if keys[pygame.K_LEFT]:          # if left-key is true in the list
        playerarea.move_ip((-1,0))  # mario will be moved one pixel left
    elif keys[pygame.K_a]:          
        playerarea.move_ip((-1,0)) 
    if keys[pygame.K_RIGHT]:
        playerarea.move_ip((1,0))
    elif keys[pygame.K_d]:
        playerarea.move_ip((1,0))
    if keys[pygame.K_DOWN]:
        playerarea.move_ip((0,1))
    elif keys[pygame.K_s]:
        playerarea.move_ip((0,1))
    if keys[pygame.K_UP]:
        playerarea.move_ip((0,-1)) 
    elif keys[pygame.K_w]:
        playerarea.move_ip((0,-1))
    """


    if playerarea.left > screen_width:  # if mario is over the right side
        playerarea.right=0       # right coordinate goes to 0
    if playerarea.right < 0:
        playerarea.left = screen_width
    if playerarea.top > screen_height:
        playerarea.bottom = 0
    if playerarea.bottom < 0:
        playerarea.top = screen_height

    

    player_rect.x = player_x
    player_rect.y = player_y
    if keys[pygame.K_SPACE] and air==False: # if mario is not in air
        jump = 5 # vertical speed will go to 15
        air = True 
    if air == True: # if mario is in the air
        playerarea.move_ip((0,-jump)) # mario will move vertically by jump
        jump = round(jump - 0.2,1) # jump will decrease 0.2 pixels
    if playerarea.bottom >= screen_height: # if mario hits bottom, jumping ends
        air = False

    # Move enemies towards player
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
            print("Player collided with enemy!", '(',x,')',sep='')


    clock.tick(120)
    

    camera_x = player_x - 400

    

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(background, (background_x, background_y))  
    screen.blit(player, (player_x, player_y)) # (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))
    pygame.display.update()


#fix screen warp (not necessary if making game idea below)
#fix enemies (bruh)
#fix jump (not necessary if making game idea below)
#change point event into timer thing OR if adding a point collectible then show both pts and time

#idea: ghost chasing player through a (top-down) corridor maze (movemet good?)

#check 'AI code dump.py' for movement and camera testing


"""
    # Create enemy objects
    enemies = []
    enemy_image = "enemy.png"
    for i in range(1):
        x = random.randint(0, screen_width - enemy.get_width())
        y = random.randint(0, screen_height - enemy.get_height())
        enemy = Enemy(200, 200, pygame.Surface((30, 50)), player.rect.x, player.rect.y)
        enemies.append(enemy)
"""
