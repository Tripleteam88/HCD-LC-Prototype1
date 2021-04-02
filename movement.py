import pygame 
pygame.init()

# Window variable, attributes and methods
window = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Game time')
# Remember that pygame uses a special grid
# Moving right adds to the x-value
# Moving down adds to the y-value



x = 50
y = 50
width = 40
height = 40
vel = 6

# run variable begins the 'game loop'
run = True
while run:
    # The pygame delay method takes miliseconds as a parameter
    # 100 milisecond delay just means that the rest of our code in the loop will not be executed until after 100 miliseconds
    # May remove this, may not. Depends on how useful this may be
    pygame.time.delay(100)

    for event in pygame.event.get():
        # For loop to check for events
        # Events can be accessed with the .type method
        if event.type == pygame.QUIT:
            run = False 

    #Key list//Like the key functions from pgz
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel


    window.fill((0))
    # Must draw my player object using rects
    pygame.draw.rect(window, (255,0,0), (x,y,width,height))
    pygame.display.update()
# When loop is broken out of
pygame.quit()