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

        This method is called once per frame and will manage player logic.
        The controls method is only called here so will run once per frame as well.
        This method will not handle player movement or combat directly, instead it will "coordinate" other methods that do so here.
        Thus encapsulating player logic into one update method. 

        IMPORTANT:
        DESCRIPTION MISSING
        '''
        self.controls()

        pass

    def controls(self):
        '''
        Handles the player control logic
        
        Only Player movement is controled here.

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