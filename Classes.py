import pygame

class Player:
    def __init__(self, img: str, WIDTH, HEIGHT, x=0, y=0, ang=0):
        
        # Pygame image is loaded
        self.img = pygame.image.load(img)  


        # x and y positions
        self.x = x
        self.y = y
        
        # Player Angle//May delete
        self.ang = ang        

        # Scale values for image       
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        # Shooting//Cool-down
        
        

    def draw(self, surface):
        self.surface = surface.blit(self.img, (self.x, self.y))

        
    def animate(self, img):
        self.img = pygame.image.load(img)

    def shoot(self, direction):
        # Implement shooting cool-down

        pass
        
class Bullet:
    def __init__(self, img,x, y, direction):
        '''
        Bullet starts at player position and moves in 1 of 4 possible directions
        '''
        # Speed of the bullet
        self.speed = 10

        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.direction = direction


        pass


    def draw(self, surface):
        self.surface = surface.blit(self.img, (self.x, self.y))

        pass

    def move(self):
        
        if self.direction == 'L':
            self.x -= self.speed
        elif self.direction == 'R':
            self.x += self.speed
        elif self.direction == 'U':
            self.y -= self.speed
        elif self.direction == 'D':
            self.y += self.speed
        