import pygame
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

# PLayer
player_img = pygame.image.load('minichief.png')



#Note that a pygame must have both a draw and update function
# Create a seperatate draw function
def draw_window():
    WIN.fill(BLACK)
    # blit method draws a 'surface' onto the screen
    # blit can take an image and a coordinate as a parameter
    WIN.blit(player_img, (WIDTH/2, HEIGHT/2))

    pygame.display.update()



# Now I make my main loop
def main():

    # This begins the infinite loop//Loops until broken out of
    run = True
    while run:
        # This for loop will check the current events that are happening 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    # CLoses window at the end of the loop
    pygame.quit()

#Calls main function
main()