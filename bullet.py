import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self,screen,ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,15,3)
        self.rect.y = ship.rect.centery
        self.rect.x = ship.rect.right
        self.x = float(self.rect.x)
        self.color = 60,60,60
        self.allowed_number = 3
    def update(self):
        self.x += 1.5
        self.rect.x = self.x

    def draw_bullets(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
