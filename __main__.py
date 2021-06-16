import pygame
import engine   # No astrisk so engine functions can be easily identified 
from engine import Manager, Player, Bullet, Enemy

pygame.init()
pygame.display.init()


# ==============================================================
# \\\\\\\\\\\\\\\\\ Initial Game Variables /////////////////////
# ==============================================================
# -----------------------------------------
# Screen ----------------------------------
# -----------------------------------------
# WINDOW // Constants should be all caps
WIDTH = 1000
HEIGHT = 600
WIN = pygame.display.set_caption("HCD2: Pre-Alpha 0")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# ------------------------------------------


# ------------------------------------------
# Game Control Variables // Clock ----------
# ------------------------------------------
FPS = 60
clock = pygame.time.Clock()
# ------------------------------------------


# ------------------------------------------
# Player object ----------------------------
# ------------------------------------------
# Player Variables -------------------------
x = 100
y = 100
# ------------------------------------------
player = engine.Player(x, y, WIN)
# ------------------------------------------

# ------------------------------------------
# Enemies ----------------------------------
# ------------------------------------------
enemy_list = [Enemy('Assets\Enemies\Alien.png')]
# ------------------------------------------


# ------------------------------------------
# Game control ---------------------------
# ------------------------------------------
game = Manager(player, enemy_list)
# ------------------------------------------

# ------------------------------------------
# Colours ----------------------------------
# ------------------------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# ------------------------------------------
# ==============================================================
# \\\\\\\\\\\\\\\\ Initial Game Variables: END /////////////////
# ==============================================================



def main():
    """
    The main game function.
    The main game loop runs here.
    All game functions are called within this main function.
    """

    running = True  # Main game loop
    while running:
        clock.tick(FPS) # Sets game framerate
        WIN.fill(BLACK)     # Clears screen by filling it with a background colour

        player.draw(WIN)
        player.update(WIN)

        

        
        
        pygame.display.update()

   
      
        



    

main()  # Main game function is called