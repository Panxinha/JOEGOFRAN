"""
Este modulo es para el powerup de velocidad
"""
import pygame
import random
from pygame.locals import (RLEACCEL)

from elements.projectile import Projectile

wing_png = pygame.image.load("VJ-2-Honors/assets/wing.png")
wing_png_scaled =pygame.transform.scale(wing_png, (55, 55))

class Wing(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Wing, self).__init__()
        self.surf = wing_png_scaled
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
