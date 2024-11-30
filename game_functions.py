import pygame 
import sys
from bullet import Bullets
def check_events(ship,screen,bg_color,bullets):
    for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_UP:
                    ship.moving_up = True
                elif events.key == pygame.K_DOWN:
                    ship.moving_down = True
                elif events.key == pygame.K_SPACE:
                    if len(bullets) < 3:
                        new_bullets = Bullets(screen,ship)
                        bullets.add(new_bullets)
            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_UP:
                     ship.moving_up = False
                if events.key == pygame.K_DOWN:
                     ship.moving_down = False

    screen.fill(bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullets()
    pygame.display.flip()