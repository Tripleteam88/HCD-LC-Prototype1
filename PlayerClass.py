import pygame

class Player:
    def __init__(self, img: str, WIDTH, HEIGHT, x=0, y=0, ang=0):
        
        # Pygame image is loaded
        self.img = pygame.image.load(img)  


        # x and y positions
        self.x = x
        self.y = y
        
        # Player Angle
        self.ang = ang        

        # Scale values for image       
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
    
    def rotate(self, angle):
        # Direction can be either up, down, left or right
        
        # Test
        self.img = pygame.transform.rotate(self.img, angle)
        pass

    def draw(self, surface):
        self.surface = surface.blit(self.img, (self.x, self.y))

        pass
        
    def animate(self, img):
        self.img = pygame.image.load(img)


        pass