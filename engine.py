"""
All game objects,methods and related game functions will be rewritten in this file.
They will all be rewritten to be more efficient and objects will inherit from the Pygame Sprite Class.
"""

import pygame
from pygame import *
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

    def __init__(self, img, x, y):
        '''
        Player class takes all the same parameters as a normal sprite.
        '''

        # Creates a sprite using the instance of the player
        pygame.sprite.Sprite.__init__(self)

        # -----------------------------------------
        # Sprite parameters -----------------------
        # -----------------------------------------
        # Player Rect/Surface parameters ----------
        self.image = pygame.image.load(img).convert()
        # Automatically sets dimensions from image
        self.rect = self.image.get_rect()
        # Position parameters
        self.rect.x = x
        self.rect.y = y
        # -----------------------------------------
        # Movement and directional Parameters -----
        # -----------------------------------------
        # Speed 
        self.speed = 10
        # Movement
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        # Direction
        self.facing_up = False
        self.facing_down = True # Default direction value
        self.facing_right = False
        self.facing_left = False
        # -----------------------------------------

    
    def draw(self, WINDOW):
       WINDOW.blit(self.image, (self.rect.x, self.rect.y))
       
        

    def update(self, events):
        '''
        Controls player behaviour.

        This method is called once per frame and will manage player logic.
        The controls method is only called here so will run once per frame as well.
        This method will not handle player movement or combat directly, instead it will "coordinate" other methods that do so here.
        Thus encapsulating player logic into one update method. 

        IMPORTANT:
        DESCRIPTION MISSING
        '''
        # -----------------------------------------
        # Event list ------------------------------
        self.events = events    # Loop through this list for controls
        # -----------------------------------------
        self.controls()
        
        # Movement
        if self.moving_up == True:
            self.rect.y -= self.speed
        if self.moving_down == True:
            self.rect.y += self.speed
        if self.moving_left == True:
            self.rect.x -= self.speed
        if self.moving_right == True:
            self.rect.x += self.speed




        

    def controls(self):
        '''
        Handles the player control logic
        
        Only Player movement is controled here.

        IMPORTANT:
        DESCRIPTION MISSING
        '''

        # ERROR: It looks like none of these conditions are excecuting when they should
        # Suggestion: Try using specific event instead
        events = self.events

        for event in events:
        # Movement Controls -----------------
            # Keydown  Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.moving_up = True
                if event.key == pygame.K_s:
                    self.moving_down = True
                if event.key == pygame.K_a:
                    self.moving_left = True
                if event.key == pygame.K_d:
                    self.moving_right = True
            # Key up Controls
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.moving_up = False
                if event.key == pygame.K_s:
                    self.moving_down = False
                if event.key == pygame.K_a:
                    self.moving_left = False
                if event.key == pygame.K_d:
                    self.moving_right = False
                
        # Direction controls -----------------
            # Keydown Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.facing_up = True
                if event.key == pygame.K_DOWN:
                    self.facing_down = True
                if event.key == pygame.K_LEFT:
                    self.facing_right = True
                if event.key == pygame.K_RIGHT:
                    self.facing_right == True
            
            # Key up controls
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.facing_up = False
                if event.key == pygame.K_DOWN:
                    self.facing_down = False
                if event.key == pygame.K_LEFT:
                    self.facing_left = False
                if event.key == pygame.K_RIGHT:
                    self.facing_right = False
                


        


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