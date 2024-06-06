import pygame
from settings import *
from building import Building
from city import City

# init the city 
city = City()

pygame.init()

# draw screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
background = pygame.image.load(BACKGROUND_PIC)
background = pygame.transform.scale(background, ((SCREEN_WIDTH, SCREEN_HEIGHT)))

# run the game loop
run = True
while run:
    clock.tick(60)
    screen.fill('white')
    #screen.blit(background, (0,0))

    # The event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    city.scroll_down_all()
                elif event.button == 5:  # Scroll down
                    city.scroll_up_all()
                else:
                    position = event.pos
        
                    city.check_for_new_calls(position)
    
    keys = pygame.key.get_pressed()

    # Update scroll position based on arrow key presses
    if keys[pygame.K_LEFT]:
        city.scroll_right_all()
    if keys[pygame.K_RIGHT]:
         city.scroll_left_all()

    city.update_all()
    city.draw_all(screen)
    
    pygame.display.update()

pygame.quit()
