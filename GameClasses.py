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

        # Animation control // Direction // Single Letter // Starts as Down
        self.direction = 'D'    # Starting direction of the player
        # Animation Frame counter
        self.frame_counter = 0  # Used to count frames per animation
        # Movement variables // Are True when the player moves
        self.up = False
        self.right = False
        self.left = False
        self.down = False

        # Animation speed and timer 
        self.animation_speed = 16
        self.animate_time = 16 #Each animation will appear for these many frames


        # x and y positions of the plauer
        self.x = x
        self.y = y

        # Cool down control
        self.cooldown = 25

    def Move(self, context: str, animation: list):
        '''
        Method is called on keypress.


        The player animation method takes the context of the desired animation as a parameter.
        This context may be, direction of movement, whether or not the player is hurt or dead, etc.
        This method also needs a list, containing the desired animation's images.
        
        **STILL IN DEVELOPMENT**
        
        '''
        # Iterate over a list of images to animate
        # Only iterate after N amount of frames //  Determined by frame counter
        # Every N frames, the index should increase. If it hits the list limit it should reset
        # Use frame counter to count
        self.frame_counter = 0
        self.total_images = len(animation)
        self.image_index = 0
        self.frames_per_image = 7
        ##total_frames = total_images * frames_per_image  # Each image will hold for N amount of  frames 

        # The animation is set here
        self.img = animation[self.image_index]



        # Count frames
        if self.frame_counter < self.frames_per_image:
            # Will add 1 to the value of the frame counter
            # This is done once per frame
            self.frame_counter += 1
            self.img = self.img # Image is not changed

        if self.frame_counter == self.frames_per_image and self.image_index < self.total_images:
            # If the time limit for the image in the animation is reached
            # The frame counter will reset and the next image will be played
            self.frame_counter = 0
            self.image_index += 1

            # Remember to reset image index after total 
            # Use clock function

        print(self.frame_counter)
        print(self.image_index)

        # It is possible that there is a conflicting method that keeps reseting the player image
        # NOTE: I think i'm gonna need a lot more class variables
        # I think what is happening is that my variable values are not being saved into the next frame
        # My whole movement system may need a rework
        return animation


    def Draw(self, surface):
        '''
        Draws/Renders the player image over another surface(Should be draw on window surface)
        The reason that the player is not draw when it is instantiated is because it allows me to control when the player is drawn
        as well as what it is drawn over and what is draw over it. Effectively controlling the "layer" that the player is drawn on.
        '''

        # This line of code will render the image wherever its x and y positions are
        # NOTE that the position does not describe the center of the image but actually the top-left corner of the image
        self.surface = surface.blit(self.img, (self.x, self.y))

    def turn(self, img: str, direction: str):
        '''
        This method controls the direction that the player will be facing.
        It does this by changing the player's image with whatever image is passed as a parameter.
        '''
        
    
        ##self.img = pygame.image.load(img)
        self.direction = direction
        
        

    def shoot(self, bullet_image: str,bullet_list: list):
        '''
        This method will be used to add bullets to the bullets list.
        This will replace the current rudementary shooting system and stop spam shooting.
        '''


        

        # Direction string should follow game logic// Currently single letter
        # bullet_image string should be the image path to be used on the bullet
        if self.cooldown == 25:
            
            
            bullet_list.append(Bullet(bullet_image, self.x, self.y, self.direction))
            
            # Resets cooldown time to 0// VALUE IS NOT FINAL
            self.cooldown = 0
        
        return bullet_list
        
    def handle_cooldown(self):
        '''
        This function should be called after the shoot function.
        '''
        if self.cooldown < 25:
            self.cooldown += 1




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

            # Sets the image of the bullet//Chose right one for each direction
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

    def animate(self, context: str):
        pass

    def move(self):
        '''
        Enemies will move towards the player 
        '''
        pass

    def turn(self):
        pass

    def draw(self):
        pass
