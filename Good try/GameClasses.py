import pygame
'''
In this classes file, I will create the second versions of my classes to be used in my game proof of concept build
'''

'''
IDEAS HEADER(Ideas will go here):


LIMIT PLAYER SHOOTING:
    - Make another cooldown after the player has shot more then X amount of times
    in a single direction.
    * This encourages player movement and adds more engagement to the game
    STATUS:
        Does not need to be apart of the PROTOTYPE BUILD(pre-alpha)
    
    DECISION:
        ADD TO GAME

    # Function must check directional count first
    # If user has shot 3 consecutive shots in the same direction user will not be allowed to shoot  
    # A shot timer may be needed to prevent bug
    # (Player directional cooldown is not reset once they stop shooting)
    # 
    # POSSIBLE FIXES:
    #   Begin reset timer once the player shoots in another direction
    #   Add a manual reload feature
    #  
    #   Combination of all fixes   


Ammo system for player:
    -Player picks up bullets left on the ground to load up on ammo
    DECISION:
        Do not implement this in the prototype version.


ENEMY AND PLAYER HEALTHBARS:
    - Create healthbars that float over the player and the enemies' heads.


ANIMATIONS:
    - All sprites need an animation method.
    Animation method should take the context as a parameter.
    The context will decide which animation to play.

'''



class Player:
    def __init__(self, img: str, x=0, y=0):
        '''
        When the player is instantiated, it's image must be loaded so it can be rendered into the game.
        Other variables must also be stored for use in other methods.
        '''

        # Loads the chosen image so it can be rendered
        self.img = pygame.image.load(img)


        # Direction // Animation and movement control // Single Letter // Starts as Down
        self.direction = 'D'    # Starting direction of the player
    
        
        # Player idle images
        self.img_left = 'Assets\Player\IDLE\PlayerLeftIDLE.png'
        self.img_right = 'Assets\Player\IDLE\PlayerRightIDLE.png'
        self.img_down = 'Assets\Player\IDLE\PlayerDownIDLE.png'
        self.img_up = 'Assets\Player\IDLE\PlayerUpIDLE.png'

        # Animation controls // Represnts what direction the player is in motion towards
        self.left = False
        self.right = False
        self.down = False
        self.up = False

        # Animation lists
        self.right_animation = [pygame.image.load('Assets\Player\Animations\Right\R1.png'), 
                                pygame.image.load('Assets\Player\Animations\Right\R2.png'), 
                                pygame.image.load('Assets\Player\Animations\Right\R3.png'),
                                pygame.image.load('Assets\Player\Animations\Right\R4.png'), 
                                pygame.image.load('Assets\Player\Animations\Right\R5.png'), 
                                pygame.image.load('Assets\Player\Animations\Right\R6.png'),
                                pygame.image.load('Assets\Player\Animations\Right\R7.png'), 
                                pygame.image.load('Assets\Player\Animations\Right\R8.png')]



        # x and y positions of the plauer
        self.x = x
        self.y = y

        # Cool down control
        self.cooldown = 25


    def animate(self):
        pass

    def draw(self, surface):


    def Walking(self):
        '''
        This method triggers the animation variables to True.
        It should be called only when the user is pressing down on a key.
        '''
        if self.direction == 'D':
            # If player is facing down
            self.down =True

        if self.direction == 'U':
            # If player is facing up
            self.up = True
            
        if self.direction == 'L':
            # If player is facing left
            self.left = True
                
        if self.direction == 'R':
            # If player is facing right
            self.right = True

    def Halt(self):

        '''
        The animation contorl values  return to false.
        Image set to the idle(for current direction) once the user releases the key.
        This method should be called when the user realeases a key.
        '''


        # This line of code will render the image wherever its x and y positions are
        # NOTE that the position does not describe the center of the image but actually the top-left corner of the image
        self.surface = surface.blit(self.img, (self.x, self.y))

    def turn(self, img: str):

        if self.direction == 'U':
            self.up = False
            self.img = pygame.image.load(self.img_up)
            
        if self.direction == 'D':
            self.down = False
            self.img = pygame.image.load(self.img_down)
            
        if self.direction == 'R':
            self.right = False
            self.img = pygame.image.load(self.img_right)
            
        if self.direction == 'L':
            self.left = False
            self.img = pygame.image.load(self.img_left)
    
    def Turn(self, direction: str):

        '''
        This method updates the direction that the player is facing.
        '''

        self.img = pygame.image.load(img)

        pass

    def shoot(self, bullet_image: str,bullet_list: list, direction: str):

        
        self.direction = direction
    
    def Animate(self):
        '''
        DESCRIPTION MISSING

        '''
        # Get it working with right animation first.
        
        if self.direction == 'R' and self.right == True:
            # Excecutes when the player is moving left
            
            
            pass
            
        
        
        pass

        

    def Shoot(self, bullet_image: str,bullet_list: list):

        '''
        This method will be used to add bullets to the bullets list.
        This will replace the current rudementary shooting system and stop spam shooting.
        '''



        

        # Direction string should follow game logic// Currently single letter
        # bullet_image string should be the image path to be used on the bullet
        if self.cooldown == 25:
            

            
            bullet_list.append(Bullet(bullet_image, self.x, self.y, direction))

            bullet_list.append(Bullet(bullet_image, self.x, self.y, self.direction))

            
            # Resets cooldown time to 0// VALUE IS NOT FINAL
            self.cooldown = 0
        
        return bullet_list
        
    def HandleCooldown(self):
        '''
        This function should be called after the shoot function.
        '''
        if self.cooldown < 25:
            self.cooldown += 1


    def Update(self):
        '''
        Updates important player related variables from frame to frame. 
        '''

        # Movement controls
        
        
        
        
        pass


    def Draw(self, surface):
            '''
            Draws/Renders the player image over another surface(Should be draw on window surface)
            The reason that the player is not draw when it is instantiated is because it allows me to control when the player is drawn
            as well as what it is drawn over and what is draw over it. Effectively controlling the "layer" that the player is drawn on.
            '''

            # This line of code will render the image wherever its x and y positions are
            # NOTE that the position does not describe the center of the image but actually the top-left corner of the image
            self.surface = surface.blit(self.img, (self.x, self.y))



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


            

        def animate(self, context):
            pass


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


        def draw(self, surface):
            '''
            This method should take the game window as a parameter
            '''
            self.surface = surface.blit(self.img, (self.x, self.y))


        def collide(self):
            '''
            This method handles what happens when a bullet collides with another object.
            '''
            pass


class Enemy:
    '''
    Enemies are the player's adversary, they will follow the player to try to attack.
    They are killed once they take enough damage from the player's bullets.
    '''

    def __init__(self, img: str, x:int, y:int) -> None:
        '''
        The enemy class must be instansiated with a starting image and a starting position(x,y)
        '''
        # Load enemy image
        self.img = pygame.image.load(img)

        # Load enemy starting position
        self.x = x
        self.y = y

        # Enemy Health // NOT FINAL
        self.health = 300

        

    def move(self):
        '''
        Enemies will move towards the player 
        '''
        pass

    def turn(self):
        pass

    def draw(self):
        pass
