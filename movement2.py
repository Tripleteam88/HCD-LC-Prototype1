import pygame
from PlayerClass import Player
pygame.init()

# First I must create a window
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# Colours
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Control Varibles
FPS = 60
speed = 6

# PLayer
#player_img = pygame.image.load('minichief.png')
player = Player('minichief.png', WIDTH/2, HEIGHT/2)


#Note that a pygame must have both a draw and update function
# Create a seperatate draw function
def draw_window():
    WIN.fill(BLACK)
    # blit method draws a 'surface' onto the screen
    # blit can take an image and a coordinate as a parameter
    
    # Custom Player draw method//Takes a surface as a parameter//The window surface in this case
    player.draw(WIN)

    pygame.display.update()



# Now I make my main loop
def main():
    clock = pygame.time.Clock()
    
    # This begins the infinite loop//Loops until broken out of
    run = True
    while run:
        clock.tick(FPS)
        # This for loop will check the current events that are happening 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
    
        # Movement keys
        if keys[pygame.K_a]:
            player.x -= speed
        if keys[pygame.K_d]:
            player.x += speed
        if keys[pygame.K_w]:
            player.y -= speed
        if keys[pygame.K_s]:
            player.y += speed
        
        

        # Arrow keys//Directional keys//Test
        if keys[pygame.K_m]:
            ##pygame.transform.rotate(player.img, 180)
            player.rotate(30)
            pass    
            
        '''
        if keys[pygame.K_RIGHT]:
            player.ang = speed
        if keys[pygame.K_UP]:
            player.ang = speed
        if keys[pygame.K_DOWN]:
            player.ang = speed
        '''

        draw_window()

    # CLoses window at the end of the loop
    pygame.quit()

#Calls main function
main()