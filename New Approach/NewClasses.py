import pygame
'''
In this classes file, I will create the second versions of my classes to be used in my game proof of concept build
'''

class Player:
    def __init__(self, img: str, x=0, y=0):
        '''
        When the player is instantiated, it's image must be loaded so it can be rendered into the game.
        Other variables must also be stored for use in other methods.
        '''

        # Loads the chosen image so it can be rendered
        self.img = pygame.image.load(img)

        # x and y positions of the plauer
        self.x = x
        self.y = y

        # NOTE: SCALE VALUES HAVE BEEN DELETED


        # Cool down control

        pass

    def draw(self, surface):
        '''
        Draws/Renders the player image over another surface(Should be draw on window surface)
        The reason that the player is not draw when it is instantiated is because it allows me to control when the player is drawn
        as well as what it is drawn over and what is draw over it. Effectively controlling the "layer" that the player is drawn on.
        '''

        # This line of code will render the image wherever its x and y positions are
        # NOTE that the position does not describe the center of the image but actually the top-left corner of the image
        self.surface = surface.blit(self.img, (self.x, self.y))


    def turn(self, img: str):
        '''
        This method controls the direction that the player will be facing.
        It does this by changing the player's image with whatever image is passed as a parameter.
        '''
        self.img = pygame.image.load(img)

        pass

    def shoot(self):
        pass


'''
IDEAS HEADER(Ideas will go here):

Ammo system for player:
    -Player picks up bullets left on the ground to load up on ammo
    DECISION:
        Do not implement this in the prototype version.
'''



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
            self.speed = 10

            # Starting coordinates//Should be the player position
            self.x = x
            self.y = y

            # Sets the image of the bullet//Chose right one for each direction
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
