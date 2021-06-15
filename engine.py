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

    def __init__(self, x, y):
        '''
        Player class takes all the same parameters as a normal sprite.
        '''

        # Creates a sprite using the instance of the player
        pygame.sprite.Sprite.__init__(self)

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
        # Images (Manually defined) ---------------
        # -----------------------------------------
        self.image_down = pygame.image.load('Assets\Player\IDLE\PlayerDownIDLE.png').convert()
        self.image_up = pygame.image.load('Assets\Player\IDLE\PlayerUpIDLE.png').convert()
        self.image_left = pygame.image.load('Assets\Player\IDLE\PlayerLeftIDLE.png').convert()
        self.image_right = pygame.image.load('Assets\Player\IDLE\PlayerRightIDLE.png').convert()
        # -----------------------------------------
        # -----------------------------------------
        # Sprite parameters -----------------------
        # -----------------------------------------
        # Player Rect -----------------------------
        self.image = self.image_down
        # Automatically sets dimensions from image
        self.rect = self.image.get_rect()
        # Position parameters
        self.rect.x = x
        self.rect.y = y
        # Suface 
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
    
    def draw(self, WINDOW):
       WINDOW.blit(self.image, (self.rect.x, self.rect.y))
       
        

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

        # Manages game events (including player controls)
        self.event_control()

        # Movement 
        if self.moving_up == True:
            self.rect.y -= self.speed
        if self.moving_down == True:
            self.rect.y += self.speed
        if self.moving_left == True:
            self.rect.x -= self.speed
        if self.moving_right == True:
            self.rect.x += self.speed
        # Direction
        if self.facing_up == True:
            self.image = self.image_up
        if self.facing_down == True:
            self.image = self.image_down
        if self.facing_left == True:
            self.image = self.image_left
        if self.facing_right == True:
            self.image = self.image_right



    def event_control(self):
        """
        
        """
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            # Keydown controls 
            if event.type == pygame.KEYDOWN:
                # Movement 
                if event.key == pygame.K_w:
                    self.moving_up = True
                if event.key == pygame.K_s:
                    self.moving_down = True
                if event.key == pygame.K_a:
                    self.moving_left = True
                if event.key == pygame.K_d:
                    self.moving_right = True

                # Directional controls
                if event.key == pygame.K_UP:
                    self.facing_up = True   # Only true value
                    self.facing_down = False
                    self.facing_left = False
                    self.facing_right = False   
                if event.key == pygame.K_DOWN:
                    self.facing_up = False
                    self.facing_down = True # Only true value
                    self.facing_left = False
                    self.facing_right = False
                if event.key == pygame.K_LEFT:
                    self.facing_up = False
                    self.facing_down = False
                    self.facing_left = True # Only true value
                    self.facing_right = False   
                if event.key == pygame.K_RIGHT:
                    self.facing_up = False
                    self.facing_down = False
                    self.facing_left = False 
                    self.facing_right = True # Only true value                


            # Keyup controls
            if event.type == pygame.KEYUP:
                # Movement
                if event.key == pygame.K_w:
                    self.moving_up = False
                if event.key == pygame.K_s:
                    self.moving_down = False
                if event.key == pygame.K_a:
                    self.moving_left = False
                if event.key == pygame.K_d:
                    self.moving_right = False
                 
    def shoot(self):
        pass




class Bullet:
        '''
        Bullets are shot by the player, they deal damage to enemies and can only be shot 1 at a time.
        They should be made to despawn once they exit the window(player view).
        '''
        def __init__(self, img: str, x, y, direction):
            '''
            Bullet starts at player position and moves in 1 of 4 possible directions.
            The bullet direction must be an uppercase letter representing the direction of the bullet.
            These must be specified by passing them as parameters.
            Bullets are drawn once they are created. They have no draw function.
            '''

            # Speed of the bullet
            self.speed = 25

            # Starting coordinates//Should be the player position
            self.x = x
            self.y = y

            # Sets the image of the bullet//Chose right one for each direction // 'D', 'U'. 'L', 'R'
            self.img = pygame.image.load(img)
            self.direction = direction


        def move(self):
            '''
            This method handles the movement of each bullet.
            It takes no arguments. It must be called on each bullet in order to move them.
            '''
            if self.direction == 'L':
                self.x -= self.speed
            elif self.direction == 'R':
                self.x += self.speed
            elif self.direction == 'U':
                self.y -= self.speed
            elif self.direction == 'D':
                self.y += self.speed


        def draw(self, WIN):
            '''
            This method should take the game window as a parameter
            '''
            WIN.blit(self.img, (self.x, self.y))


        def collide(self):
            '''
            This method handles what happens when a bullet collides with another object.
            '''
            pass

# =============================================================================================
# =============================================================================================




# =============================================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game functions ///////////////////////////////////////
# =============================================================================================



# =============================================================================================
# =============================================================================================