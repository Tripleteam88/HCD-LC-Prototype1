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
    PLayerRight = 'ArrowR.png'
    PLayerLeft = 'ArrowL.png'
    PLayerUP = 'ArrowU.png'
    PLayerDown = 'ArrowD.png'


    keys = pygame.key.get_pressed()

    # Movement controls
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed


    # Direction Controls: Turns player // Bullets need more images
    if keys[pygame.K_LEFT]:
        player.turn(PLayerLeft)
        bullet_list.append(Bullet('bullet.png', player.x, player.y, 'L'))

    if keys[pygame.K_RIGHT]:
        player.turn(PLayerRight)
        bullet_list.append(Bullet('bullet.png', player.x, player.y, 'R'))

    if keys[pygame.K_UP]:
        player.turn(PLayerUP)
        bullet_list.append(Bullet('bullet.png', player.x, player.y, 'U'))

    if keys[pygame.K_DOWN]:
        player.turn(PLayerDown)
        bullet_list.append(Bullet('bullet.png', player.x, player.y, 'D'))

    if keys[pygame.K_ESCAPE]:
        # Exit key, press esc to quit
        pygame.quit()

    return bullet_list

def bullet_control(bullet_list: list, surface):
    '''
    Will control the bullets on screen.
    The game window should be passed as the parameter
    '''
    for bullet in bullet_list:
        bullet.move()
        
    
    return bullet_list

def draw_bullets(bullet_list: list, surface):

    for bullet in bullet_list:
        bullet.draw(surface)

    return bullet_list