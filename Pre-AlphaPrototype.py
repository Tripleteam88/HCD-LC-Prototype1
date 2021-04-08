import pygame
from GameClasses import Player, Bullet
from UtilityFunctions import check_events, controls, bullet_control, draw_bullets

pygame.init()

# ------------------------------------------
# WINDOW // Constants should be all caps
WIDTH = 1000
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window variable is created // This method takes a tuple argument for the window's size
# ------------------------------------------

# ------------------------------------------
# Control Variables
FPS = 60
speed = 6
# ------------------------------------------

# ------------------------------------------
# Player Object
player = Player('Assets\Player\IDLE\PlayerDownIDLE.png', WIDTH/2, HEIGHT/2)
# Player animations
WalkRight = [pygame.image.load('Assets\Player\Animations\Right\R1.png'), pygame.image.load('Assets\Player\Animations\Right\R2.png'), pygame.image.load('Assets\Player\Animations\Right\R3.png'),
pygame.image.load('Assets\Player\Animations\Right\R4.png'), pygame.image.load('Assets\Player\Animations\Right\R5.png'), pygame.image.load('Assets\Player\Animations\Right\R6.png'),
pygame.image.load('Assets\Player\Animations\Right\R7.png'), pygame.image.load('Assets\Player\Animations\Right\R8.png')]
WalkLeft = []
WalkDown = []
WalkUp = []
# ------------------------------------------

# ------------------------------------------
# Combat variables
bullet_list = []

# ------------------------------------------

# ------------------------------------------
# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# ------------------------------------------


# Main draw function
def draw():
    WIN.fill(BLUE)

    draw_bullets(bullet_list, WIN)
    player.draw(WIN)

    pygame.display.update()


# Main game loop
def main():

    # Clock object is created
    clock = pygame.time.Clock()

    # Main loop will is where all game logic is handled
    run = True
    while run:
        clock.tick(FPS)
    


        # Custom function that checks events
        # Currently will only close the window if user kills the window
        check_events()

        # Custom function that checks pressed keys // Implementing controls
        controls(player, bullet_list, speed, WIN, WalkRight)

        # Bullet control function // Loops through bullets and applies changes
        if bullet_list != []:
            bullet_control(bullet_list, WIN)
        print(player.img)
        draw()

main()