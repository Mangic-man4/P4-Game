import pygame, random, sys
from pygame.locals import *
pygame.init() 


#Display/Screen
screen_width = 1550
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
dispSurf = screen
pygame.display.set_caption("AI game 0.2")


"""
########################
-----BROKEN-----

Enemies
(line 92)
Enemy movement
Enemy collision? (at the start the first few secs?)
Either enemy or player x & y pos
-----BROKEN-----
#########################
"""


#Camera
class Camera:
    def __init__(self, width, height):
        height = screen_height
        width = screen_width
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height


    #Camera stuff
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)


    #Move camera
    def update(self, target):
        x = -target.rect.x + int(self.width / 2)
        y = -target.rect.y + int(self.height / 2)
        #print('Cam1', x,y)

        #Limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        #print('Cam2', x,y)
        x = max(-(self.width - 1280), x)  # right
        y = max(-(self.height - 720), y)  # bottom
        #print('Cam3', x,y)
        self.camera = pygame.Rect(x, y, self.width, self.height)


#Handle all entities/sprites? (background, player, enemies...)
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print('Entity', x,y)


#Player
class Player(Entity):
    def __init__(self, x, y, image, bounds):
        super().__init__(x, y, image)
        self.bounds = bounds


    #Movement
    def update(self, *args):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        elif key[pygame.K_a]:
            self.rect.x -= 5
        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        elif key[pygame.K_d]:
            self.rect.x += 5
        if key[pygame.K_UP]:
            self.rect.y -= 5
        elif key[pygame.K_w]:
            self.rect.y -= 5
        if key[pygame.K_DOWN]:
            self.rect.y += 5
        elif key[pygame.K_s]:
            self.rect.y += 5


        #Limit movement to map
        self.rect.x = max(self.bounds.left, self.rect.x)
        self.rect.x = min(self.bounds.right - self.rect.width, self.rect.x)
        self.rect.y = max(self.bounds.top, self.rect.y)
        self.rect.y = min(self.bounds.bottom - self.rect.height, self.rect.y)

#Background
class Background(Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


#Enemies
class Enemy(Entity):
    def __init__(self, x, y, image, player_x, player_y, bounds):
        super().__init__(x, y, image)
        self.image = image
        self.bounds = bounds
        self.x = x
        self.y = y
        print('Enemy',x,y)
        self.rect = self.image.get_rect()
        self.rect.x = self.x #random.randint(0, screen_width)
        self.rect.y = self.y #random.randint(0, screen_height)
        self.player_x = player_x
        self.player_y = player_y
        self.speed = 1.5

         
    #Enemy movement
#    def update(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        if player_x < self.x:
            self.x -= self.speed
        elif player_x > self.x:
            self.x += self.speed
        if player_y < self.y:
            self.y -= self.speed
        elif player_y > self.y:
            self.y += self.speed
        if self.x < self.bounds[0]:
            self.x = self.bounds[0]
        elif self.x > self.bounds[2]:
            self.x = self.bounds[2]
        if self.y < self.bounds[1]:
            self.y = self.bounds[1]
        elif self.y > self.bounds[3]:
            self.y = self.bounds[3]
        self.rect.x = self.x
        self.rect.y = self.y


        #Enemy moves back to spawn if it hits the player's spawn
        self.spawn_x = x
        self.spawn_y = y
        if self.rect.x <= player_x + 100 and self.rect.x >= player_x - 100 and self.rect.y <= player_y + 100 and self.rect.y >= player_y - 100:
            self.rect.x = self.spawn_x
            self.rect.y = self.spawn_y


#Game loop, variables
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()    
    clock.tick(120)
    time_elapsed = 0

    enemy_image = pygame.Surface((30, 50))
    player_image = pygame.Surface((30, 50))
    Enemy_collisions=0
    x = random.randint(0, screen_width - enemy_image.get_width())
    y = random.randint(0, screen_height - enemy_image.get_height())
    all_sprites = pygame.sprite.Group()
    
    background = Background(0, -120, pygame.image.load("background1.png"))
    bounds = pygame.Rect(0, -119, screen_width + 270, screen_height)
    player = Player(100, 100, player_image, bounds)
    enemy = Enemy(x, y, enemy_image, player.rect.x, player.rect.y, bounds)
    enemies = [Enemy(x, y, enemy_image, player.rect.x, player.rect.y, bounds) for i in range(5)]
    
    all_sprites.add(background)
    all_sprites.add(player)
    all_sprites.add(enemy)
    camera = Camera(screen_width, screen_height)
    
    player_x = player.rect.x
    player_y = player.rect.y
    enemyx = enemy.rect.x 
    enemyy = enemy.rect.y  


    #Create a list to store the enemy sprites
    enemies = []

    #Generate a random position for each enemy
    for i in range(5):
            enemies.append(Enemy(x, y, enemy_image, player.rect.x, player.rect.y, bounds))


    #Check if running
    running = True
    while running:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              running = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 running = False
        if not running:
           pygame.quit()
           sys.exit()
        dt = clock.tick() 
        time_elapsed += dt

        #Update player position
        player.update()

        
        #Update enemy AI
        for enemy in enemies:
            enemy.update(player.rect.x, player.rect.y)

        enemy.player_x = player_x
        enemy.player_y = player_y

       #Check for collision with enemies
        player_rect = player.rect
        for enemy in enemies:
            enemy_rect = enemy.rect
            if player_rect.colliderect(enemy_rect):
                Enemy_collisions += 1
                print("Player collided with enemy!", '(',Enemy_collisions,')',sep='')



        #Print player and enemy positions
        if time_elapsed > 1: 
            print("Player position:", player.rect.x, player.rect.y)
            print("Enemy position:", enemy.rect.x, enemy.rect.y)
            time_elapsed = 0



        #Update sprites on screen and the camera
        all_sprites.update(player.rect.x, player.rect.y)
        for enemy in enemies:
            enemy.update(player_x, player_y)
        camera.update(player)
        all_sprites.draw(screen)


        screen.fill((30, 180, 20))
        screen.blit(background.image, camera.apply(background))
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))        
        pygame.display.flip()


        #FPS
        clock.tick(60)


    pygame.quit()


#Start game loop
if __name__ == '__main__':
    main()



#fix screen warp (not necessary if making game idea below)
#fix enemies (bruh) 
#change enemy movement into stationary, back-forth and up-down
#fix jump (not necessary if making game idea below)
#change point event into a timer thing OR if adding a point collectible then show both pts and time

#idea: ghost chasing player through a (top-down) corridor maze (movemet good?)

#check 'AI code dump.py' for movement and camera testing

"""
#Game loop, variables
def main():
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
bounds = screen.get_rect()
running = True


#Player
player = Player(600, 400, pygame.image.load("player.png").convert(), bounds)

#Enemies
enemy_image = pygame.image.load("enemy.png").convert()
enemy1 = Enemy(300, 300, enemy_image, player.rect.x, player.rect.y, bounds)
enemy2 = Enemy(800, 300, enemy_image, player.rect.x, player.rect.y, bounds)
enemy3 = Enemy(1200, 300, enemy_image, player.rect.x, player.rect.y, bounds)
enemies = [enemy1, enemy2, enemy3]

#Background
background_image = pygame.image.load("background.png").convert()
background = Background(0, 0, background_image)

#Sprites
entities = pygame.sprite.Group()
entities.add(background)
entities.add(player)
entities.add(enemy1)
entities.add(enemy2)
entities.add(enemy3)

#Camera
camera = Camera(screen_width, screen_height)

#Game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #Player update
    player.update()

    #Enemy update
"""