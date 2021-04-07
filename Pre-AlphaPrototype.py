import pygame
from GameClasses import Player, Bullet
from UtilityFunctions import check_events, check_keys, bullet_control, draw_bullets

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
    WIN.fill(BLACK)

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
        # This for loop will check the current events that are happening

        # Custom function that checks events
        # Currently will only close the window if user kills the window
        check_events()

        # Custom function that checks pressed keys // Implementing controls
        check_keys(player, bullet_list, speed, WIN)

        # Bullet control function // Loops through bullets and applies changes
        if bullet_list != []:
            bullet_control(bullet_list, WIN)
        print(player.cooldown)
        draw()

main()