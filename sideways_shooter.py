import pygame
import sys
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullets
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Sideways Shooter")
    bg_color = (230,230,230)
    ship = Ship(screen)
    bullets = Group()
    while True:
        gf.check_events(ship,screen,bg_color,bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.x >= 1200:
                bullets.remove(bullet)

run_game()
