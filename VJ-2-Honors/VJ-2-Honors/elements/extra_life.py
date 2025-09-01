"""
este modulo es para el power up de vida extra
"""
import pygame
import random
from pygame.locals import (RLEACCEL)

from elements.projectile import Projectile

Extra_lifepng = pygame.image.load('VJ-2-Honors/assets/extra_life.png')
Extra_life_png_scaled = pygame.transform.scale(Extra_lifepng, (55, 55))

class Extra_life(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Extra_life, self).__init__()
        self.surf = Extra_life_png_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # posicion inicial se genera aleatoriamente, con random.randint
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 0
        self.projectiles = pygame.sprite.Group()


    def power_up(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
        self.projectiles.update()