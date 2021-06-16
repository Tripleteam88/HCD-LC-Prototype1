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

    def __init__(self, x, y, WIN):
        '''
        Player class takes all the same parameters as a normal sprite.
        '''

        # Creates a sprite using the instance of the player
        pygame.sprite.Sprite.__init__(self)
        # Game window dimensions
        self.window_width = 1000
        self.window_height = 600
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
        
        # -----------------------------------------
        # Combat ----------------------------------
        self.bullet_list = [] # Stores fired bullets
        self.health = 200
        # -----------------------------------------

        
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
        # -----------------------------------------

    def draw(self, WINDOW):
       WINDOW.blit(self.image, (self.rect.x, self.rect.y))
       
        

    def update(self, WIN):
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
        # Bullet management
        self.manage_bullets(WIN)

        # Movement 
        if self.moving_up == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if self.moving_down == True and self.rect.y < self.window_height - self.rect.height:
            # The player's Point of reference( (x,y) coordinates) begins at the top left corner of the
            # To enforce the window boundry, this must be accouted for (see above)
            self.rect.y += self.speed
        if self.moving_left == True and self.rect.x > 0:
            self.rect.x -= self.speed
        if self.moving_right == True and self.rect.x < self.window_width - self.rect.width:
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
                    self.shoot('U')
                    
                    self.facing_up = True   # Only true value
                    self.facing_down = False
                    self.facing_left = False
                    self.facing_right = False   
                if event.key == pygame.K_DOWN:
                    self.shoot('D')

                    self.facing_up = False
                    self.facing_down = True # Only true value
                    self.facing_left = False
                    self.facing_right = False
                if event.key == pygame.K_LEFT:
                    self.shoot('L')

                    self.facing_up = False
                    self.facing_down = False
                    self.facing_left = True # Only true value
                    self.facing_right = False   
                if event.key == pygame.K_RIGHT:
                    self.shoot('R')
                    
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
    
    def shoot(self, direction):
        '''
        This method is used to create bullet objects(not manage them)
        When using the shoot method, please specify a direction
        Directions are specfied using a capital letter
        
        Examples:
        Left: "L"
        Right: "R"
        Down: "D"
        Up: "U"
        '''
        self.bullet_list.append(Bullet(self, direction))

    def manage_bullets(self, WIN):
        '''
        This method loops through the player's list of fired bullets.
        The bullet rendering is managed here.
        Bullets that exceed the game window's dimensions are deleted and no longer renderd.
        '''

        for bullet in self.bullet_list:
            if bullet.on_screen():
                bullet.move()
                bullet.draw(WIN)
            else:
                self.bullet_list.remove(bullet)

                





class Bullet(pygame.sprite.Sprite):
        '''
        Bullets are shot by the player, they deal damage to enemies and can only be shot 1 at a time.
        They should be made to despawn once they exit the window(player view).
        '''
        def __init__(self, player, direction):
            '''
            Bullet starts at player position and moves in 1 of 4 possible directions.
            The bullet direction must be an uppercase letter representing the direction of the bullet.
            These must be specified by passing them as parameters.
            Bullets are drawn once they are created. They have no draw function.
            '''

            self.player = player
            # Speed of the bullet
            self.speed = 25



            # Sets the image of the bullet//Chose right one for each direction // 'D', 'U'. 'L', 'R'
            self.image = pygame.image.load('Assets\Iteams\Bullet.png') # MANUAL DEFINITION FOR NOW
            self.rect = self.image.get_rect() # Creates rect object from image
            
            # Starting coordinates//Should be the player position
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y
            self.direction = direction
        
        def __str__(self):
            '''
            String method. Called when user prints a bullet object or calls the str function
            '''
            return f'Type: Bullet, X: {self.rect.x}, Y:  {self.rect.y}, Direction: {self.direction}' 

        def move(self):
            '''
            This method handles the movement of each bullet.
            It takes no arguments. It must be called on each bullet in order to move them.

            '''
            if self.direction == 'L':
                self.rect.x -= self.speed
            elif self.direction == 'R':
                self.rect.x += self.speed
            elif self.direction == 'U':
                self.rect.y -= self.speed
            elif self.direction == 'D':
                self.rect.y += self.speed

        def draw(self, WIN):
            '''
            This method will render the bullets to the screen.
            '''
            WIN.blit(self.image, (self.rect.x, self.rect.y))
        
        def on_screen(self):
            '''
            This method will check if the bullet has left the screen view.
            It should be called in the player manage_bullets method
            
            Returns
            ------------------------------------------------
            boolean --> True (bullet is off screen)
            boolean --> False (bullet is not off screen)
            '''
            # Check if bullets are in the window area // Set window size manually for now
            if self.rect.x > 1000 or self.rect.x < 0:
                return False
            if self.rect.y > 600 or self.rect.x < 0:
                return False
            else: 
                return True


class Manager:
    """
    As the name implies, this object manages all the enemies in a level.
    """
    def __init__(self, player, enemy_list):
        
        
        # Stores values with (data types)
        self.player: Player = player
        
        self.enemies: list = enemy_list
    
    def manage_enemies(self):
        pass

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
    """
    This is the basic enemy class that the player battles in the game.
    I may want different types of enemies so this class should be very minimal.
    """
    def __init__(self, image):

        # Image and rect objects
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        
        # Combat variables
        self.health = 150
        self.speed = 2 

    def draw(self, WIN):
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        
    def move(self, player):
        '''
        Will move the enemy towards the player's position.
        '''
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed

    def is_hit(self, bullet):
        """
        This method should be called by the manager class.
        It will check if a given bullet has hit the enemy object
        """
        if self.rect.colliderect(bullet.rect):
            return True
        else:
            return False

    def update(self, player):
        
        # Move towards player
        self.move(player)

        
        

    


# =============================================================================================
# =============================================================================================




# =============================================================================================
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Game functions ///////////////////////////////////////
# =============================================================================================



# =============================================================================================
# =============================================================================================