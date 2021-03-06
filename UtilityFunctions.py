import pygame
from NewClasses import Player, Bullet
'''
For the purposes of this program, some variables will need to be set.
'''

# Player Images go here // Change these when images are replaced
# Globals may be useful // Try to avoid if possible



def check_events():
    '''
    DESCRIPTION MISSING
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def check_keys(player: Player, bullet_list: list, speed: int, surface):
    '''
    This function will check the keys pressed and control what those keys do
    '''

    # Variables for player image
    PLayerRight = 'New Approach\Images\ArrowR.png'
    PLayerLeft = 'New Approach\Images\ArrowL.png'
    PLayerUP = 'New Approach\Images\ArrowU.png'
    PLayerDown = 'New Approach\Images\ArrowD.png'


    keys = pygame.key.get_pressed()

    # Movement controls // Speed parameter is the speed of the player
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed


 # TODO: store bullet string in a variable with a new function parameter 
    # Direction Controls: Turns player // Bullets need more images
    if keys[pygame.K_LEFT]:
        player.turn(PLayerLeft)
        player.shoot('New Approach\Images\Bullet.png', bullet_list, 'L')

    elif keys[pygame.K_RIGHT]:
        player.turn(PLayerRight)
        player.shoot('New Approach\Images\Bullet.png', bullet_list, 'R')

    elif keys[pygame.K_UP]:
        player.turn(PLayerUP)
        player.shoot('New Approach\Images\Bullet.png', bullet_list, 'U')
        

    elif keys[pygame.K_DOWN]:
        player.turn(PLayerDown)
        player.shoot('New Approach\Images\Bullet.png', bullet_list, 'D')

    # Should always be called in the main loop 
    player.handle_cooldown()


    if keys[pygame.K_ESCAPE]:
        # Exit key, press esc to quit
        pygame.quit()

    # Updates the list that was passed // No need for globals
    return bullet_list

def bullet_control(bullet_list: list, surface):
    '''
    Will control the bullets on screen.
    The game window should be passed as the parameter.
    '''
    for bullet in bullet_list:
        bullet.move()
        
    
    return bullet_list

def draw_bullets(bullet_list: list, surface):

    for bullet in bullet_list:
        bullet.draw(surface)

    return bullet_list