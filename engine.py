"""
All game objects,methods and related game functions will be rewritten in this file.
They will all be rewritten to be more efficient and objects will inherit from the Pygame Sprite Class.
"""

import pygame
pygame.init()
pygame.display.init()

# ========================================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game Classes //////////////////////////////////////
# ========================================================================================
class Player(pygame.sprite.Sprite):
    '''
    Player class inherits from the spite class to add more base functionality.
    The Player object is a type of sprite.
    '''

    def __init__(self, image, x, y):
        '''
        Player class takes all the same parameters as a normal sprite.
        '''

        # Creates a sprite using the instance of the player
        pygame.sprite.Sprite.__init__(self)

        # -----------------------------------------
        # Sprite parameters -----------------------
        # -----------------------------------------
        # Player Rect/Surface parameters ----------
        self.image = image
        # Automatically sets dimensions from image
        self.rect = self.image.get_rect()
        # Position parameters
        self.rect.x = x
        self.rect.y = y
        # -----------------------------------------

    def update(self):
        '''
        Controls player behaviour.

        IMPORTANT:
        DESCRIPTION MISSING
        '''
        pass

# =============================================================================================
# =============================================================================================




# =============================================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game functions ///////////////////////////////////////
# =============================================================================================

def window_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

# =============================================================================================
# =============================================================================================