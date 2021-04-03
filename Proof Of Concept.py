import pygame
from Classes import Player, Bullet
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
speed = 5

# PLayer
#player_img = pygame.image.load('minichief.png')
player = Player('ArrowU.png', WIDTH/2, HEIGHT/2)

# Combat Variables
bullet_list = []


#Note that a pygame must have both a draw and update function
# Create a seperatate draw function
def draw_window():
    WIN.fill(BLACK)
    # blit method draws a 'surface' onto the screen
    # blit can take an image and a coordinate as a parameter
    
    # Custom Player draw method//Takes a surface as a parameter//The window surface in this case
    player.draw(WIN)
    if bullet_list != []:
        for bullet in bullet_list:
                bullet.draw(WIN)


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
        if keys[pygame.K_LEFT]:
            ##pygame.transform.rotate(player.img, 180)
            ##player.rotate(30)

            # Try the animation instead, there may be no need to rotate
            player.animate('ArrowL.png')
            bullet_list.append(Bullet('bullet.png', player.x, player.y, 'L'))
            
            # Remember to use different bullet pictures to account for where it should be facing
            


        if keys[pygame.K_RIGHT]:
           player.animate('ArrowR.png')
           bullet_list.append(Bullet('bullet.png', player.x, player.y, 'R'))

        if keys[pygame.K_UP]:
          player.animate('ArrowU.png')
          bullet_list.append(Bullet('bullet.png', player.x, player.y, 'U'))

        if keys[pygame.K_DOWN]:
          player.animate('ArrowD.png')
          bullet_list.append(Bullet('bullet.png', player.x, player.y, 'D'))

       

        if bullet_list:
            for bullet in bullet_list:
                bullet.move()

        draw_window()

    # CLoses window at the end of the loop
    pygame.quit()

#Calls main function
main()