"""
All game objects will be rewritten in this file.
They will all be rewritten to be more efficient and inherit from the Pygame Sprite Class.
"""

import pygame


class Player(pygame.sprite.Sprite):
    '''
    Player class inherits from the spite class to add more base functionality.
    The Player object is a type of sprite.
    '''

    def __init__(self, image):
        '''
        Player class takes all the same parameters as a normal sprite.
        '''

        # Creates a sprite using the instance of the player
        pygame.sprite.Sprite.__init__(self)

        # -----------------------------------------
        # Sprite parameters -----------------------
        # -----------------------------------------
        self.image = image

        # -----------------------------------------



    def Walking(self):
        pass