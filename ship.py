import pygame

class Ship:
    def __init__(self,screen):
        self.screen = screen

        # Rectification
        self.image = pygame.image.load("images/ship_2.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Positioning
        self.rect.centery =self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centery)
        # Movement
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_up and self.rect.top>0:
            self.center -= 1.5
        if self.moving_down and self.rect.bottom<787:
            self.center += 1.5

        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
