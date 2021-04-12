import pygame
from engine import *

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
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN = pygame.display.set_caption("HCD2: Pre-Alpha 0.1")
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
pass
# ------------------------------------------


# ------------------------------------------
# Combat control ---------------------------
# ------------------------------------------
pass
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

        window_event()

        pass



    pass

main()  # Main game function is called