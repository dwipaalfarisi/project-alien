import pygame

class Ship:
    "Class to manage the ship"

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and gets its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Starteach new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the ship at its location"""
        self.screen.blit(self.image, self.rect)